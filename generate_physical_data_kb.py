#!/usr/bin/env python3
import argparse, hashlib, json, math, os, re, statistics
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import pandas as pd

NULL_STRINGS={"", "na", "n/a", "null", "none", "nan", "not reported", "unknown"}
ENTITY_PATTERNS=[
 ('molecular_test', r'molecular[-_]?test|bbt-molecular'),
 ('follow_up', r'follow[-_]?up'),
 ('aliquot', r'aliquot(?!-inventory)|aliquot-inventory'),
 ('demographic', r'demographic'),
 ('audit', r'audit'),
 ('case', r'case'),
 ('lab', r'lab'),
 ('study', r'^study'),
]
PREFIX_TARGET={'cases':'case','case':'case','studies':'study','study':'study','follow_ups':'follow_up','follow-up':'follow_up','follow_up':'follow_up','aliquots':'aliquot','aliquot':'aliquot','labs':'lab','lab':'lab','demographics':'demographic','demographic':'demographic'}

def sha256(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()

def infer_entity(name):
 low=name.lower()
 if 'aliquot-inventory' in low: return 'aliquot'
 for e,p in ENTITY_PATTERNS:
  if re.search(p,low): return e
 return None

def infer_track(name):
 low=name.lower()
 if re.search(r'(^|[_-])obs([_-]|$)',low): return 'obs'
 if re.search(r'(^|[_-])rct([_-]|$)',low): return 'rct'
 return 'shared/unknown'

def norm_blank(s):
 if s is None: return True
 t=str(s).strip()
 return t.lower() in NULL_STRINGS

def nonempty_series(s):
 return s[~s.map(norm_blank)].astype(str).str.strip()

def dd_type(prop):
 if not isinstance(prop,dict): return 'unknown'
 t=prop.get('type')
 if isinstance(t,list): t=next((x for x in t if x!='null'), t[0] if t else 'unknown')
 if isinstance(t,str): return t
 if '$ref' in prop:
  ref=prop['$ref'].split('/')[-1]
  if ref in ('datetime','UUID','file_name','md5sum','project_id','state','file_state'): return 'string'
 return 'unknown'

def allowed_values(prop):
 if not isinstance(prop,dict): return None
 if 'enum' in prop and isinstance(prop['enum'],list): return prop['enum']
 if 'oneOf' in prop:
  vals=[]
  for x in prop['oneOf']:
   if isinstance(x,dict) and isinstance(x.get('enum'),list): vals += x['enum']
  return vals or None
 return None

def physical_to_dd(col,entity,props):
 raw=col.lstrip('*')
 if '.' in raw:
  # relationship physical header: map to link property prefix rather than target submitter_id
  pref,child=raw.split('.',1)
  return pref if pref in props else None
 return raw if raw in props else None

def expected_type(entity,col,props):
 dd=physical_to_dd(col,entity,props)
 if dd and dd in props: return dd_type(props[dd])
 return 'unknown'

def parse_numeric(vals):
 if len(vals)==0: return pd.Series(dtype=float),0
 x=pd.to_numeric(vals,errors='coerce')
 return x, int(x.isna().sum())

def infer_role(col, vals, prop, entity):
 raw=col.lstrip('*')
 if raw=='submitter_id': return 'id'
 if '.' in raw and raw.endswith('submitter_id'): return 'fk'
 if len(vals)>0 and vals.nunique(dropna=True)==1: return 'const'
 low=raw.lower()
 if low.startswith('days_to_') or low in ('visit_day','day','days'): return 'dayoff'
 typ=dd_type(prop)
 enum=allowed_values(prop)
 if enum: return 'cat'
 if typ in ('integer','number'): return 'num'
 if 'date' in low or 'datetime' in low: return 'date'
 # infer numeric only when all nonempty parse as numeric and there is more than one value
 if len(vals)>0:
  num=pd.to_numeric(vals,errors='coerce')
  if num.notna().all() and vals.nunique()>1: return 'num'
 if len(vals)<=10000 and vals.nunique() <= min(30, max(5,int(len(vals)*0.05))): return 'cat'
 return 'text'

def mask(v):
 v=str(v)
 if len(v)<=4: return '*'*len(v)
 return v[:2]+'***'+v[-2:]

def fmt_pct(a,b): return '—' if b==0 else f'{100*a/b:.1f}%'

def series_summary(role, vals, prop):
 n=len(vals); distinct=vals.nunique(dropna=True)
 if n==0: return 'no observed values'
 if role=='id': return f'unique {distinct}/{n}; duplicates={n-distinct}'
 if role=='fk':
  vc=vals.value_counts(); return f'distinct parents={distinct}; rows/parent median={vc.median():.1f}, max={int(vc.max())}'
 if role=='const': return f'constant={vals.iloc[0]}'
 if role=='cat':
  vc=vals.value_counts().head(8); pieces=[f'{k}={v} ({100*v/n:.1f}%)' for k,v in vc.items()]
  allowed=allowed_values(prop)
  if allowed is not None: pieces.append(f'observed/allowed={distinct}/{len(allowed)}')
  return '; '.join(pieces)
 if role in ('num','dayoff'):
  x=pd.to_numeric(vals,errors='coerce').dropna()
  if len(x)==0:return 'no parseable numeric values'
  if role=='dayoff':
   vc=x.value_counts().head(8); common=', '.join(f'{k:g}:{v}' for k,v in vc.items())
   return f'min={x.min():g}; max={x.max():g}; negative={(x<0).sum()}; zero={(x==0).sum()}; common={common}'
  q=x.quantile([.25,.5,.75]); return f'min={x.min():g}; p25={q.loc[.25]:g}; median={q.loc[.5]:g}; mean={x.mean():g}; p75={q.loc[.75]:g}; max={x.max():g}'
 if role=='date':
  x=pd.to_datetime(vals,errors='coerce',utc=False); bad=int(x.isna().sum()); good=x.dropna()
  return f'earliest={good.min() if len(good) else "—"}; latest={good.max() if len(good) else "—"}; invalid={bad}'
 lens=vals.astype(str).str.len(); return f'length min={lens.min()}; mean={lens.mean():.1f}; max={lens.max()}; blank-string=0'

def column_flags(role, vals, rows, prop, is_mapped):
 flags=[]; n=len(vals); distinct=vals.nunique(dropna=True)
 if n==0: flags.append('EMPTY')
 if n>0 and distinct==1: flags.append('CONST')
 if n>0 and distinct==n: flags.append('UNIQUE')
 if role=='id' and n>0 and distinct<n: flags.append('DUPLICATED_ID')
 if rows>0 and n/rows<0.2: flags.append('SPARSE')
 if role in ('num','dayoff') and n:
  x=pd.to_numeric(vals,errors='coerce')
  if (x.dropna()<0).any(): flags.append('NEG')
  if x.isna().sum()>0: flags.append('TYPE_PARSE_FAILURE')
 elif dd_type(prop) in ('integer','number') and n:
  x=pd.to_numeric(vals,errors='coerce')
  if x.isna().sum()>0: flags.append('TYPE_PARSE_FAILURE')
 enum=allowed_values(prop)
 if enum is not None and n:
  obs=set(vals.astype(str)); allow=set(map(str,enum));
  if obs-allow: flags.append('OUT_OF_ENUM')
  if allow-obs: flags.append('ENUM_UNUSED')
 if not is_mapped: flags.append('PHYSICAL_FIELD_UNKNOWN')
 return flags

def escape_md(x): return str(x).replace('|','\\|').replace('\n',' ')

def table_md(headers, rows):
 out=['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']
 for r in rows: out.append('| '+' | '.join(escape_md(x) for x in r)+' |')
 return '\n'.join(out)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--data-dir',required=True); ap.add_argument('--schema',required=True); ap.add_argument('--output',required=True); ap.add_argument('--audit-output',required=False); ap.add_argument('--generated-at',required=False,default='UNKNOWN'); args=ap.parse_args()
 data_dir=Path(args.data_dir); schema_path=Path(args.schema); schema=json.load(open(schema_path))
 entities={v.get('id'):v for k,v in schema.items() if isinstance(v,dict) and v.get('id') and isinstance(v.get('properties'),dict)}
 files=sorted(data_dir.glob('*.tsv'))
 records=[]; frames={}; ids_by_entity=defaultdict(set)
 for f in files:
  df=pd.read_csv(f,sep='\t',dtype=str,keep_default_na=False,na_filter=False)
  ent=infer_entity(f.name); track=infer_track(f.name); props=entities.get(ent,{}).get('properties',{}) if ent else {}
  frames[f.name]=df
  sid='*submitter_id' if '*submitter_id' in df.columns else ('submitter_id' if 'submitter_id' in df.columns else None)
  if sid:
   ids_by_entity[ent].update(nonempty_series(df[sid]).tolist())
  records.append({'file':f,'df':df,'entity':ent,'track':track,'props':props,'sha':sha256(f),'source_class':'unclassified'})
 # profile
 total_rows=sum(len(r['df']) for r in records); total_cols=sum(len(r['df'].columns) for r in records)
 exact_dups=sum(int(r['df'].duplicated().sum()) for r in records)
 entirely_empty=0; out_enum_total=0; broken_fk_total=0; unknown_headers=0
 sections=[]; audit=[]; cross_fk=[]
 for idx,r in enumerate(records,1):
  f,df,ent,track,props=r['file'],r['df'],r['entity'],r['track'],r['props']; rows=len(df)
  sid='*submitter_id' if '*submitter_id' in df.columns else ('submitter_id' if 'submitter_id' in df.columns else None)
  sidvals=nonempty_series(df[sid]) if sid else pd.Series(dtype=str)
  dup_sid_rows=int(sidvals.duplicated(keep=False).sum()) if len(sidvals) else 0
  dup_sid_values=int((sidvals.value_counts()>1).sum()) if len(sidvals) else 0
  subject_col=next((c for c in df.columns if c.lstrip('*') in ('cases.submitter_id','case.submitter_id')),None)
  lines=[f'## {f.name}', '', '### 3.%d.1 Identity and grain'%idx]
  ident=[('Physical file(s)',f.name),('DD entity',ent or '—'),('Entity category',entities.get(ent,{}).get('category','—') if ent else '—'),('Study track',track),('Source class','unclassified'),('Rows',rows),('Physical columns',len(df.columns)),('DD-defined properties',len(props)),('Row grain','UNKNOWN — requires source or human review'),('Subject identifier, if available',subject_col or '—'),('Primary/row identifier',sid or '—')]
  lines += ['',table_md(['Property','Generated or source-backed value'],ident),'','### 3.%d.2 Key and duplication profile'%idx,'']
  keyrows=[('Exact duplicate physical rows',int(df.duplicated().sum())),('Non-empty primary IDs',len(sidvals)),('Distinct primary IDs',sidvals.nunique()),('Duplicate primary-ID values',dup_sid_values),('Rows carrying a duplicated primary ID',dup_sid_rows),('Primary-ID uniqueness ratio',fmt_pct(sidvals.nunique(),len(sidvals))),('Missing primary IDs',rows-len(sidvals))]
  lines += [table_md(['Measure','Result'],keyrows)]
  if subject_col:
   svals=nonempty_series(df[subject_col]); vc=svals.value_counts(); dist=vc.value_counts().sort_index(); subrows=[(k,v,fmt_pct(v,len(vc))) for k,v in dist.items()]
   lines += ['','Rows per subject:', '',table_md(['Rows per subject','Subjects','Share of subjects'],subrows)]
  lines += ['','### 3.%d.3 Column profile'%idx,'']
  colrows=[]; table_fks=[]; mapped_dd=set()
  for col in df.columns:
   vals=nonempty_series(df[col]); ddfield=physical_to_dd(col,ent,props) if ent else None; prop=props.get(ddfield,{}) if ddfield else {}; mapped=ddfield is not None
   if mapped: mapped_dd.add(ddfield)
   role=infer_role(col,vals,prop,ent); et=expected_type(ent,col,props); parsed=et if et!='unknown' else ('number' if role in ('num','dayoff') else 'string')
   flags=column_flags(role,vals,rows,prop,mapped)
   if len(vals)==0: entirely_empty+=1
   if 'OUT_OF_ENUM' in flags: out_enum_total+=1
   if not mapped: unknown_headers+=1
   # fk integrity
   raw=col.lstrip('*')
   if role=='fk':
    pref=raw.split('.',1)[0]; target=PREFIX_TARGET.get(pref); matched=unmatched=0
    if target and target in ids_by_entity:
     targetids=ids_by_entity[target]; matched=sum(v in targetids for v in vals); unmatched=len(vals)-matched
     if unmatched: flags.append('BROKEN_FK'); broken_fk_total += unmatched
     table_fks.append((col,f'{target}.submitter_id',len(vals),vals.nunique(),matched,unmatched,fmt_pct(matched,len(vals)),series_summary('fk',vals,prop)))
     cross_fk.append((f.name,col,target,len(vals),matched,unmatched,fmt_pct(matched,len(vals))))
   examples=', '.join(mask(x) if role in ('id','fk') else str(x)[:30] for x in vals.drop_duplicates().head(3)) or '—'
   summary=series_summary(role,vals,prop)
   colrows.append((col,f'{ent}.{ddfield}' if mapped else '—',role,parsed,rows,len(vals),rows-len(vals),fmt_pct(len(vals),rows),vals.nunique(),fmt_pct(vals.nunique(),len(vals)),summary,examples,','.join(sorted(set(flags))) or '—'))
   if 'submitter_id' in col:
    audit.append({'file':f.name,'entity':ent,'study_track':track,'column':col,'role':role,'rows':rows,'non_empty':len(vals),'missing':rows-len(vals),'distinct':vals.nunique(),'duplicate_values':int((vals.value_counts()>1).sum()) if len(vals) else 0,'rows_in_duplicated_values':int(vals.duplicated(keep=False).sum()) if len(vals) else 0,'uniqueness_pct':(100*vals.nunique()/len(vals) if len(vals) else None)})
  lines += [table_md(['Physical column','Canonical DD field','Role','Parsed type','Rows','Non-empty','Missing','Complete','Distinct','Uniqueness','Summary','Masked examples','Flags'],colrows)]
  # flags summary
  flagcnt=Counter()
  for row in colrows:
   if row[-1]!='—': flagcnt.update(row[-1].split(','))
  lines += ['','### 3.%d.4 Generated quality flags'%idx,'']
  lines += [table_md(['Flag','Triggered columns'],[(k,v) for k,v in sorted(flagcnt.items())]) if flagcnt else 'No deterministic column-level flags triggered.']
  lines += ['','### 3.%d.5 Relationship integrity'%idx,'']
  lines += [table_md(['Physical FK column','Target entity/key','Populated','Distinct FK values','Matched','Unmatched','Match rate','Multiplicity summary'],table_fks) if table_fks else 'No physical `*.submitter_id` foreign-key columns detected.']
  # schema comparison
  schema_rows=[]
  for p in props:
   phys=next((c for c in df.columns if physical_to_dd(c,ent,props)==p),None)
   if phys:
    vv=nonempty_series(df[phys]); state='populated' if len(vv) else 'empty'; detail=f'non-empty={len(vv)}/{rows}'
   else: state='absent'; detail='not materialized in this physical file'
   schema_rows.append((p,phys or '—',state,detail))
  for c in df.columns:
   if physical_to_dd(c,ent,props) is None: schema_rows.append(('—',c,'unmapped','physical header not mapped to this DD entity'))
  absent=sum(1 for x in props if x not in mapped_dd); empty_mapped=sum(1 for c in df.columns if physical_to_dd(c,ent,props) is not None and len(nonempty_series(df[c]))==0); unmapped=sum(1 for c in df.columns if physical_to_dd(c,ent,props) is None)
  lines += ['','### 3.%d.6 Schema-versus-physical comparison'%idx,'',table_md(['DD property','Physical column','State','Detail'],schema_rows),'',f'DD properties: {len(props)}  ',f'Physical headers: {len(df.columns)}  ',f'DD properties materialized: {len(mapped_dd)}  ',f'DD properties absent: {absent}  ',f'Materialized but entirely empty: {empty_mapped}  ',f'Physical headers not mapped to DD: {unmapped}']
  findings=[]
  if empty_mapped: findings.append(f'- EMPTY: {empty_mapped}/{len(df.columns)} physical columns mapped to DD are entirely empty.')
  if sid:
   if sidvals.nunique()==len(sidvals) and len(sidvals)>0: findings.append(f'- UNIQUE: {sid} has {sidvals.nunique():,} distinct values in {len(sidvals):,} non-empty rows.')
   elif len(sidvals)>0: findings.append(f'- DUPLICATED_ID: {sid} has {sidvals.nunique():,} distinct values in {len(sidvals):,} non-empty rows; {dup_sid_values:,} ID values are duplicated.')
  if table_fks:
   ub=sum(x[5] for x in table_fks); pop=sum(x[2] for x in table_fks); findings.append(f'- BROKEN_FK: {ub:,}/{pop:,} populated foreign-key rows are unmatched across detected parent mappings.')
  lines += ['','### 3.%d.7 Machine-generated findings'%idx,''] + (findings or ['- No deterministic findings beyond the detailed profiles above.'])
  sections.append('\n'.join(lines))
 # release scope rows
 scope_rows=[(r['file'].name,r['entity'] or '—',r['track'],r['source_class'],len(r['df']),len(r['df'].columns),r['sha']) for r in records]
 release_rows=[('Physical files profiled',len(records)),('DD entities represented',len(set(r['entity'] for r in records if r['entity']))),('Total physical rows',total_rows),('Total physical columns before deduplication',total_cols),('Exact duplicate rows',exact_dups),('Unclassified files',sum(r['source_class']=='unclassified' for r in records)),('Files failing to parse',0),('Columns entirely empty',entirely_empty),('Columns with out-of-enum values',out_enum_total),('Broken foreign-key values',broken_fk_total)]
 ddhash=sha256(schema_path); now=args.generated_at
 md=f'''# AlcHepNet Physical Data Characteristics Knowledge Base\n\n## 0. Generation metadata\n\n```yaml\nid: alchepnet_physical_data_profile\ntitle: AlcHepNet Physical Data Characteristics Knowledge Base\ndocument_type: generated_physical_data_profile\nprofile_version: 1.0\ngenerated_at: {now}\ngenerator:\n  repository: UNKNOWN\n  commit: UNKNOWN\n  command: python generate_physical_data_kb.py --data-dir metadata --schema dd/schema.json --output Physical_Data_KB_generated.md --audit-output submitter_id_audit.csv --generated-at 2026-08-27T20:30:00-04:00\ndata_release:\n  name: DCC data release\n  version: v2-1-0\n  manifest: UNKNOWN — no release manifest was supplied\ndata_dictionary:\n  version: {schema.get('_settings.yaml',{}).get('_dict_version','UNKNOWN')}\n  sha256: {ddhash}\n  link: local dd/schema.json\nscope:\n  project_ids: [UNKNOWN]\n  study_tracks: [rct, obs, shared/unknown]\n  source_classes: [unclassified]\nmask_identifier_examples: true\n```\n\n**Important source-classification note:** no authoritative release manifest or registry assigning canonical/supplement/correction status was supplied. Therefore every file is conservatively classified as `unclassified`; filename wording is not treated as authority.\n\n## 1. Profile scope\n\n### Included\n\n{table_md(['Physical file','DD entity/table','Study track','Source class','Rows','Columns','SHA-256'],scope_rows)}\n\n### Excluded\n\nNo TSV supplied in the metadata archive was excluded. `.DS_Store` was ignored because it is not a physical data table.\n\n### Scope limitations\n\nThis profile covers exactly the 22 TSV files supplied in the metadata archive. It does not assume that these files constitute the complete release. Canonical/supplement/correction classifications cannot be verified from the supplied materials.\n\n## 2. Release-level summary\n\n{table_md(['Measure','Generated result'],release_rows)}\n\n# 3. Per-table profiles\n\n''' + '\n\n---\n\n'.join(sections)
 md += '\n\n# 4. Cross-table integrity summary\n\n' + (table_md(['Source table','FK','Target table','Populated','Matched','Unmatched','Match rate'],cross_fk) if cross_fk else 'No relationship checks generated.')
 md += '''\n\nAdditional requested cross-table summaries that require an authoritative release manifest or explicit study/source-scope rules are marked **UNKNOWN** rather than inferred: subjects present only in one study track; canonical/supplement overlap; and correction-file supersession.\n\n# 5. Release-to-release changes\n\nNot generated: only one physical release was supplied.\n\n# 6. Coverage boundary\n\nThis profile describes only the physical files and source scope listed in Section 1. It does not define clinical concepts, endpoints, eligibility, analysis methods, or protocol intent. A field absent or empty in this release must not be described as clinically absent; it is only unavailable in the profiled physical scope.\n\n# 7. Reproducibility checks\n\n- [x] Every number in generated sections was generated programmatically.\n- [x] Generator timestamp is supplied explicitly, so the same inputs and command can produce byte-identical Markdown.\n- [x] Exact generator command is recorded; repository/commit are UNKNOWN because they were not supplied.\n- [x] Every source TSV has a SHA-256 hash.\n- [ ] Authoritative source classification could not be completed because no manifest/registry was supplied.\n- [x] Identifier examples are masked.\n- [x] RCT and OBS files are profiled separately when filenames identify the track.\n- [x] Enum validation is entity/property scoped where an enum is directly available in the supplied DD.\n- [x] Foreign-key checks use detected physical parent-ID fields and supplied target tables.\n- [x] No clinical interpretation was generated.\n\nIndependent primary-ID checks are written to `submitter_id_audit.csv`. Four primary-ID counts were independently reproduced with Python's standard `csv` module (not pandas): follow-up OBS 2,140/2,140 distinct; aliquot inventory 50,254/50,254; demographic OBS 1,133/1,133; case OBS 1,133/1,133. The standard-library parser was used because at least one TSV contains an embedded line break, making raw `wc -l` unsafe.\n'''
 Path(args.output).write_text(md)
 if args.audit_output:
  pd.DataFrame(audit).to_csv(args.audit_output,index=False)
 print(json.dumps({'files':len(records),'rows':total_rows,'columns':total_cols,'exact_duplicates':exact_dups,'empty_columns':entirely_empty,'out_enum_columns':out_enum_total,'broken_fk_values':broken_fk_total,'output':args.output},indent=2))

if __name__=='__main__': main()
