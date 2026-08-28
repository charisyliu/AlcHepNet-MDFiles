# AlcHepNet Physical Data Characteristics Knowledge Base

## 0. Generation metadata

```yaml
id: alchepnet_physical_data_profile
title: AlcHepNet Physical Data Characteristics Knowledge Base
document_type: generated_physical_data_profile
profile_version: 1.0
generated_at: 2026-08-27T20:30:00-04:00
generator:
  repository: UNKNOWN
  commit: UNKNOWN
  command: python generate_physical_data_kb.py --data-dir metadata --schema dd/schema.json --output AlcHepNet_Physical_Data_KB_Final.md --audit-output AlcHepNet_submitter_id_QC.csv --generated-at 2026-08-27T20:30:00-04:00
data_release:
  name: DCC data release
  version: v2-1-0
  manifest: UNKNOWN — no release manifest was supplied
data_dictionary:
  version: 2.1.1
  sha256: 0409bafaf9e3550f0da112dcf9c1166afd4d7d1dcd704596e92382720e194ac4
  link: local dd/schema.json
scope:
  project_ids: [ARDaC-AlcHepNet]
  study_tracks: [rct, obs, shared/unknown]
  source_classes: [unclassified]
mask_identifier_examples: true
```

**Important source-classification note:** no authoritative release manifest or registry assigning canonical/supplement/correction status was supplied. Therefore every file is conservatively classified as `unclassified`; filename wording is not treated as authority.

## 1. Profile scope

### Included

| Physical file | DD entity/table | Study track | Source class | Rows | Columns | SHA-256 |
|---|---|---|---|---|---|---|
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001.tsv | aliquot | shared/unknown | unclassified | 20000 | 9 | 471699e65f9ae449d527e293b632f5cf6721ed4708170d4a85ba857c2486f02b |
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_002.tsv | aliquot | shared/unknown | unclassified | 6529 | 9 | 03578cff32d3ebd2f134265dfdd845193643292f8ce637cb6387f0d8d86a8190 |
| audit_obs_DCC_data_release_v2-1-0.tsv | audit | obs | unclassified | 1060 | 29 | 42781b961cd366ac30767ab4acb7304825287a26c668ac035ece3c340e9c0c64 |
| audit_rct_DCC_data_release_v2-1-0.tsv | audit | rct | unclassified | 134 | 29 | 69fed4761c6964cc0c8715474db43e25de70587bb12046f891cd959eb7de45ed |
| bbt-molecular-merged_valid_followupsdel1_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 1748 | 14 | 983e85eb5ac6923eba01b70187316e52cbcb2cf09fba9f898875976b2fe4b203 |
| demographic_obs_DCC_data_release_v2-1-0.tsv | demographic | obs | unclassified | 1133 | 19 | 79ba6f48c34ac0f22935310138be0e9143a7ac0b92515424b38e76f430113402 |
| demographic_rct_DCC_data_release_v2-1-0.tsv | demographic | rct | unclassified | 147 | 19 | 4fa25a8419bbfe941cdf52c084a4f75f6da15fd139bcaeec278f3cd8d48bce66 |
| mod_aliquot-inventory_DCC_data_release_v2-1-0_updated_labs_250815.tsv | aliquot | shared/unknown | unclassified | 50254 | 9 | 131b2e44003a106ad2ccd8626e3adfb18223ac4ccf37fc830a8fc2a34e66885b |
| mod_case_obs_DCC_data_release_v2-1-0_250815_minor.tsv | case | obs | unclassified | 1133 | 23 | 798f0c2119eb225a0e8c909fdb37742efdee6b522304c9cdee43fc5a71ba168a |
| mod_case_rct_DCC_data_release_v2-1-0_250815_minor.tsv | case | rct | unclassified | 147 | 23 | da9d2ae2f05a3a26ee4e919fd2fb7e11ef90859589155982b63bf5e410bff59b |
| mod_follow-up_add-on_cleaned_v2-1-0.tsv | follow_up | shared/unknown | unclassified | 25 | 106 | ce6d430d9515612fff7a80d4d109292f9ff5213d1e8c18ad6b394970216128b1 |
| mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv | follow_up | obs | unclassified | 2140 | 106 | 0a1460ac872379385e0f423d0948f57bcf35e49ac06f7c3f83c0e9eb83cc9c4d |
| mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv | follow_up | rct | unclassified | 834 | 106 | c9ac33734e9a0b86c9d55b1c6590d77af417a99c676c3a915dea05acc4642c3b |
| mod_lab_PI_DCC_data_release_v2-1-0_minor.tsv | lab | shared/unknown | unclassified | 11 | 20 | ddec428bda331818c80f8ab54c54683fbe8705c48b3296b963a35928482d1686 |
| mod_molecular-test_liangpunsakul-orm1_DCC_data_release_v2-1-0_minor.tsv | molecular_test | shared/unknown | unclassified | 164 | 14 | 6dc13d912b0023501d40521a6014f8f1f5ccc65bbe725b7e2b3332e45317b573 |
| mod_molecular-test_szabo_DCC_data_release_v2-1-0_fixed_duplicates_minor.tsv | molecular_test | shared/unknown | unclassified | 993 | 14 | 5ac8ebcfa706ebe19a4573eaa2be2e368a24c29d8fc2c2a6c95881e218f13789 |
| molecular-test_liangpunsakul-orm1_part2_DCC_data_release_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 40 | 14 | 7816b12c1ebcaaf9824537ba103024379857451a8b514a672a046c2799040c0b |
| molecular-test_mehal-ace_DCC_data_release_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 192 | 14 | bc3913e1bf3eab7f00aa4c03a8468dc5aa3253cec539239f6edfbd9d46e0b5b4 |
| molecular-test_mehal-renin_DCC_data_release_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 192 | 14 | 36538d8b746a6a6eb34765b96ccb95aba76b5c08624d28908046fce28d589571 |
| molecular-test_nagy-urine_DCC_data_release_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 1160 | 14 | aaf28a474578df957ce21351ed73779c126523b559f375adcf033daeb2f913a8 |
| molecular-test_schnabl_DCC_data_release_v2-1-0.tsv | molecular_test | shared/unknown | unclassified | 297 | 14 | 88e88218ab41269f452478c67dcb76ecaf9773a39151d93e1f5b4c2d1225d799 |
| study_DCC_data_release_v2-1-0.tsv | study | shared/unknown | unclassified | 2 | 8 | 669cf78868e7adb61a57388406f4022a0129423c560d7e5d0d60a01a8802f67d |

### Excluded

No TSV supplied in the metadata archive was excluded. `.DS_Store` was ignored because it is not a physical data table.

### Scope limitations

This profile covers exactly the 22 TSV files supplied in the metadata archive. It does not assume that these files constitute the complete release. Canonical/supplement/correction classifications cannot be verified from the supplied materials.

## 2. Release-level summary

| Measure | Generated result |
|---|---|
| Physical files profiled | 22 |
| DD entities represented | 8 |
| Total physical rows | 88335 |
| Total physical columns before deduplication | 627 |
| Exact duplicate rows | 0 |
| Unclassified files | 22 |
| Files failing to parse | 0 |
| Columns entirely empty | 341 |
| Columns with out-of-enum values | 0 |
| Broken foreign-key values | 0 |

# 3. Per-table profiles

## aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001.tsv

### 3.1.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001.tsv |
| DD entity | aliquot |
| Entity category | biospecimen |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 20000 |
| Physical columns | 9 |
| DD-defined properties | 13 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.1.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 20000 |
| Distinct primary IDs | 20000 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.1.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | aliquot.type | const | string | 20000 | 20000 | 0 | 100.0% | 1 | 0.0% | constant=aliquot | aliquot | CONST |
| project_id | aliquot.project_id | const | string | 20000 | 20000 | 0 | 100.0% | 1 | 0.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | aliquot.submitter_id | id | string | 20000 | 20000 | 0 | 100.0% | 20000 | 100.0% | unique 20000/20000; duplicates=0 | 71***04, 71***03, 71***02 | UNIQUE |
| *follow_ups.submitter_id | aliquot.follow_ups | fk | string | 20000 | 20000 | 0 | 100.0% | 2031 | 10.2% | distinct parents=2031; rows/parent median=7.0, max=38 | 71***_0, 42***_0, 42***_0 | — |
| labs.submitter_id | aliquot.labs | fk | string | 20000 | 20000 | 0 | 100.0% | 10 | 0.1% | distinct parents=10; rows/parent median=1229.0, max=6272 | la***_1, la***14, la***15 | — |
| aliquot_amount | aliquot.aliquot_amount | num | number | 20000 | 0 | 20000 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| aliquot_collection_unit | aliquot.aliquot_collection_unit | cat | string | 20000 | 0 | 20000 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| container_type | aliquot.container_type | cat | string | 20000 | 0 | 20000 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| specimen_type | aliquot.specimen_type | cat | string | 20000 | 20000 | 0 | 100.0% | 13 | 0.1% | Serum=3735 (18.7%); PBMC=3639 (18.2%); Platelet Poor Plasma=2847 (14.2%); Urine=2700 (13.5%); Lysed RBC=1383 (6.9%); Whole Blood (DNA)=1146 (5.7%); Platelet Rich Plasma=929 (4.6%); NEAT Plasma=875 (4.4%); observed/allowed=13/17 | Serum, Stool, Platelet Rich Plasma | ENUM_UNUSED |

### 3.1.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 3 |
| ENUM_UNUSED | 1 |
| SPARSE | 3 |
| UNIQUE | 1 |

### 3.1.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *follow_ups.submitter_id | follow_up.submitter_id | 20000 | 2031 | 20000 | 0 | 100.0% | distinct parents=2031; rows/parent median=7.0, max=38 |
| labs.submitter_id | lab.submitter_id | 20000 | 10 | 20000 | 0 | 100.0% | distinct parents=10; rows/parent median=1229.0, max=6272 |

### 3.1.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=20000/20000 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=20000/20000 |
| aliquot_amount | aliquot_amount | empty | non-empty=0/20000 |
| aliquot_collection_unit | aliquot_collection_unit | empty | non-empty=0/20000 |
| specimen_type | specimen_type | populated | non-empty=20000/20000 |
| container_type | container_type | empty | non-empty=0/20000 |
| project_id | project_id | populated | non-empty=20000/20000 |
| labs | labs.submitter_id | populated | non-empty=20000/20000 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=20000/20000 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 13  
Physical headers: 9  
DD properties materialized: 9  
DD properties absent: 4  
Materialized but entirely empty: 3  
Physical headers not mapped to DD: 0

### 3.1.7 Machine-generated findings

- EMPTY: 3/9 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 20,000 distinct values in 20,000 non-empty rows.
- BROKEN_FK: 0/40,000 populated foreign-key rows are unmatched across detected parent mappings.

---

## aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_002.tsv

### 3.2.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_002.tsv |
| DD entity | aliquot |
| Entity category | biospecimen |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 6529 |
| Physical columns | 9 |
| DD-defined properties | 13 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.2.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 6529 |
| Distinct primary IDs | 6529 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.2.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | aliquot.type | const | string | 6529 | 6529 | 0 | 100.0% | 1 | 0.0% | constant=aliquot | aliquot | CONST |
| project_id | aliquot.project_id | const | string | 6529 | 6529 | 0 | 100.0% | 1 | 0.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | aliquot.submitter_id | id | string | 6529 | 6529 | 0 | 100.0% | 6529 | 100.0% | unique 6529/6529; duplicates=0 | 51***01, 51***01, 51***01 | UNIQUE |
| *follow_ups.submitter_id | aliquot.follow_ups | fk | string | 6529 | 6529 | 0 | 100.0% | 656 | 10.0% | distinct parents=656; rows/parent median=5.0, max=37 | 51***68, 51***_0, 51***84 | — |
| labs.submitter_id | aliquot.labs | fk | string | 6529 | 6529 | 0 | 100.0% | 9 | 0.1% | distinct parents=9; rows/parent median=638.0, max=1674 | la***_2, la***_3, la***_1 | — |
| aliquot_amount | aliquot.aliquot_amount | num | number | 6529 | 0 | 6529 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| aliquot_collection_unit | aliquot.aliquot_collection_unit | cat | string | 6529 | 0 | 6529 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| container_type | aliquot.container_type | cat | string | 6529 | 0 | 6529 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| specimen_type | aliquot.specimen_type | cat | string | 6529 | 6529 | 0 | 100.0% | 13 | 0.2% | PBMC=1681 (25.7%); Serum=1494 (22.9%); Platelet Poor Plasma=1038 (15.9%); Urine=996 (15.3%); Lysed RBC=270 (4.1%); HCl Sodium Citrate Plasma=205 (3.1%); Platelet Rich Plasma=194 (3.0%); CPT Plasma=182 (2.8%); observed/allowed=13/17 | HCl Sodium Citrate Plasma, PBMC, Platelet Rich Plasma | ENUM_UNUSED |

### 3.2.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 3 |
| ENUM_UNUSED | 1 |
| SPARSE | 3 |
| UNIQUE | 1 |

### 3.2.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *follow_ups.submitter_id | follow_up.submitter_id | 6529 | 656 | 6529 | 0 | 100.0% | distinct parents=656; rows/parent median=5.0, max=37 |
| labs.submitter_id | lab.submitter_id | 6529 | 9 | 6529 | 0 | 100.0% | distinct parents=9; rows/parent median=638.0, max=1674 |

### 3.2.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=6529/6529 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=6529/6529 |
| aliquot_amount | aliquot_amount | empty | non-empty=0/6529 |
| aliquot_collection_unit | aliquot_collection_unit | empty | non-empty=0/6529 |
| specimen_type | specimen_type | populated | non-empty=6529/6529 |
| container_type | container_type | empty | non-empty=0/6529 |
| project_id | project_id | populated | non-empty=6529/6529 |
| labs | labs.submitter_id | populated | non-empty=6529/6529 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=6529/6529 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 13  
Physical headers: 9  
DD properties materialized: 9  
DD properties absent: 4  
Materialized but entirely empty: 3  
Physical headers not mapped to DD: 0

### 3.2.7 Machine-generated findings

- EMPTY: 3/9 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 6,529 distinct values in 6,529 non-empty rows.
- BROKEN_FK: 0/13,058 populated foreign-key rows are unmatched across detected parent mappings.

---

## audit_obs_DCC_data_release_v2-1-0.tsv

### 3.3.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | audit_obs_DCC_data_release_v2-1-0.tsv |
| DD entity | audit |
| Entity category | administrative |
| Study track | obs |
| Source class | unclassified |
| Rows | 1060 |
| Physical columns | 29 |
| DD-defined properties | 33 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.3.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 1060 |
| Distinct primary IDs | 1060 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 1060 | 100.0% |

### 3.3.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | audit.type | const | string | 1060 | 1060 | 0 | 100.0% | 1 | 0.1% | constant=audit | audit | CONST |
| project_id | audit.project_id | const | string | 1060 | 1060 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | audit.submitter_id | id | string | 1060 | 1060 | 0 | 100.0% | 1060 | 100.0% | unique 1060/1060; duplicates=0 | 11***it, 11***it, 11***it | UNIQUE |
| cases.submitter_id | audit.cases | fk | string | 1060 | 1060 | 0 | 100.0% | 1060 | 100.0% | distinct parents=1060; rows/parent median=1.0, max=1 | 11***bs, 11***bs, 11***bs | UNIQUE |
| adt0101 | audit.adt0101 | cat | string | 1060 | 1060 | 0 | 100.0% | 6 | 0.6% | 4 or more times a week=770 (72.6%); Monthly or less=90 (8.5%); 2 to 3 times a week=80 (7.5%); Never=68 (6.4%); 2 to 4 times a month=47 (4.4%); Not Done/Missing=5 (0.5%); observed/allowed=6/7 | 2 to 4 times a month, Monthly or less, 4 or more times a week | ENUM_UNUSED |
| adt0102 | audit.adt0102 | cat | string | 1060 | 1060 | 0 | 100.0% | 6 | 0.6% | 10 or more=326 (30.8%); 5 or 6=216 (20.4%); 1 or 2=170 (16.0%); 3 or 4=159 (15.0%); 7 to 9=151 (14.2%); Not Done/Missing=38 (3.6%); observed/allowed=6/7 | 1 or 2, 3 or 4, 5 or 6 | ENUM_UNUSED |
| adt0103 | audit.adt0103 | cat | string | 1060 | 1060 | 0 | 100.0% | 6 | 0.6% | Daily or almost daily=471 (44.4%); Never=219 (20.7%); Weekly=175 (16.5%); Less than monthly=94 (8.9%); Monthly=85 (8.0%); Not Done/Missing=16 (1.5%); observed/allowed=6/7 | Never, Weekly, Less than monthly | ENUM_UNUSED |
| adt0104 | audit.adt0104 | cat | string | 1060 | 984 | 76 | 92.8% | 6 | 0.6% | Daily or almost daily=361 (36.7%); Never=285 (29.0%); Weekly=143 (14.5%); Monthly=97 (9.9%); Less than monthly=87 (8.8%); Not Done/Missing=11 (1.1%); observed/allowed=6/7 | Never, Weekly, Daily or almost daily | ENUM_UNUSED |
| adt0105 | audit.adt0105 | cat | string | 1060 | 983 | 77 | 92.7% | 6 | 0.6% | Never=337 (34.3%); Daily or almost daily=184 (18.7%); Less than monthly=177 (18.0%); Weekly=166 (16.9%); Monthly=110 (11.2%); Not Done/Missing=9 (0.9%); observed/allowed=6/7 | Never, Weekly, Less than monthly | ENUM_UNUSED |
| adt0106 | audit.adt0106 | cat | string | 1060 | 983 | 77 | 92.7% | 6 | 0.6% | Never=378 (38.5%); Daily or almost daily=295 (30.0%); Weekly=132 (13.4%); Less than monthly=96 (9.8%); Monthly=73 (7.4%); Not Done/Missing=9 (0.9%); observed/allowed=6/7 | Never, Less than monthly, Daily or almost daily | ENUM_UNUSED |
| adt0107 | audit.adt0107 | cat | string | 1060 | 984 | 76 | 92.8% | 6 | 0.6% | Daily or almost daily=316 (32.1%); Never=262 (26.6%); Weekly=153 (15.5%); Less than monthly=125 (12.7%); Monthly=112 (11.4%); Not Done/Missing=16 (1.6%); observed/allowed=6/7 | Never, Weekly, Daily or almost daily | ENUM_UNUSED |
| adt0108 | audit.adt0108 | cat | string | 1060 | 984 | 76 | 92.8% | 6 | 0.6% | Never=367 (37.3%); Less than monthly=185 (18.8%); Weekly=183 (18.6%); Monthly=139 (14.1%); Daily or almost daily=97 (9.9%); Not Done/Missing=13 (1.3%); observed/allowed=6/7 | Never, Less than monthly, Monthly | ENUM_UNUSED |
| adt0109 | audit.adt0109 | cat | string | 1060 | 984 | 76 | 92.8% | 4 | 0.4% | No=726 (73.8%); Yes, during the last year=166 (16.9%); Yes, but not in the last year=86 (8.7%); Not Done/Missing=6 (0.6%); observed/allowed=4/5 | No, Yes, during the last year, Yes, but not in the last year | ENUM_UNUSED |
| adt0110 | audit.adt0110 | cat | string | 1060 | 984 | 76 | 92.8% | 4 | 0.4% | Yes, during the last year=665 (67.6%); No=224 (22.8%); Yes, but not in the last year=90 (9.1%); Not Done/Missing=5 (0.5%); observed/allowed=4/5 | No, Yes, during the last year, Yes, but not in the last year | ENUM_UNUSED |
| adtcomploth | audit.adtcomploth | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| auditnd | audit.auditnd | const | string | 1060 | 1060 | 0 | 100.0% | 1 | 0.1% | constant=Yes | Yes | CONST,ENUM_UNUSED |
| days_to_test | audit.days_to_test | dayoff | number | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_collected | audit.usaudit_collected | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_completed_by | audit.usaudit_completed_by | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q1 | audit.usaudit_q1 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q10 | audit.usaudit_q10 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q2 | audit.usaudit_q2 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q3 | audit.usaudit_q3 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q4 | audit.usaudit_q4 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q5 | audit.usaudit_q5 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q6 | audit.usaudit_q6 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q7 | audit.usaudit_q7 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q8 | audit.usaudit_q8 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q9 | audit.usaudit_q9 | cat | string | 1060 | 0 | 1060 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.3.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 14 |
| ENUM_UNUSED | 11 |
| SPARSE | 14 |
| UNIQUE | 2 |

### 3.3.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| cases.submitter_id | case.submitter_id | 1060 | 1060 | 1060 | 0 | 100.0% | distinct parents=1060; rows/parent median=1.0, max=1 |

### 3.3.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=1060/1060 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=1060/1060 |
| days_to_test | days_to_test | empty | non-empty=0/1060 |
| usaudit_collected | usaudit_collected | empty | non-empty=0/1060 |
| usaudit_completed_by | usaudit_completed_by | empty | non-empty=0/1060 |
| usaudit_q1 | usaudit_q1 | empty | non-empty=0/1060 |
| usaudit_q2 | usaudit_q2 | empty | non-empty=0/1060 |
| usaudit_q3 | usaudit_q3 | empty | non-empty=0/1060 |
| usaudit_q4 | usaudit_q4 | empty | non-empty=0/1060 |
| usaudit_q5 | usaudit_q5 | empty | non-empty=0/1060 |
| usaudit_q6 | usaudit_q6 | empty | non-empty=0/1060 |
| usaudit_q7 | usaudit_q7 | empty | non-empty=0/1060 |
| usaudit_q8 | usaudit_q8 | empty | non-empty=0/1060 |
| usaudit_q9 | usaudit_q9 | empty | non-empty=0/1060 |
| usaudit_q10 | usaudit_q10 | empty | non-empty=0/1060 |
| auditnd | auditnd | populated | non-empty=1060/1060 |
| adtcomploth | adtcomploth | empty | non-empty=0/1060 |
| adt0101 | adt0101 | populated | non-empty=1060/1060 |
| adt0102 | adt0102 | populated | non-empty=1060/1060 |
| adt0103 | adt0103 | populated | non-empty=1060/1060 |
| adt0104 | adt0104 | populated | non-empty=984/1060 |
| adt0105 | adt0105 | populated | non-empty=983/1060 |
| adt0106 | adt0106 | populated | non-empty=983/1060 |
| adt0107 | adt0107 | populated | non-empty=984/1060 |
| adt0108 | adt0108 | populated | non-empty=984/1060 |
| adt0109 | adt0109 | populated | non-empty=984/1060 |
| adt0110 | adt0110 | populated | non-empty=984/1060 |
| cases | cases.submitter_id | populated | non-empty=1060/1060 |
| project_id | project_id | populated | non-empty=1060/1060 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 33  
Physical headers: 29  
DD properties materialized: 29  
DD properties absent: 4  
Materialized but entirely empty: 14  
Physical headers not mapped to DD: 0

### 3.3.7 Machine-generated findings

- EMPTY: 14/29 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 1,060 distinct values in 1,060 non-empty rows.
- BROKEN_FK: 0/1,060 populated foreign-key rows are unmatched across detected parent mappings.

---

## audit_rct_DCC_data_release_v2-1-0.tsv

### 3.4.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | audit_rct_DCC_data_release_v2-1-0.tsv |
| DD entity | audit |
| Entity category | administrative |
| Study track | rct |
| Source class | unclassified |
| Rows | 134 |
| Physical columns | 29 |
| DD-defined properties | 33 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.4.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 134 |
| Distinct primary IDs | 134 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 134 | 100.0% |

### 3.4.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | audit.type | const | string | 134 | 134 | 0 | 100.0% | 1 | 0.7% | constant=audit | audit | CONST |
| project_id | audit.project_id | const | string | 134 | 134 | 0 | 100.0% | 1 | 0.7% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | audit.submitter_id | id | string | 134 | 134 | 0 | 100.0% | 134 | 100.0% | unique 134/134; duplicates=0 | 11***it, 11***it, 11***it | UNIQUE |
| cases.submitter_id | audit.cases | fk | string | 134 | 134 | 0 | 100.0% | 134 | 100.0% | distinct parents=134; rows/parent median=1.0, max=1 | 11***al, 11***al, 11***al | UNIQUE |
| adt0101 | audit.adt0101 | cat | string | 134 | 134 | 0 | 100.0% | 5 | 3.7% | 4 or more times a week=120 (89.6%); 2 to 3 times a week=6 (4.5%); 2 to 4 times a month=6 (4.5%); Monthly or less=1 (0.7%); Never=1 (0.7%); observed/allowed=5/7 | 4 or more times a week, 2 to 3 times a week, 2 to 4 times a month | ENUM_UNUSED |
| adt0102 | audit.adt0102 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | 10 or more=46 (34.3%); 7 to 9=30 (22.4%); 5 or 6=26 (19.4%); 3 or 4=20 (14.9%); 1 or 2=10 (7.5%); Not Done/Missing=2 (1.5%); observed/allowed=6/7 | 7 to 9, 3 or 4, 10 or more | ENUM_UNUSED |
| adt0103 | audit.adt0103 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | Daily or almost daily=84 (62.7%); Never=17 (12.7%); Less than monthly=12 (9.0%); Weekly=11 (8.2%); Monthly=9 (6.7%); Not Done/Missing=1 (0.7%); observed/allowed=6/7 | Weekly, Never, Daily or almost daily | ENUM_UNUSED |
| adt0104 | audit.adt0104 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | Daily or almost daily=52 (38.8%); Never=41 (30.6%); Weekly=17 (12.7%); Less than monthly=12 (9.0%); Monthly=10 (7.5%); Not Done/Missing=2 (1.5%); observed/allowed=6/7 | Less than monthly, Daily or almost daily, Never | ENUM_UNUSED |
| adt0105 | audit.adt0105 | cat | string | 134 | 134 | 0 | 100.0% | 5 | 3.7% | Never=46 (34.3%); Weekly=26 (19.4%); Monthly=23 (17.2%); Daily or almost daily=21 (15.7%); Less than monthly=18 (13.4%); observed/allowed=5/7 | Less than monthly, Daily or almost daily, Monthly | ENUM_UNUSED |
| adt0106 | audit.adt0106 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | Never=42 (31.3%); Daily or almost daily=40 (29.9%); Weekly=26 (19.4%); Less than monthly=13 (9.7%); Monthly=12 (9.0%); Not Done/Missing=1 (0.7%); observed/allowed=6/7 | Less than monthly, Never, Daily or almost daily | ENUM_UNUSED |
| adt0107 | audit.adt0107 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | Daily or almost daily=49 (36.6%); Never=27 (20.1%); Less than monthly=20 (14.9%); Monthly=19 (14.2%); Weekly=18 (13.4%); Not Done/Missing=1 (0.7%); observed/allowed=6/7 | Weekly, Monthly, Daily or almost daily | ENUM_UNUSED |
| adt0108 | audit.adt0108 | cat | string | 134 | 134 | 0 | 100.0% | 6 | 4.5% | Never=50 (37.3%); Less than monthly=28 (20.9%); Weekly=23 (17.2%); Monthly=23 (17.2%); Daily or almost daily=9 (6.7%); Not Done/Missing=1 (0.7%); observed/allowed=6/7 | Daily or almost daily, Less than monthly, Monthly | ENUM_UNUSED |
| adt0109 | audit.adt0109 | cat | string | 134 | 134 | 0 | 100.0% | 3 | 2.2% | No=103 (76.9%); Yes, during the last year=18 (13.4%); Yes, but not in the last year=13 (9.7%); observed/allowed=3/5 | No, Yes, but not in the last year, Yes, during the last year | ENUM_UNUSED |
| adt0110 | audit.adt0110 | cat | string | 134 | 134 | 0 | 100.0% | 4 | 3.0% | Yes, during the last year=112 (83.6%); No=15 (11.2%); Yes, but not in the last year=6 (4.5%); Not Done/Missing=1 (0.7%); observed/allowed=4/5 | Yes, during the last year, Yes, but not in the last year, No | ENUM_UNUSED |
| adtcomploth | audit.adtcomploth | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| auditnd | audit.auditnd | const | string | 134 | 134 | 0 | 100.0% | 1 | 0.7% | constant=Yes | Yes | CONST,ENUM_UNUSED |
| days_to_test | audit.days_to_test | dayoff | number | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_collected | audit.usaudit_collected | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_completed_by | audit.usaudit_completed_by | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q1 | audit.usaudit_q1 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q10 | audit.usaudit_q10 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q2 | audit.usaudit_q2 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q3 | audit.usaudit_q3 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q4 | audit.usaudit_q4 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q5 | audit.usaudit_q5 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q6 | audit.usaudit_q6 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q7 | audit.usaudit_q7 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q8 | audit.usaudit_q8 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| usaudit_q9 | audit.usaudit_q9 | cat | string | 134 | 0 | 134 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.4.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 14 |
| ENUM_UNUSED | 11 |
| SPARSE | 14 |
| UNIQUE | 2 |

### 3.4.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| cases.submitter_id | case.submitter_id | 134 | 134 | 134 | 0 | 100.0% | distinct parents=134; rows/parent median=1.0, max=1 |

### 3.4.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=134/134 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=134/134 |
| days_to_test | days_to_test | empty | non-empty=0/134 |
| usaudit_collected | usaudit_collected | empty | non-empty=0/134 |
| usaudit_completed_by | usaudit_completed_by | empty | non-empty=0/134 |
| usaudit_q1 | usaudit_q1 | empty | non-empty=0/134 |
| usaudit_q2 | usaudit_q2 | empty | non-empty=0/134 |
| usaudit_q3 | usaudit_q3 | empty | non-empty=0/134 |
| usaudit_q4 | usaudit_q4 | empty | non-empty=0/134 |
| usaudit_q5 | usaudit_q5 | empty | non-empty=0/134 |
| usaudit_q6 | usaudit_q6 | empty | non-empty=0/134 |
| usaudit_q7 | usaudit_q7 | empty | non-empty=0/134 |
| usaudit_q8 | usaudit_q8 | empty | non-empty=0/134 |
| usaudit_q9 | usaudit_q9 | empty | non-empty=0/134 |
| usaudit_q10 | usaudit_q10 | empty | non-empty=0/134 |
| auditnd | auditnd | populated | non-empty=134/134 |
| adtcomploth | adtcomploth | empty | non-empty=0/134 |
| adt0101 | adt0101 | populated | non-empty=134/134 |
| adt0102 | adt0102 | populated | non-empty=134/134 |
| adt0103 | adt0103 | populated | non-empty=134/134 |
| adt0104 | adt0104 | populated | non-empty=134/134 |
| adt0105 | adt0105 | populated | non-empty=134/134 |
| adt0106 | adt0106 | populated | non-empty=134/134 |
| adt0107 | adt0107 | populated | non-empty=134/134 |
| adt0108 | adt0108 | populated | non-empty=134/134 |
| adt0109 | adt0109 | populated | non-empty=134/134 |
| adt0110 | adt0110 | populated | non-empty=134/134 |
| cases | cases.submitter_id | populated | non-empty=134/134 |
| project_id | project_id | populated | non-empty=134/134 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 33  
Physical headers: 29  
DD properties materialized: 29  
DD properties absent: 4  
Materialized but entirely empty: 14  
Physical headers not mapped to DD: 0

### 3.4.7 Machine-generated findings

- EMPTY: 14/29 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 134 distinct values in 134 non-empty rows.
- BROKEN_FK: 0/134 populated foreign-key rows are unmatched across detected parent mappings.

---

## bbt-molecular-merged_valid_followupsdel1_v2-1-0.tsv

### 3.5.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | bbt-molecular-merged_valid_followupsdel1_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 1748 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.5.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 1748 |
| Distinct primary IDs | 1748 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.5.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 1748 | 1748 | 0 | 100.0% | 1 | 0.1% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 1748 | 1748 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 1748 | 1748 | 0 | 100.0% | 1748 | 100.0% | unique 1748/1748; duplicates=0 | 11***CE, 11***CE, 11***CE | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 1748 | 1748 | 0 | 100.0% | 628 | 35.9% | distinct parents=628; rows/parent median=2.0, max=5 | 11***07, 11***07, 11***07 | — |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 1748 | 1748 | 0 | 100.0% | 463 | 26.5% | distinct parents=463; rows/parent median=5.0, max=8 | 11***_0, 11***28, 11***_0 | — |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | cat | string | 1748 | 1748 | 0 | 100.0% | 8 | 0.5% | Urine KIM-1=232 (13.3%); Urine Creatinine=232 (13.3%); Urine L-FABP=232 (13.3%); Urine IL-18=232 (13.3%); Urine NGAL=232 (13.3%); ORM1=204 (11.7%); ACE=192 (11.0%); Renin=192 (11.0%); observed/allowed=8/95 | ACE, ORM1, Urine Creatinine | ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 1748 | 0 | 1748 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | cat | string | 1748 | 1748 | 0 | 100.0% | 5 | 0.3% | ng/mL=656 (37.5%); pg/mL=464 (26.5%); mg/dL=232 (13.3%); µg/ml=204 (11.7%); µg/l=192 (11.0%) | µg/l, µg/ml, mg/dL | — |
| test_value | molecular_test.test_value | num | string | 1748 | 1717 | 31 | 98.2% | 1685 | 98.1% | min=0; p25=11.4498; median=93.6092; mean=2472.04; p75=377.848; max=338210 | 119.6379630058864, 90.3579602047552, 127.0522079030392 | — |

### 3.5.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 1 |

### 3.5.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 1748 | 628 | 1748 | 0 | 100.0% | distinct parents=628; rows/parent median=2.0, max=5 |
| *follow_ups.submitter_id | follow_up.submitter_id | 1748 | 463 | 1748 | 0 | 100.0% | distinct parents=463; rows/parent median=5.0, max=8 |

### 3.5.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=1748/1748 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=1748/1748 |
| gene_symbol | gene_symbol | empty | non-empty=0/1748 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/1748 |
| test_result | test_result | empty | non-empty=0/1748 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/1748 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/1748 |
| days_to_test | days_to_test | empty | non-empty=0/1748 |
| laboratory_test | laboratory_test | populated | non-empty=1748/1748 |
| test_value | test_value | populated | non-empty=1717/1748 |
| test_unit | test_unit | populated | non-empty=1748/1748 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=1748/1748 |
| aliquots | aliquots.submitter_id | populated | non-empty=1748/1748 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=1748/1748 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.5.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 1,748 distinct values in 1,748 non-empty rows.
- BROKEN_FK: 0/3,496 populated foreign-key rows are unmatched across detected parent mappings.

---

## demographic_obs_DCC_data_release_v2-1-0.tsv

### 3.6.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | demographic_obs_DCC_data_release_v2-1-0.tsv |
| DD entity | demographic |
| Entity category | clinical |
| Study track | obs |
| Source class | unclassified |
| Rows | 1133 |
| Physical columns | 19 |
| DD-defined properties | 23 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | *cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.6.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 1133 |
| Distinct primary IDs | 1133 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 1133 | 100.0% |

### 3.6.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | demographic.type | const | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | constant=demographic | demographic | CONST |
| project_id | demographic.project_id | const | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | demographic.submitter_id | id | string | 1133 | 1133 | 0 | 100.0% | 1133 | 100.0% | unique 1133/1133; duplicates=0 | 11***ic, 11***ic, 11***ic | UNIQUE |
| *cases.submitter_id | demographic.cases | fk | string | 1133 | 1133 | 0 | 100.0% | 1133 | 100.0% | distinct parents=1133; rows/parent median=1.0, max=1 | 11***bs, 11***bs, 11***bs | UNIQUE |
| age_at_index | demographic.age_at_index | num | number | 1133 | 1133 | 0 | 100.0% | 425 | 37.5% | min=21.2; p25=35.4; median=44.2; mean=44.6973; p75=53.6; max=82 | 57.2, 60.8, 35.9 | — |
| cause_of_death_primary | demographic.cause_of_death_primary | text | string | 1133 | 204 | 929 | 18.0% | 179 | 87.7% | length min=3; mean=44.7; max=408; blank-string=0 | Septic Shock, Septic shock due to Klebsiella, Septic shock | SPARSE |
| cause_of_death_secondary | demographic.cause_of_death_secondary | text | string | 1133 | 105 | 1028 | 9.3% | 103 | 98.1% | length min=3; mean=83.7; max=1530; blank-string=0 | Acute kidney injury Lactic aci, 1) Acute kidney injury 2) Drug, Altered mental status Acute hy | SPARSE |
| cur_employ_stat | demographic.cur_employ_stat | cat | string | 1133 | 1132 | 1 | 99.9% | 3 | 0.3% | No=598 (52.8%); Yes=486 (42.9%); Missing=48 (4.2%); observed/allowed=3/4 | No, Yes, Missing | ENUM_UNUSED |
| days_to_death | demographic.days_to_death | dayoff | number | 1133 | 240 | 893 | 21.2% | 143 | 59.6% | min=2; max=1170; negative=0; zero=0; common=9:6, 16:6, 14:6, 20:5, 6:5, 36:5, 25:5, 22:5 | 101, 426, 6 | — |
| death_related_to | demographic.death_related_to | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| education | demographic.education | cat | string | 1133 | 1133 | 0 | 100.0% | 7 | 0.6% | Trade School/Some College=310 (27.4%); Completed High School=278 (24.5%); Standard College/University=259 (22.9%); Completed Graduate/Professional Program=135 (11.9%); Year 10=72 (6.4%); Missing=58 (5.1%); Elementary=21 (1.9%) | Trade School/Some College, Standard College/University, Completed High School | — |
| ethnicity | demographic.ethnicity | cat | string | 1133 | 1111 | 22 | 98.1% | 2 | 0.2% | not hispanic or latino=1025 (92.3%); hispanic or latino=86 (7.7%); observed/allowed=2/6 | not hispanic or latino, hispanic or latino | ENUM_UNUSED |
| gender | demographic.gender | cat | string | 1133 | 1132 | 1 | 99.9% | 2 | 0.2% | male=632 (55.8%); female=500 (44.2%); observed/allowed=2/6 | male, female | ENUM_UNUSED |
| marital | demographic.marital | cat | string | 1133 | 1133 | 0 | 100.0% | 7 | 0.6% | Single, never married=422 (37.2%); Married=347 (30.6%); Divorced=212 (18.7%); Living with significant other (common law marriage)=66 (5.8%); Separated=45 (4.0%); Missing=25 (2.2%); Widowed=16 (1.4%); observed/allowed=7/9 | Married, Single, never married, Living with significant other  | ENUM_UNUSED |
| race | demographic.race | cat | string | 1133 | 1102 | 31 | 97.3% | 6 | 0.5% | white=885 (80.3%); black or african american=164 (14.9%); asian=31 (2.8%); american indian or alaska native=10 (0.9%); More than one race=9 (0.8%); native hawaiian or other pacific islander=3 (0.3%); observed/allowed=6/11 | white, native hawaiian or other pacif, asian | ENUM_UNUSED |
| sex | demographic.sex | cat | string | 1133 | 1133 | 0 | 100.0% | 2 | 0.2% | male=631 (55.7%); female=502 (44.3%); observed/allowed=2/4 | male, female | ENUM_UNUSED |
| vital_status | demographic.vital_status | cat | string | 1133 | 1133 | 0 | 100.0% | 2 | 0.2% | Alive=892 (78.7%); Dead=241 (21.3%); observed/allowed=2/5 | Alive, Dead | ENUM_UNUSED |
| year_of_birth | demographic.year_of_birth | num | number | 1133 | 1133 | 0 | 100.0% | 58 | 5.1% | min=1940; p25=1968; median=1977; mean=1976.64; p75=1987; max=2001 | 1962, 1958, 1983 | — |
| year_of_death | demographic.year_of_death | num | number | 1133 | 240 | 893 | 21.2% | 6 | 2.5% | min=2019; p25=2021; median=2022; mean=2021.55; p75=2023; max=2024 | 2019, 2020, 2022 | — |

### 3.6.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 1 |
| ENUM_UNUSED | 7 |
| SPARSE | 3 |
| UNIQUE | 2 |

### 3.6.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *cases.submitter_id | case.submitter_id | 1133 | 1133 | 1133 | 0 | 100.0% | distinct parents=1133; rows/parent median=1.0, max=1 |

### 3.6.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=1133/1133 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=1133/1133 |
| ethnicity | ethnicity | populated | non-empty=1111/1133 |
| sex | sex | populated | non-empty=1133/1133 |
| gender | gender | populated | non-empty=1132/1133 |
| race | race | populated | non-empty=1102/1133 |
| education | education | populated | non-empty=1133/1133 |
| marital | marital | populated | non-empty=1133/1133 |
| cur_employ_stat | cur_employ_stat | populated | non-empty=1132/1133 |
| vital_status | vital_status | populated | non-empty=1133/1133 |
| age_at_index | age_at_index | populated | non-empty=1133/1133 |
| year_of_birth | year_of_birth | populated | non-empty=1133/1133 |
| days_to_death | days_to_death | populated | non-empty=240/1133 |
| year_of_death | year_of_death | populated | non-empty=240/1133 |
| cause_of_death_primary | cause_of_death_primary | populated | non-empty=204/1133 |
| cause_of_death_secondary | cause_of_death_secondary | populated | non-empty=105/1133 |
| death_related_to | death_related_to | empty | non-empty=0/1133 |
| cases | *cases.submitter_id | populated | non-empty=1133/1133 |
| project_id | project_id | populated | non-empty=1133/1133 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 23  
Physical headers: 19  
DD properties materialized: 19  
DD properties absent: 4  
Materialized but entirely empty: 1  
Physical headers not mapped to DD: 0

### 3.6.7 Machine-generated findings

- EMPTY: 1/19 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 1,133 distinct values in 1,133 non-empty rows.
- BROKEN_FK: 0/1,133 populated foreign-key rows are unmatched across detected parent mappings.

---

## demographic_rct_DCC_data_release_v2-1-0.tsv

### 3.7.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | demographic_rct_DCC_data_release_v2-1-0.tsv |
| DD entity | demographic |
| Entity category | clinical |
| Study track | rct |
| Source class | unclassified |
| Rows | 147 |
| Physical columns | 19 |
| DD-defined properties | 23 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | *cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.7.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 147 |
| Distinct primary IDs | 147 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 147 | 100.0% |

### 3.7.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | demographic.type | const | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | constant=demographic | demographic | CONST |
| project_id | demographic.project_id | const | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | demographic.submitter_id | id | string | 147 | 147 | 0 | 100.0% | 147 | 100.0% | unique 147/147; duplicates=0 | 11***ic, 11***ic, 11***ic | UNIQUE |
| *cases.submitter_id | demographic.cases | fk | string | 147 | 147 | 0 | 100.0% | 147 | 100.0% | distinct parents=147; rows/parent median=1.0, max=1 | 11***al, 11***al, 11***al | UNIQUE |
| age_at_index | demographic.age_at_index | num | number | 147 | 147 | 0 | 100.0% | 120 | 81.6% | min=26.5; p25=37.4; median=44; mean=44.6878; p75=51.95; max=68.8 | 35.1, 29.1, 26.5 | — |
| cause_of_death_primary | demographic.cause_of_death_primary | text | string | 147 | 33 | 114 | 22.4% | 32 | 97.0% | length min=5; mean=62.9; max=283; blank-string=0 | Decompensated liver disease, Anoxic brain injury secondary , Cardiac arrest in setting of d | — |
| cause_of_death_secondary | demographic.cause_of_death_secondary | text | string | 147 | 15 | 132 | 10.2% | 15 | 100.0% | length min=6; mean=85.0; max=252; blank-string=0 | Acute respiratory failure Aspi, Pulseless electrical activity, Acute respiratory failure Rena | SPARSE,UNIQUE |
| cur_employ_stat | demographic.cur_employ_stat | cat | string | 147 | 147 | 0 | 100.0% | 3 | 2.0% | No=86 (58.5%); Yes=55 (37.4%); Missing=6 (4.1%); observed/allowed=3/4 | Yes, No, Missing | ENUM_UNUSED |
| days_to_death | demographic.days_to_death | dayoff | number | 147 | 36 | 111 | 24.5% | 32 | 88.9% | min=7; max=482; negative=0; zero=0; common=62:2, 53:2, 9:2, 28:2, 17:1, 20:1, 197:1, 48:1 | 48, 62, 17 | — |
| death_related_to | demographic.death_related_to | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| education | demographic.education | cat | string | 147 | 147 | 0 | 100.0% | 7 | 4.8% | Completed High School=47 (32.0%); Trade School/Some College=45 (30.6%); Standard College/University=23 (15.6%); Completed Graduate/Professional Program=11 (7.5%); Missing=11 (7.5%); Year 10=7 (4.8%); Elementary=3 (2.0%) | Completed High School, Trade School/Some College, Standard College/University | — |
| ethnicity | demographic.ethnicity | cat | string | 147 | 145 | 2 | 98.6% | 2 | 1.4% | not hispanic or latino=126 (86.9%); hispanic or latino=19 (13.1%); observed/allowed=2/6 | not hispanic or latino, hispanic or latino | ENUM_UNUSED |
| gender | demographic.gender | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | male=88 (59.9%); female=59 (40.1%); observed/allowed=2/6 | male, female | ENUM_UNUSED |
| marital | demographic.marital | cat | string | 147 | 147 | 0 | 100.0% | 7 | 4.8% | Married=58 (39.5%); Divorced=37 (25.2%); Single, never married=36 (24.5%); Living with significant other (common law marriage)=8 (5.4%); Separated=5 (3.4%); Widowed=2 (1.4%); Missing=1 (0.7%); observed/allowed=7/9 | Divorced, Single, never married, Married | ENUM_UNUSED |
| race | demographic.race | cat | string | 147 | 144 | 3 | 98.0% | 5 | 3.5% | white=121 (84.0%); black or african american=17 (11.8%); More than one race=2 (1.4%); american indian or alaska native=2 (1.4%); asian=2 (1.4%); observed/allowed=5/11 | white, black or african american, More than one race | ENUM_UNUSED |
| sex | demographic.sex | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | male=88 (59.9%); female=59 (40.1%); observed/allowed=2/4 | male, female | ENUM_UNUSED |
| vital_status | demographic.vital_status | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | Alive=111 (75.5%); Dead=36 (24.5%); observed/allowed=2/5 | Alive, Dead | ENUM_UNUSED |
| year_of_birth | demographic.year_of_birth | num | number | 147 | 147 | 0 | 100.0% | 42 | 28.6% | min=1951; p25=1969; median=1977; mean=1976.14; p75=1983; max=1994 | 1985, 1991, 1994 | — |
| year_of_death | demographic.year_of_death | num | number | 147 | 36 | 111 | 24.5% | 3 | 8.3% | min=2020; p25=2021; median=2021; mean=2021.08; p75=2021; max=2022 | 2021, 2022, 2020 | — |

### 3.7.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 1 |
| ENUM_UNUSED | 7 |
| SPARSE | 2 |
| UNIQUE | 3 |

### 3.7.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *cases.submitter_id | case.submitter_id | 147 | 147 | 147 | 0 | 100.0% | distinct parents=147; rows/parent median=1.0, max=1 |

### 3.7.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=147/147 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=147/147 |
| ethnicity | ethnicity | populated | non-empty=145/147 |
| sex | sex | populated | non-empty=147/147 |
| gender | gender | populated | non-empty=147/147 |
| race | race | populated | non-empty=144/147 |
| education | education | populated | non-empty=147/147 |
| marital | marital | populated | non-empty=147/147 |
| cur_employ_stat | cur_employ_stat | populated | non-empty=147/147 |
| vital_status | vital_status | populated | non-empty=147/147 |
| age_at_index | age_at_index | populated | non-empty=147/147 |
| year_of_birth | year_of_birth | populated | non-empty=147/147 |
| days_to_death | days_to_death | populated | non-empty=36/147 |
| year_of_death | year_of_death | populated | non-empty=36/147 |
| cause_of_death_primary | cause_of_death_primary | populated | non-empty=33/147 |
| cause_of_death_secondary | cause_of_death_secondary | populated | non-empty=15/147 |
| death_related_to | death_related_to | empty | non-empty=0/147 |
| cases | *cases.submitter_id | populated | non-empty=147/147 |
| project_id | project_id | populated | non-empty=147/147 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 23  
Physical headers: 19  
DD properties materialized: 19  
DD properties absent: 4  
Materialized but entirely empty: 1  
Physical headers not mapped to DD: 0

### 3.7.7 Machine-generated findings

- EMPTY: 1/19 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 147 distinct values in 147 non-empty rows.
- BROKEN_FK: 0/147 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_aliquot-inventory_DCC_data_release_v2-1-0_updated_labs_250815.tsv

### 3.8.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_aliquot-inventory_DCC_data_release_v2-1-0_updated_labs_250815.tsv |
| DD entity | aliquot |
| Entity category | biospecimen |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 50254 |
| Physical columns | 9 |
| DD-defined properties | 13 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.8.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 50254 |
| Distinct primary IDs | 50254 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.8.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | aliquot.type | const | string | 50254 | 50254 | 0 | 100.0% | 1 | 0.0% | constant=aliquot | aliquot | CONST |
| project_id | aliquot.project_id | const | string | 50254 | 50254 | 0 | 100.0% | 1 | 0.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | aliquot.submitter_id | id | string | 50254 | 50254 | 0 | 100.0% | 50254 | 100.0% | unique 50254/50254; duplicates=0 | 11***01, 11***02, 11***03 | UNIQUE |
| *follow_ups.submitter_id | aliquot.follow_ups | fk | string | 50254 | 50254 | 0 | 100.0% | 2320 | 4.6% | distinct parents=2320; rows/parent median=21.0, max=52 | 11***_0, 11***80, 11***28 | — |
| labs.submitter_id | aliquot.labs | fk | string | 50254 | 50143 | 111 | 99.8% | 1 | 0.0% | distinct parents=1; rows/parent median=50143.0, max=50143 | la***_0 | CONST |
| aliquot_amount | aliquot.aliquot_amount | num | number | 50254 | 0 | 50254 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| aliquot_collection_unit | aliquot.aliquot_collection_unit | cat | string | 50254 | 0 | 50254 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| container_type | aliquot.container_type | cat | string | 50254 | 0 | 50254 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| specimen_type | aliquot.specimen_type | cat | string | 50254 | 50197 | 57 | 99.9% | 14 | 0.0% | CPT Plasma=12649 (25.2%); Platelet Poor Plasma=10135 (20.2%); PBMC=9139 (18.2%); Urine=5283 (10.5%); Serum=4755 (9.5%); Lysed RBC=3296 (6.6%); Platelet Rich Plasma=2991 (6.0%); Whole Blood (DNA)=910 (1.8%); observed/allowed=14/17 | Urine, CPT Plasma, NEAT Plasma | ENUM_UNUSED |

### 3.8.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 3 |
| ENUM_UNUSED | 1 |
| SPARSE | 3 |
| UNIQUE | 1 |

### 3.8.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *follow_ups.submitter_id | follow_up.submitter_id | 50254 | 2320 | 50254 | 0 | 100.0% | distinct parents=2320; rows/parent median=21.0, max=52 |
| labs.submitter_id | lab.submitter_id | 50143 | 1 | 50143 | 0 | 100.0% | distinct parents=1; rows/parent median=50143.0, max=50143 |

### 3.8.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=50254/50254 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=50254/50254 |
| aliquot_amount | aliquot_amount | empty | non-empty=0/50254 |
| aliquot_collection_unit | aliquot_collection_unit | empty | non-empty=0/50254 |
| specimen_type | specimen_type | populated | non-empty=50197/50254 |
| container_type | container_type | empty | non-empty=0/50254 |
| project_id | project_id | populated | non-empty=50254/50254 |
| labs | labs.submitter_id | populated | non-empty=50143/50254 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=50254/50254 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 13  
Physical headers: 9  
DD properties materialized: 9  
DD properties absent: 4  
Materialized but entirely empty: 3  
Physical headers not mapped to DD: 0

### 3.8.7 Machine-generated findings

- EMPTY: 3/9 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 50,254 distinct values in 50,254 non-empty rows.
- BROKEN_FK: 0/100,397 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_case_obs_DCC_data_release_v2-1-0_250815_minor.tsv

### 3.9.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_case_obs_DCC_data_release_v2-1-0_250815_minor.tsv |
| DD entity | case |
| Entity category | administrative |
| Study track | obs |
| Source class | unclassified |
| Rows | 1133 |
| Physical columns | 23 |
| DD-defined properties | 27 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.9.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 1133 |
| Distinct primary IDs | 1133 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.9.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | case.type | const | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | constant=case | case | CONST |
| project_id | case.project_id | const | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | case.submitter_id | id | string | 1133 | 1133 | 0 | 100.0% | 1133 | 100.0% | unique 1133/1133; duplicates=0 | 11***bs, 11***bs, 11***bs | UNIQUE |
| *studies.submitter_id | case.studies | fk | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | distinct parents=1; rows/parent median=1133.0, max=1133 | *** | CONST |
| actarm | case.actarm | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ah_hosp | case.ah_hosp | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ah_hosp_num | case.ah_hosp_num | num | number | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| aki_status | case.aki_status | cat | string | 1133 | 546 | 587 | 48.2% | 2 | 0.4% | Yes=295 (54.0%); No=251 (46.0%); observed/allowed=2/3 | No, Yes | ENUM_UNUSED |
| bari_surgery | case.bari_surgery | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| cohort | case.cohort | cat | string | 1133 | 1133 | 0 | 100.0% | 3 | 0.3% | Heavy Drinker with Alcoholic Hepatits=717 (63.3%); Heavy Drinker without Alcoholic Hepatits=257 (22.7%); Healthy Donor=159 (14.0%); observed/allowed=3/3 | Healthy Donor, Heavy Drinker with Alcoholic H, Heavy Drinker without Alcoholi | — |
| consent_type | case.consent_type | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_180_aki | case.days_180_aki | cat | string | 1133 | 403 | 730 | 35.6% | 2 | 0.5% | Yes=287 (71.2%); No=116 (28.8%); observed/allowed=2/3 | No, Yes | ENUM_UNUSED |
| days_180_survival | case.days_180_survival | cat | string | 1133 | 649 | 484 | 57.3% | 2 | 0.3% | alive=463 (71.3%); dead=186 (28.7%); observed/allowed=2/3 | alive, dead | ENUM_UNUSED |
| days_90_aki | case.days_90_aki | cat | string | 1133 | 470 | 663 | 41.5% | 2 | 0.4% | Yes=260 (55.3%); No=210 (44.7%); observed/allowed=2/3 | No, Yes | ENUM_UNUSED |
| days_90_survival | case.days_90_survival | cat | string | 1133 | 852 | 281 | 75.2% | 2 | 0.2% | alive=697 (81.8%); dead=155 (18.2%); observed/allowed=2/3 | alive, dead | ENUM_UNUSED |
| days_to_aki | case.days_to_aki | dayoff | number | 1133 | 1133 | 0 | 100.0% | 267 | 23.6% | min=-23; max=1827; negative=95; zero=190; common=0:190, 252:92, 1:33, -2:18, 253:16, 2:15, 168:13, 182:12 | 0.0, 1827.0, -7.0 | NEG |
| days_to_consent | case.days_to_consent | dayoff | number | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_death | case.days_to_death | dayoff | number | 1133 | 1133 | 0 | 100.0% | 289 | 25.5% | min=0; max=1170; negative=0; zero=134; common=0:134, 252:105, 1:25, 253:17, 168:15, 7:12, 182:12, 9:11 | 0.0, 248.0, 100.0 | — |
| index_date | case.index_date | const | string | 1133 | 1133 | 0 | 100.0% | 1 | 0.1% | constant=Study Enrollment | Study Enrollment | CONST,ENUM_UNUSED |
| inf_cnst_sign_dt | case.inf_cnst_sign_dt | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| rct_meld_strata | case.rct_meld_strata | cat | string | 1133 | 0 | 1133 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| study_site | case.study_site | cat | string | 1133 | 1133 | 0 | 100.0% | 10 | 0.9% | Cleveland Clinic=216 (19.1%); Virginia Commonwealth University=189 (16.7%); Mayo Clinic=152 (13.4%); Indiana University=120 (10.6%); University of Louisville=119 (10.5%); University of Pittsburgh=105 (9.3%); BIDMC=90 (7.9%); UT Southwestern=62 (5.5%); observed/allowed=10/16 | Cleveland Clinic, Indiana University, University of Louisville | ENUM_UNUSED |
| vital_status | case.vital_status | cat | string | 1133 | 1133 | 0 | 100.0% | 2 | 0.2% | alive=892 (78.7%); dead=241 (21.3%); observed/allowed=2/3 | alive, dead | ENUM_UNUSED |

### 3.9.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 8 |
| ENUM_UNUSED | 8 |
| NEG | 1 |
| SPARSE | 8 |
| UNIQUE | 1 |

### 3.9.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *studies.submitter_id | study.submitter_id | 1133 | 1 | 1133 | 0 | 100.0% | distinct parents=1; rows/parent median=1133.0, max=1133 |

### 3.9.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=1133/1133 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=1133/1133 |
| consent_type | consent_type | empty | non-empty=0/1133 |
| inf_cnst_sign_dt | inf_cnst_sign_dt | empty | non-empty=0/1133 |
| days_to_consent | days_to_consent | empty | non-empty=0/1133 |
| index_date | index_date | populated | non-empty=1133/1133 |
| actarm | actarm | empty | non-empty=0/1133 |
| cohort | cohort | populated | non-empty=1133/1133 |
| study_site | study_site | populated | non-empty=1133/1133 |
| bari_surgery | bari_surgery | empty | non-empty=0/1133 |
| ah_hosp | ah_hosp | empty | non-empty=0/1133 |
| ah_hosp_num | ah_hosp_num | empty | non-empty=0/1133 |
| rct_meld_strata | rct_meld_strata | empty | non-empty=0/1133 |
| vital_status | vital_status | populated | non-empty=1133/1133 |
| days_to_death | days_to_death | populated | non-empty=1133/1133 |
| aki_status | aki_status | populated | non-empty=546/1133 |
| days_to_aki | days_to_aki | populated | non-empty=1133/1133 |
| days_90_survival | days_90_survival | populated | non-empty=852/1133 |
| days_180_survival | days_180_survival | populated | non-empty=649/1133 |
| days_90_aki | days_90_aki | populated | non-empty=470/1133 |
| days_180_aki | days_180_aki | populated | non-empty=403/1133 |
| studies | *studies.submitter_id | populated | non-empty=1133/1133 |
| project_id | project_id | populated | non-empty=1133/1133 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 27  
Physical headers: 23  
DD properties materialized: 23  
DD properties absent: 4  
Materialized but entirely empty: 8  
Physical headers not mapped to DD: 0

### 3.9.7 Machine-generated findings

- EMPTY: 8/23 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 1,133 distinct values in 1,133 non-empty rows.
- BROKEN_FK: 0/1,133 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_case_rct_DCC_data_release_v2-1-0_250815_minor.tsv

### 3.10.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_case_rct_DCC_data_release_v2-1-0_250815_minor.tsv |
| DD entity | case |
| Entity category | administrative |
| Study track | rct |
| Source class | unclassified |
| Rows | 147 |
| Physical columns | 23 |
| DD-defined properties | 27 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.10.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 147 |
| Distinct primary IDs | 147 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.10.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | case.type | const | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | constant=case | case | CONST |
| project_id | case.project_id | const | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | case.submitter_id | id | string | 147 | 147 | 0 | 100.0% | 147 | 100.0% | unique 147/147; duplicates=0 | 11***al, 11***al, 11***al | UNIQUE |
| *studies.submitter_id | case.studies | fk | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | distinct parents=1; rows/parent median=147.0, max=147 | cl***al | CONST |
| actarm | case.actarm | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | Anakinra + Zinc=74 (50.3%); Prednisone=73 (49.7%); observed/allowed=2/3 | Prednisone, Anakinra + Zinc | ENUM_UNUSED |
| ah_hosp | case.ah_hosp | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ah_hosp_num | case.ah_hosp_num | num | number | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| aki_status | case.aki_status | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | No=98 (66.7%); Yes=49 (33.3%); observed/allowed=2/3 | No, Yes | ENUM_UNUSED |
| bari_surgery | case.bari_surgery | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| cohort | case.cohort | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| consent_type | case.consent_type | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_180_aki | case.days_180_aki | cat | string | 147 | 97 | 50 | 66.0% | 2 | 2.1% | Yes=49 (50.5%); No=48 (49.5%); observed/allowed=2/3 | Yes, No | ENUM_UNUSED |
| days_180_survival | case.days_180_survival | cat | string | 147 | 92 | 55 | 62.6% | 2 | 2.2% | alive=60 (65.2%); dead=32 (34.8%); observed/allowed=2/3 | dead, alive | ENUM_UNUSED |
| days_90_aki | case.days_90_aki | cat | string | 147 | 121 | 26 | 82.3% | 2 | 1.7% | No=76 (62.8%); Yes=45 (37.2%); observed/allowed=2/3 | No, Yes | ENUM_UNUSED |
| days_90_survival | case.days_90_survival | cat | string | 147 | 120 | 27 | 81.6% | 2 | 1.7% | alive=94 (78.3%); dead=26 (21.7%); observed/allowed=2/3 | alive, dead | ENUM_UNUSED |
| days_to_aki | case.days_to_aki | dayoff | number | 147 | 147 | 0 | 100.0% | 52 | 35.4% | min=0; max=180; negative=0; zero=6; common=180:48, 0:6, 7:6, 1:6, 9:5, 4:4, 8:4, 14:3 | 179, 32, 174 | — |
| days_to_consent | case.days_to_consent | dayoff | number | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_death | case.days_to_death | dayoff | number | 147 | 147 | 0 | 100.0% | 80 | 54.4% | min=0; max=480; negative=0; zero=3; common=187:9, 180:7, 186:6, 183:5, 1:4, 175:4, 176:3, 174:3 | 179, 48, 174 | — |
| index_date | case.index_date | const | string | 147 | 147 | 0 | 100.0% | 1 | 0.7% | constant=Study Enrollment | Study Enrollment | CONST,ENUM_UNUSED |
| inf_cnst_sign_dt | case.inf_cnst_sign_dt | cat | string | 147 | 0 | 147 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| rct_meld_strata | case.rct_meld_strata | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | Low(<=25)=79 (53.7%); High(>25)=68 (46.3%); observed/allowed=2/2 | Low(<=25), High(>25) | — |
| study_site | case.study_site | cat | string | 147 | 147 | 0 | 100.0% | 11 | 7.5% | Cleveland Clinic=25 (17.0%); Indiana University=18 (12.2%); University of Louisville=18 (12.2%); Virginia Commonwealth University=18 (12.2%); UT Southwestern - Parkland=16 (10.9%); University of Pittsburgh=14 (9.5%); Mayo Clinic=11 (7.5%); UT Southwestern=9 (6.1%); observed/allowed=11/16 | Cleveland Clinic, Indiana University, Mayo Clinic - FL | ENUM_UNUSED |
| vital_status | case.vital_status | cat | string | 147 | 147 | 0 | 100.0% | 2 | 1.4% | alive=111 (75.5%); dead=36 (24.5%); observed/allowed=2/3 | alive, dead | ENUM_UNUSED |

### 3.10.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 7 |
| ENUM_UNUSED | 9 |
| SPARSE | 7 |
| UNIQUE | 1 |

### 3.10.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| *studies.submitter_id | study.submitter_id | 147 | 1 | 147 | 0 | 100.0% | distinct parents=1; rows/parent median=147.0, max=147 |

### 3.10.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=147/147 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=147/147 |
| consent_type | consent_type | empty | non-empty=0/147 |
| inf_cnst_sign_dt | inf_cnst_sign_dt | empty | non-empty=0/147 |
| days_to_consent | days_to_consent | empty | non-empty=0/147 |
| index_date | index_date | populated | non-empty=147/147 |
| actarm | actarm | populated | non-empty=147/147 |
| cohort | cohort | empty | non-empty=0/147 |
| study_site | study_site | populated | non-empty=147/147 |
| bari_surgery | bari_surgery | empty | non-empty=0/147 |
| ah_hosp | ah_hosp | empty | non-empty=0/147 |
| ah_hosp_num | ah_hosp_num | empty | non-empty=0/147 |
| rct_meld_strata | rct_meld_strata | populated | non-empty=147/147 |
| vital_status | vital_status | populated | non-empty=147/147 |
| days_to_death | days_to_death | populated | non-empty=147/147 |
| aki_status | aki_status | populated | non-empty=147/147 |
| days_to_aki | days_to_aki | populated | non-empty=147/147 |
| days_90_survival | days_90_survival | populated | non-empty=120/147 |
| days_180_survival | days_180_survival | populated | non-empty=92/147 |
| days_90_aki | days_90_aki | populated | non-empty=121/147 |
| days_180_aki | days_180_aki | populated | non-empty=97/147 |
| studies | *studies.submitter_id | populated | non-empty=147/147 |
| project_id | project_id | populated | non-empty=147/147 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 27  
Physical headers: 23  
DD properties materialized: 23  
DD properties absent: 4  
Materialized but entirely empty: 7  
Physical headers not mapped to DD: 0

### 3.10.7 Machine-generated findings

- EMPTY: 7/23 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 147 distinct values in 147 non-empty rows.
- BROKEN_FK: 0/147 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_follow-up_add-on_cleaned_v2-1-0.tsv

### 3.11.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_follow-up_add-on_cleaned_v2-1-0.tsv |
| DD entity | follow_up |
| Entity category | administrative |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 25 |
| Physical columns | 106 |
| DD-defined properties | 110 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.11.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 25 |
| Distinct primary IDs | 25 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 21 | 91.3% |
| 2 | 2 | 8.7% |

### 3.11.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | follow_up.type | const | string | 25 | 25 | 0 | 100.0% | 1 | 4.0% | constant=follow_up | follow_up | CONST |
| project_id | follow_up.project_id | const | string | 25 | 25 | 0 | 100.0% | 1 | 4.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | follow_up.submitter_id | id | string | 25 | 25 | 0 | 100.0% | 25 | 100.0% | unique 25/25; duplicates=0 | 11***68, 11***84, 21***28 | UNIQUE |
| cases.submitter_id | follow_up.cases | fk | string | 25 | 25 | 0 | 100.0% | 23 | 92.0% | distinct parents=23; rows/parent median=1.0, max=2 | 11***bs, 11***bs, 21***bs | — |
| demographics.submitter_id | follow_up.demographics | fk | string | 25 | 25 | 0 | 100.0% | 23 | 92.0% | distinct parents=23; rows/parent median=1.0, max=2 | 11***ic, 11***ic, 21***ic | — |
| *days_to_follow_up | follow_up.days_to_follow_up | dayoff | number | 25 | 25 | 0 | 100.0% | 8 | 32.0% | min=3; max=168; negative=0; zero=0; common=28:9, 84:6, 7:3, 14:2, 3:2, 168:1, 90:1, 8:1 | 168, 84, 28 | — |
| admission_date | follow_up.admission_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_culture | follow_up.ascites_culture | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_culture_result | follow_up.ascites_culture_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_date | follow_up.ascites_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_diagnosis_date | follow_up.ascites_diagnosis_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_organism | follow_up.ascites_organism | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| bariatric_surgery | follow_up.bariatric_surgery | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture | follow_up.blood_culture | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture_date | follow_up.blood_culture_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture_result | follow_up.blood_culture_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_organism | follow_up.blood_organism | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| bmi | follow_up.bmi | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| cdc_hiv_risk_factors | follow_up.cdc_hiv_risk_factors | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| child_pugh_score | follow_up.child_pugh_score | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_date | follow_up.ct_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result | follow_up.ct_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_finding | follow_up.ct_result_finding | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_sig | follow_up.ct_result_sig | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| duodenum_ulcer_bleed | follow_up.duodenum_ulcer_bleed | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| duodenum_ulcer_size | follow_up.duodenum_ulcer_size | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy | follow_up.endoscopy | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy_date | follow_up.endoscopy_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy_ulcer_present | follow_up.endoscopy_ulcer_present | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy_varices_present | follow_up.endoscopy_varices_present | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_ulcer_bleed | follow_up.esophageal_ulcer_bleed | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_ulcer_size | follow_up.esophageal_ulcer_size | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_varices_bleed | follow_up.esophageal_varices_bleed | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_varices_size | follow_up.esophageal_varices_size | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| event_type | follow_up.event_type | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_capmed | follow_up.fibro_capmed | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_e | follow_up.fibro_e | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_iqr | follow_up.fibro_iqr | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_probe | follow_up.fibro_probe | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_total_number | follow_up.fibro_total_number | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan | follow_up.fibroscan | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan_date | follow_up.fibroscan_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_e_iqr | follow_up.firbro_e_iqr | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_valid_number | follow_up.firbro_valid_number | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_ulcer_bleed | follow_up.gastric_ulcer_bleed | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_ulcer_size | follow_up.gastric_ulcer_size | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_varices_bleed | follow_up.gastric_varices_bleed | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_varices_size | follow_up.gastric_varices_size | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| height | follow_up.height | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_carcinoma | follow_up.hep_carcinoma | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_enceph | follow_up.hep_enceph | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_enceph_diagnosis_date | follow_up.hep_enceph_diagnosis_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hepcar_diagnosis_date | follow_up.hepcar_diagnosis_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_alc_hep | follow_up.hospitalized_alc_hep | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_alc_hep_times | follow_up.hospitalized_alc_hep_times | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_at_enrollment | follow_up.hospitalized_at_enrollment | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| infection_screen_date | follow_up.infection_screen_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| infection_screen_done | follow_up.infection_screen_done | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| lille_score | follow_up.lille_score | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_abdomen_imaging | follow_up.liver_abdomen_imaging | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_imaging_type | follow_up.liver_imaging_type | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_collected | follow_up.liver_score_collected | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_date | follow_up.liver_score_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_transplant | follow_up.liver_transplant | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_transplant_date | follow_up.liver_transplant_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| maddreys_score | follow_up.maddreys_score | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| medical_info_collected | follow_up.medical_info_collected | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| meld_score | follow_up.meld_score | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_date | follow_up.mri_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_finding | follow_up.mri_finding | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_result | follow_up.mri_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_sig | follow_up.mri_sig | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_date | follow_up.other_imaging_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_finding | follow_up.other_imaging_finding | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_result | follow_up.other_imaging_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_sig | follow_up.other_imaging_sig | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_type | follow_up.other_imaging_type | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| portal_hypertensive_gastropathy | follow_up.portal_hypertensive_gastropathy | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| soc_collected | follow_up.soc_collected | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test | follow_up.stool_test | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_date | follow_up.stool_test_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_finding | follow_up.stool_test_finding | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_collected | follow_up.tlfb_collected | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_drinking_days | follow_up.tlfb_drinking_days | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_number_drinks | follow_up.tlfb_number_drinks | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_date | follow_up.ultrasound_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_finding | follow_up.ultrasound_finding | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result | follow_up.ultrasound_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result_sig | follow_up.ultrasound_result_sig | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture | follow_up.urine_culture | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture_date | follow_up.urine_culture_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture_fungal_result | follow_up.urine_culture_fungal_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture_organism | follow_up.urine_culture_organism | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture_result | follow_up.urine_culture_result | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| varices | follow_up.varices | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| varices_diagnosis_date | follow_up.varices_diagnosis_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| visit_day | follow_up.visit_day | dayoff | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| weight | follow_up.weight | num | number | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray | follow_up.xray | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_date | follow_up.xray_date | date | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_findings | follow_up.xray_findings | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_impression | follow_up.xray_impression | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_infiltrates | follow_up.xray_infiltrates | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_last_4_weeks | follow_up.xray_last_4_weeks | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_normal | follow_up.xray_normal | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_pleural_effusion | follow_up.xray_pleural_effusion | cat | string | 25 | 0 | 25 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.11.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 100 |
| SPARSE | 100 |
| UNIQUE | 1 |

### 3.11.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| cases.submitter_id | case.submitter_id | 25 | 23 | 25 | 0 | 100.0% | distinct parents=23; rows/parent median=1.0, max=2 |
| demographics.submitter_id | demographic.submitter_id | 25 | 23 | 25 | 0 | 100.0% | distinct parents=23; rows/parent median=1.0, max=2 |

### 3.11.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=25/25 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=25/25 |
| days_to_follow_up | *days_to_follow_up | populated | non-empty=25/25 |
| event_type | event_type | empty | non-empty=0/25 |
| visit_day | visit_day | empty | non-empty=0/25 |
| cdc_hiv_risk_factors | cdc_hiv_risk_factors | empty | non-empty=0/25 |
| height | height | empty | non-empty=0/25 |
| weight | weight | empty | non-empty=0/25 |
| bmi | bmi | empty | non-empty=0/25 |
| soc_collected | soc_collected | empty | non-empty=0/25 |
| infection_screen_done | infection_screen_done | empty | non-empty=0/25 |
| infection_screen_date | infection_screen_date | empty | non-empty=0/25 |
| blood_culture | blood_culture | empty | non-empty=0/25 |
| blood_culture_result | blood_culture_result | empty | non-empty=0/25 |
| blood_organism | blood_organism | empty | non-empty=0/25 |
| blood_culture_date | blood_culture_date | empty | non-empty=0/25 |
| urine_culture | urine_culture | empty | non-empty=0/25 |
| urine_culture_result | urine_culture_result | empty | non-empty=0/25 |
| urine_culture_organism | urine_culture_organism | empty | non-empty=0/25 |
| urine_culture_date | urine_culture_date | empty | non-empty=0/25 |
| urine_culture_fungal_result | urine_culture_fungal_result | empty | non-empty=0/25 |
| ascites_culture | ascites_culture | empty | non-empty=0/25 |
| ascites_culture_result | ascites_culture_result | empty | non-empty=0/25 |
| ascites_organism | ascites_organism | empty | non-empty=0/25 |
| ascites_date | ascites_date | empty | non-empty=0/25 |
| xray | xray | empty | non-empty=0/25 |
| xray_last_4_weeks | xray_last_4_weeks | empty | non-empty=0/25 |
| xray_date | xray_date | empty | non-empty=0/25 |
| xray_infiltrates | xray_infiltrates | empty | non-empty=0/25 |
| xray_impression | xray_impression | empty | non-empty=0/25 |
| xray_pleural_effusion | xray_pleural_effusion | empty | non-empty=0/25 |
| xray_normal | xray_normal | empty | non-empty=0/25 |
| xray_findings | xray_findings | empty | non-empty=0/25 |
| endoscopy | endoscopy | empty | non-empty=0/25 |
| endoscopy_date | endoscopy_date | empty | non-empty=0/25 |
| endoscopy_varices_present | endoscopy_varices_present | empty | non-empty=0/25 |
| esophageal_varices_size | esophageal_varices_size | empty | non-empty=0/25 |
| esophageal_varices_bleed | esophageal_varices_bleed | empty | non-empty=0/25 |
| gastric_varices_size | gastric_varices_size | empty | non-empty=0/25 |
| gastric_varices_bleed | gastric_varices_bleed | empty | non-empty=0/25 |
| portal_hypertensive_gastropathy | portal_hypertensive_gastropathy | empty | non-empty=0/25 |
| endoscopy_ulcer_present | endoscopy_ulcer_present | empty | non-empty=0/25 |
| esophageal_ulcer_size | esophageal_ulcer_size | empty | non-empty=0/25 |
| esophageal_ulcer_bleed | esophageal_ulcer_bleed | empty | non-empty=0/25 |
| gastric_ulcer_size | gastric_ulcer_size | empty | non-empty=0/25 |
| gastric_ulcer_bleed | gastric_ulcer_bleed | empty | non-empty=0/25 |
| duodenum_ulcer_size | duodenum_ulcer_size | empty | non-empty=0/25 |
| duodenum_ulcer_bleed | duodenum_ulcer_bleed | empty | non-empty=0/25 |
| fibroscan | fibroscan | empty | non-empty=0/25 |
| fibroscan_date | fibroscan_date | empty | non-empty=0/25 |
| fibro_capmed | fibro_capmed | empty | non-empty=0/25 |
| fibro_iqr | fibro_iqr | empty | non-empty=0/25 |
| fibro_e | fibro_e | empty | non-empty=0/25 |
| firbro_e_iqr | firbro_e_iqr | empty | non-empty=0/25 |
| fibro_probe | fibro_probe | empty | non-empty=0/25 |
| firbro_valid_number | firbro_valid_number | empty | non-empty=0/25 |
| fibro_total_number | fibro_total_number | empty | non-empty=0/25 |
| liver_abdomen_imaging | liver_abdomen_imaging | empty | non-empty=0/25 |
| liver_imaging_type | liver_imaging_type | empty | non-empty=0/25 |
| ultrasound_date | ultrasound_date | empty | non-empty=0/25 |
| ultrasound_result | ultrasound_result | empty | non-empty=0/25 |
| ultrasound_result_sig | ultrasound_result_sig | empty | non-empty=0/25 |
| ultrasound_finding | ultrasound_finding | empty | non-empty=0/25 |
| ct_date | ct_date | empty | non-empty=0/25 |
| ct_result | ct_result | empty | non-empty=0/25 |
| ct_result_sig | ct_result_sig | empty | non-empty=0/25 |
| ct_result_finding | ct_result_finding | empty | non-empty=0/25 |
| mri_date | mri_date | empty | non-empty=0/25 |
| mri_result | mri_result | empty | non-empty=0/25 |
| mri_sig | mri_sig | empty | non-empty=0/25 |
| mri_finding | mri_finding | empty | non-empty=0/25 |
| other_imaging_date | other_imaging_date | empty | non-empty=0/25 |
| other_imaging_type | other_imaging_type | empty | non-empty=0/25 |
| other_imaging_result | other_imaging_result | empty | non-empty=0/25 |
| other_imaging_sig | other_imaging_sig | empty | non-empty=0/25 |
| other_imaging_finding | other_imaging_finding | empty | non-empty=0/25 |
| medical_info_collected | medical_info_collected | empty | non-empty=0/25 |
| ascites_diagnosis_date | ascites_diagnosis_date | empty | non-empty=0/25 |
| hep_enceph | hep_enceph | empty | non-empty=0/25 |
| hep_enceph_diagnosis_date | hep_enceph_diagnosis_date | empty | non-empty=0/25 |
| varices | varices | empty | non-empty=0/25 |
| varices_diagnosis_date | varices_diagnosis_date | empty | non-empty=0/25 |
| hep_carcinoma | hep_carcinoma | empty | non-empty=0/25 |
| hepcar_diagnosis_date | hepcar_diagnosis_date | empty | non-empty=0/25 |
| liver_transplant | liver_transplant | empty | non-empty=0/25 |
| liver_transplant_date | liver_transplant_date | empty | non-empty=0/25 |
| stool_test | stool_test | empty | non-empty=0/25 |
| stool_test_finding | stool_test_finding | empty | non-empty=0/25 |
| stool_test_date | stool_test_date | empty | non-empty=0/25 |
| bariatric_surgery | bariatric_surgery | empty | non-empty=0/25 |
| hospitalized_alc_hep | hospitalized_alc_hep | empty | non-empty=0/25 |
| hospitalized_alc_hep_times | hospitalized_alc_hep_times | empty | non-empty=0/25 |
| hospitalized_at_enrollment | hospitalized_at_enrollment | empty | non-empty=0/25 |
| admission_date | admission_date | empty | non-empty=0/25 |
| liver_score_collected | liver_score_collected | empty | non-empty=0/25 |
| liver_score_date | liver_score_date | empty | non-empty=0/25 |
| meld_score | meld_score | empty | non-empty=0/25 |
| child_pugh_score | child_pugh_score | empty | non-empty=0/25 |
| lille_score | lille_score | empty | non-empty=0/25 |
| maddreys_score | maddreys_score | empty | non-empty=0/25 |
| tlfb_collected | tlfb_collected | empty | non-empty=0/25 |
| tlfb_number_drinks | tlfb_number_drinks | empty | non-empty=0/25 |
| tlfb_drinking_days | tlfb_drinking_days | empty | non-empty=0/25 |
| cases | cases.submitter_id | populated | non-empty=25/25 |
| demographics | demographics.submitter_id | populated | non-empty=25/25 |
| project_id | project_id | populated | non-empty=25/25 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 110  
Physical headers: 106  
DD properties materialized: 106  
DD properties absent: 4  
Materialized but entirely empty: 100  
Physical headers not mapped to DD: 0

### 3.11.7 Machine-generated findings

- EMPTY: 100/106 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 25 distinct values in 25 non-empty rows.
- BROKEN_FK: 0/50 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv

### 3.12.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv |
| DD entity | follow_up |
| Entity category | administrative |
| Study track | obs |
| Source class | unclassified |
| Rows | 2140 |
| Physical columns | 106 |
| DD-defined properties | 110 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.12.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 2140 |
| Distinct primary IDs | 2140 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 560 | 49.5% |
| 2 | 291 | 25.7% |
| 3 | 126 | 11.1% |
| 4 | 155 | 13.7% |

### 3.12.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | follow_up.type | const | string | 2140 | 2140 | 0 | 100.0% | 1 | 0.0% | constant=follow_up | follow_up | CONST |
| project_id | follow_up.project_id | const | string | 2140 | 2140 | 0 | 100.0% | 1 | 0.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | follow_up.submitter_id | id | string | 2140 | 2140 | 0 | 100.0% | 2140 | 100.0% | unique 2140/2140; duplicates=0 | 11***_0, 11***_0, 11***_0 | UNIQUE |
| cases.submitter_id | follow_up.cases | fk | string | 2140 | 2140 | 0 | 100.0% | 1132 | 52.9% | distinct parents=1132; rows/parent median=2.0, max=4 | 11***bs, 11***bs, 11***bs | — |
| demographics.submitter_id | follow_up.demographics | fk | string | 2140 | 2140 | 0 | 100.0% | 1132 | 52.9% | distinct parents=1132; rows/parent median=2.0, max=4 | 11***ic, 11***ic, 11***ic | — |
| *days_to_follow_up | follow_up.days_to_follow_up | dayoff | number | 2140 | 2140 | 0 | 100.0% | 4 | 0.2% | min=0; max=168; negative=0; zero=1132; common=0:1132, 28:399, 168:345, 84:264 | 0, 28, 84 | — |
| admission_date | follow_up.admission_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_culture | follow_up.ascites_culture | cat | string | 2140 | 1116 | 1024 | 52.1% | 3 | 0.3% | Not Done=622 (55.7%); No=402 (36.0%); Yes=92 (8.2%); observed/allowed=3/5 | No, Yes, Not Done | ENUM_UNUSED |
| ascites_culture_result | follow_up.ascites_culture_result | cat | string | 2140 | 286 | 1854 | 13.4% | 2 | 0.7% | Negative=269 (94.1%); Positive=17 (5.9%); observed/allowed=2/3 | Negative, Positive | ENUM_UNUSED,SPARSE |
| ascites_date | follow_up.ascites_date | date | string | 2140 | 91 | 2049 | 4.3% | 59 | 64.8% | earliest=—; latest=—; invalid=91 | 0, 24, 19 | SPARSE |
| ascites_diagnosis_date | follow_up.ascites_diagnosis_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_organism | follow_up.ascites_organism | text | string | 2140 | 17 | 2123 | 0.8% | 15 | 88.2% | length min=11; mean=30.4; max=85; blank-string=0 | Escherichia coli, Vancomycin resistant Enterococ, Enterobacter cloacae complex A | SPARSE |
| bariatric_surgery | follow_up.bariatric_surgery | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture | follow_up.blood_culture | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture_date | follow_up.blood_culture_date | date | string | 2140 | 635 | 1505 | 29.7% | 105 | 16.5% | earliest=—; latest=—; invalid=635 | -2, 76, 78 | — |
| blood_culture_result | follow_up.blood_culture_result | cat | string | 2140 | 703 | 1437 | 32.9% | 2 | 0.3% | Negative=661 (94.0%); Positive=42 (6.0%); observed/allowed=2/2 | Positive, Negative | — |
| blood_organism | follow_up.blood_organism | text | string | 2140 | 42 | 2098 | 2.0% | 37 | 88.1% | length min=4; mean=29.0; max=100; blank-string=0 | Escherichia coli, ESBL, Klebsiella pneumoniae, Vancomycin resistant Enterococ | SPARSE |
| bmi | follow_up.bmi | num | number | 2140 | 1611 | 529 | 75.3% | 395 | 24.5% | min=14.47; p25=23.65; median=27.1; mean=28.4368; p75=32.035; max=73.5 | 22.4, 37.1, 36.3 | — |
| cdc_hiv_risk_factors | follow_up.cdc_hiv_risk_factors | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| child_pugh_score | follow_up.child_pugh_score | num | number | 2140 | 1748 | 392 | 81.7% | 12 | 0.7% | min=0; p25=5; median=8; mean=8.32551; p75=11; max=15 | 5, 11, 10 | — |
| ct_date | follow_up.ct_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result | follow_up.ct_result | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_finding | follow_up.ct_result_finding | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_sig | follow_up.ct_result_sig | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| duodenum_ulcer_bleed | follow_up.duodenum_ulcer_bleed | cat | string | 2140 | 13 | 2127 | 0.6% | 2 | 15.4% | No=9 (69.2%); Yes=4 (30.8%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED,SPARSE |
| duodenum_ulcer_size | follow_up.duodenum_ulcer_size | cat | string | 2140 | 5 | 2135 | 0.2% | 2 | 40.0% | Small=4 (80.0%); Medium=1 (20.0%); observed/allowed=2/5 | Medium, Small | ENUM_UNUSED,SPARSE |
| endoscopy | follow_up.endoscopy | cat | string | 2140 | 1380 | 760 | 64.5% | 2 | 0.1% | No=1033 (74.9%); Yes=347 (25.1%); observed/allowed=2/2 | Yes, No | — |
| endoscopy_date | follow_up.endoscopy_date | date | string | 2140 | 223 | 1917 | 10.4% | 95 | 42.6% | earliest=—; latest=—; invalid=223 | -5, -1, 138 | SPARSE |
| endoscopy_ulcer_present | follow_up.endoscopy_ulcer_present | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy_varices_present | follow_up.endoscopy_varices_present | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_ulcer_bleed | follow_up.esophageal_ulcer_bleed | cat | string | 2140 | 28 | 2112 | 1.3% | 2 | 7.1% | No=20 (71.4%); Yes=8 (28.6%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED,SPARSE |
| esophageal_ulcer_size | follow_up.esophageal_ulcer_size | cat | string | 2140 | 22 | 2118 | 1.0% | 3 | 13.6% | Small=13 (59.1%); Medium=5 (22.7%); Large=4 (18.2%); observed/allowed=3/5 | Medium, Small, Large | ENUM_UNUSED,SPARSE |
| esophageal_varices_bleed | follow_up.esophageal_varices_bleed | cat | string | 2140 | 175 | 1965 | 8.2% | 2 | 1.1% | No=160 (91.4%); Yes=15 (8.6%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED,SPARSE |
| esophageal_varices_size | follow_up.esophageal_varices_size | cat | string | 2140 | 187 | 1953 | 8.7% | 3 | 1.6% | Small=110 (58.8%); Large=48 (25.7%); Medium=29 (15.5%); observed/allowed=3/5 | Medium, Small, Large | ENUM_UNUSED,SPARSE |
| event_type | follow_up.event_type | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_capmed | follow_up.fibro_capmed | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_e | follow_up.fibro_e | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_iqr | follow_up.fibro_iqr | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_probe | follow_up.fibro_probe | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_total_number | follow_up.fibro_total_number | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan | follow_up.fibroscan | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan_date | follow_up.fibroscan_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_e_iqr | follow_up.firbro_e_iqr | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_valid_number | follow_up.firbro_valid_number | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_ulcer_bleed | follow_up.gastric_ulcer_bleed | cat | string | 2140 | 28 | 2112 | 1.3% | 2 | 7.1% | No=23 (82.1%); Yes=5 (17.9%); observed/allowed=2/4 | Yes, No | ENUM_UNUSED,SPARSE |
| gastric_ulcer_size | follow_up.gastric_ulcer_size | cat | string | 2140 | 23 | 2117 | 1.1% | 3 | 13.0% | Small=15 (65.2%); Large=6 (26.1%); Medium=2 (8.7%); observed/allowed=3/5 | Small, Large, Medium | ENUM_UNUSED,SPARSE |
| gastric_varices_bleed | follow_up.gastric_varices_bleed | cat | string | 2140 | 14 | 2126 | 0.7% | 2 | 14.3% | No=11 (78.6%); Yes=3 (21.4%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED,SPARSE |
| gastric_varices_size | follow_up.gastric_varices_size | cat | string | 2140 | 9 | 2131 | 0.4% | 3 | 33.3% | Small=7 (77.8%); Medium=1 (11.1%); Large=1 (11.1%); observed/allowed=3/5 | Small, Medium, Large | ENUM_UNUSED,SPARSE |
| height | follow_up.height | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_carcinoma | follow_up.hep_carcinoma | cat | string | 2140 | 1868 | 272 | 87.3% | 2 | 0.1% | No=1864 (99.8%); Yes=4 (0.2%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED |
| hep_enceph | follow_up.hep_enceph | cat | string | 2140 | 1864 | 276 | 87.1% | 2 | 0.1% | No=1565 (84.0%); Yes=299 (16.0%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED |
| hep_enceph_diagnosis_date | follow_up.hep_enceph_diagnosis_date | date | string | 2140 | 294 | 1846 | 13.7% | 101 | 34.4% | earliest=—; latest=—; invalid=294 | -26, -14, -31 | SPARSE |
| hepcar_diagnosis_date | follow_up.hepcar_diagnosis_date | date | string | 2140 | 4 | 2136 | 0.2% | 3 | 75.0% | earliest=—; latest=—; invalid=4 | -2393, -491, 12 | SPARSE |
| hospitalized_alc_hep | follow_up.hospitalized_alc_hep | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_alc_hep_times | follow_up.hospitalized_alc_hep_times | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_at_enrollment | follow_up.hospitalized_at_enrollment | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| infection_screen_date | follow_up.infection_screen_date | date | string | 2140 | 820 | 1320 | 38.3% | 162 | 19.8% | earliest=—; latest=—; invalid=820 | 108, 78, 0 | — |
| infection_screen_done | follow_up.infection_screen_done | cat | string | 2140 | 1379 | 761 | 64.4% | 2 | 0.1% | Yes=911 (66.1%); No=468 (33.9%); observed/allowed=2/2 | No, Yes | — |
| lille_score | follow_up.lille_score | num | number | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_abdomen_imaging | follow_up.liver_abdomen_imaging | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_imaging_type | follow_up.liver_imaging_type | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_collected | follow_up.liver_score_collected | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_date | follow_up.liver_score_date | date | string | 2140 | 1187 | 953 | 55.5% | 218 | 18.4% | earliest=—; latest=—; invalid=1187 | 0, 34, 119 | — |
| liver_transplant | follow_up.liver_transplant | cat | string | 2140 | 1873 | 267 | 87.5% | 2 | 0.1% | No=1867 (99.7%); Yes=6 (0.3%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED |
| liver_transplant_date | follow_up.liver_transplant_date | date | string | 2140 | 6 | 2134 | 0.3% | 6 | 100.0% | earliest=—; latest=—; invalid=6 | 225, 14, 7 | SPARSE,UNIQUE |
| maddreys_score | follow_up.maddreys_score | num | number | 2140 | 1918 | 222 | 89.6% | 1488 | 77.6% | min=-20.1; p25=-1.8; median=21.38; mean=30.3479; p75=53.275; max=279.12 | -10.02, -14.42, 94.72 | NEG |
| medical_info_collected | follow_up.medical_info_collected | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| meld_score | follow_up.meld_score | num | number | 2140 | 1938 | 202 | 90.6% | 52 | 2.7% | min=0; p25=8; median=18; mean=18.8767; p75=26; max=54 | 10, 6, 37 | — |
| mri_date | follow_up.mri_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_finding | follow_up.mri_finding | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_result | follow_up.mri_result | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_sig | follow_up.mri_sig | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_date | follow_up.other_imaging_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_finding | follow_up.other_imaging_finding | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_result | follow_up.other_imaging_result | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_sig | follow_up.other_imaging_sig | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_type | follow_up.other_imaging_type | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| portal_hypertensive_gastropathy | follow_up.portal_hypertensive_gastropathy | cat | string | 2140 | 233 | 1907 | 10.9% | 4 | 1.7% | Yes, Mild=83 (35.6%); Yes, Unknown severity=74 (31.8%); Yes, Moderate=59 (25.3%); Yes, Severe=17 (7.3%); observed/allowed=4/7 | Yes, Moderate, Yes, Mild, Yes, Severe | ENUM_UNUSED,SPARSE |
| soc_collected | follow_up.soc_collected | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test | follow_up.stool_test | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_date | follow_up.stool_test_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_finding | follow_up.stool_test_finding | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_collected | follow_up.tlfb_collected | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_drinking_days | follow_up.tlfb_drinking_days | num | number | 2140 | 1706 | 434 | 79.7% | 31 | 1.8% | min=0; p25=0; median=4; mean=10.7503; p75=24; max=30 | 4, 0, 9 | — |
| tlfb_number_drinks | follow_up.tlfb_number_drinks | num | number | 2140 | 1710 | 430 | 79.9% | 326 | 19.1% | min=0; p25=0; median=11.5; mean=104.013; p75=150; max=1960 | 4, 0, 13 | — |
| ultrasound_date | follow_up.ultrasound_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_finding | follow_up.ultrasound_finding | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result | follow_up.ultrasound_result | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result_sig | follow_up.ultrasound_result_sig | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture | follow_up.urine_culture | const | string | 2140 | 499 | 1641 | 23.3% | 1 | 0.2% | constant=Not Done | Not Done | CONST,ENUM_UNUSED |
| urine_culture_date | follow_up.urine_culture_date | date | string | 2140 | 358 | 1782 | 16.7% | 84 | 23.5% | earliest=—; latest=—; invalid=358 | 74, -4, -1 | SPARSE |
| urine_culture_fungal_result | follow_up.urine_culture_fungal_result | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture_organism | follow_up.urine_culture_organism | text | string | 2140 | 118 | 2022 | 5.5% | 90 | 76.3% | length min=5; mean=31.5; max=191; blank-string=0 | Enterococcus faecium, Enterococcus faecalis, Vancomycin resistant enterococ | SPARSE |
| urine_culture_result | follow_up.urine_culture_result | cat | string | 2140 | 412 | 1728 | 19.3% | 2 | 0.5% | Negative=295 (71.6%); Positive=117 (28.4%); observed/allowed=2/3 | Negative, Positive | ENUM_UNUSED,SPARSE |
| varices | follow_up.varices | cat | string | 2140 | 1854 | 286 | 86.6% | 2 | 0.1% | No=1648 (88.9%); Yes=206 (11.1%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED |
| varices_diagnosis_date | follow_up.varices_diagnosis_date | date | string | 2140 | 205 | 1935 | 9.6% | 97 | 47.3% | earliest=—; latest=—; invalid=205 | 6, -5, -6 | SPARSE |
| visit_day | follow_up.visit_day | dayoff | number | 2140 | 2140 | 0 | 100.0% | 4 | 0.2% | min=0; max=168; negative=0; zero=1132; common=0:1132, 28:399, 168:345, 84:264 | 0, 28, 84 | ENUM_UNUSED |
| weight | follow_up.weight | num | number | 2140 | 1750 | 390 | 81.8% | 761 | 43.5% | min=39.9; p25=68; median=81.6; mean=85.0824; p75=97.3; max=216.2 | 67.6, 102.9, 123.2 | — |
| xray | follow_up.xray | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_date | follow_up.xray_date | date | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_findings | follow_up.xray_findings | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_impression | follow_up.xray_impression | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_infiltrates | follow_up.xray_infiltrates | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_last_4_weeks | follow_up.xray_last_4_weeks | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_normal | follow_up.xray_normal | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_pleural_effusion | follow_up.xray_pleural_effusion | cat | string | 2140 | 0 | 2140 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.12.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 57 |
| ENUM_UNUSED | 20 |
| NEG | 1 |
| SPARSE | 80 |
| UNIQUE | 2 |

### 3.12.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| cases.submitter_id | case.submitter_id | 2140 | 1132 | 2140 | 0 | 100.0% | distinct parents=1132; rows/parent median=2.0, max=4 |
| demographics.submitter_id | demographic.submitter_id | 2140 | 1132 | 2140 | 0 | 100.0% | distinct parents=1132; rows/parent median=2.0, max=4 |

### 3.12.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=2140/2140 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=2140/2140 |
| days_to_follow_up | *days_to_follow_up | populated | non-empty=2140/2140 |
| event_type | event_type | empty | non-empty=0/2140 |
| visit_day | visit_day | populated | non-empty=2140/2140 |
| cdc_hiv_risk_factors | cdc_hiv_risk_factors | empty | non-empty=0/2140 |
| height | height | empty | non-empty=0/2140 |
| weight | weight | populated | non-empty=1750/2140 |
| bmi | bmi | populated | non-empty=1611/2140 |
| soc_collected | soc_collected | empty | non-empty=0/2140 |
| infection_screen_done | infection_screen_done | populated | non-empty=1379/2140 |
| infection_screen_date | infection_screen_date | populated | non-empty=820/2140 |
| blood_culture | blood_culture | empty | non-empty=0/2140 |
| blood_culture_result | blood_culture_result | populated | non-empty=703/2140 |
| blood_organism | blood_organism | populated | non-empty=42/2140 |
| blood_culture_date | blood_culture_date | populated | non-empty=635/2140 |
| urine_culture | urine_culture | populated | non-empty=499/2140 |
| urine_culture_result | urine_culture_result | populated | non-empty=412/2140 |
| urine_culture_organism | urine_culture_organism | populated | non-empty=118/2140 |
| urine_culture_date | urine_culture_date | populated | non-empty=358/2140 |
| urine_culture_fungal_result | urine_culture_fungal_result | empty | non-empty=0/2140 |
| ascites_culture | ascites_culture | populated | non-empty=1116/2140 |
| ascites_culture_result | ascites_culture_result | populated | non-empty=286/2140 |
| ascites_organism | ascites_organism | populated | non-empty=17/2140 |
| ascites_date | ascites_date | populated | non-empty=91/2140 |
| xray | xray | empty | non-empty=0/2140 |
| xray_last_4_weeks | xray_last_4_weeks | empty | non-empty=0/2140 |
| xray_date | xray_date | empty | non-empty=0/2140 |
| xray_infiltrates | xray_infiltrates | empty | non-empty=0/2140 |
| xray_impression | xray_impression | empty | non-empty=0/2140 |
| xray_pleural_effusion | xray_pleural_effusion | empty | non-empty=0/2140 |
| xray_normal | xray_normal | empty | non-empty=0/2140 |
| xray_findings | xray_findings | empty | non-empty=0/2140 |
| endoscopy | endoscopy | populated | non-empty=1380/2140 |
| endoscopy_date | endoscopy_date | populated | non-empty=223/2140 |
| endoscopy_varices_present | endoscopy_varices_present | empty | non-empty=0/2140 |
| esophageal_varices_size | esophageal_varices_size | populated | non-empty=187/2140 |
| esophageal_varices_bleed | esophageal_varices_bleed | populated | non-empty=175/2140 |
| gastric_varices_size | gastric_varices_size | populated | non-empty=9/2140 |
| gastric_varices_bleed | gastric_varices_bleed | populated | non-empty=14/2140 |
| portal_hypertensive_gastropathy | portal_hypertensive_gastropathy | populated | non-empty=233/2140 |
| endoscopy_ulcer_present | endoscopy_ulcer_present | empty | non-empty=0/2140 |
| esophageal_ulcer_size | esophageal_ulcer_size | populated | non-empty=22/2140 |
| esophageal_ulcer_bleed | esophageal_ulcer_bleed | populated | non-empty=28/2140 |
| gastric_ulcer_size | gastric_ulcer_size | populated | non-empty=23/2140 |
| gastric_ulcer_bleed | gastric_ulcer_bleed | populated | non-empty=28/2140 |
| duodenum_ulcer_size | duodenum_ulcer_size | populated | non-empty=5/2140 |
| duodenum_ulcer_bleed | duodenum_ulcer_bleed | populated | non-empty=13/2140 |
| fibroscan | fibroscan | empty | non-empty=0/2140 |
| fibroscan_date | fibroscan_date | empty | non-empty=0/2140 |
| fibro_capmed | fibro_capmed | empty | non-empty=0/2140 |
| fibro_iqr | fibro_iqr | empty | non-empty=0/2140 |
| fibro_e | fibro_e | empty | non-empty=0/2140 |
| firbro_e_iqr | firbro_e_iqr | empty | non-empty=0/2140 |
| fibro_probe | fibro_probe | empty | non-empty=0/2140 |
| firbro_valid_number | firbro_valid_number | empty | non-empty=0/2140 |
| fibro_total_number | fibro_total_number | empty | non-empty=0/2140 |
| liver_abdomen_imaging | liver_abdomen_imaging | empty | non-empty=0/2140 |
| liver_imaging_type | liver_imaging_type | empty | non-empty=0/2140 |
| ultrasound_date | ultrasound_date | empty | non-empty=0/2140 |
| ultrasound_result | ultrasound_result | empty | non-empty=0/2140 |
| ultrasound_result_sig | ultrasound_result_sig | empty | non-empty=0/2140 |
| ultrasound_finding | ultrasound_finding | empty | non-empty=0/2140 |
| ct_date | ct_date | empty | non-empty=0/2140 |
| ct_result | ct_result | empty | non-empty=0/2140 |
| ct_result_sig | ct_result_sig | empty | non-empty=0/2140 |
| ct_result_finding | ct_result_finding | empty | non-empty=0/2140 |
| mri_date | mri_date | empty | non-empty=0/2140 |
| mri_result | mri_result | empty | non-empty=0/2140 |
| mri_sig | mri_sig | empty | non-empty=0/2140 |
| mri_finding | mri_finding | empty | non-empty=0/2140 |
| other_imaging_date | other_imaging_date | empty | non-empty=0/2140 |
| other_imaging_type | other_imaging_type | empty | non-empty=0/2140 |
| other_imaging_result | other_imaging_result | empty | non-empty=0/2140 |
| other_imaging_sig | other_imaging_sig | empty | non-empty=0/2140 |
| other_imaging_finding | other_imaging_finding | empty | non-empty=0/2140 |
| medical_info_collected | medical_info_collected | empty | non-empty=0/2140 |
| ascites_diagnosis_date | ascites_diagnosis_date | empty | non-empty=0/2140 |
| hep_enceph | hep_enceph | populated | non-empty=1864/2140 |
| hep_enceph_diagnosis_date | hep_enceph_diagnosis_date | populated | non-empty=294/2140 |
| varices | varices | populated | non-empty=1854/2140 |
| varices_diagnosis_date | varices_diagnosis_date | populated | non-empty=205/2140 |
| hep_carcinoma | hep_carcinoma | populated | non-empty=1868/2140 |
| hepcar_diagnosis_date | hepcar_diagnosis_date | populated | non-empty=4/2140 |
| liver_transplant | liver_transplant | populated | non-empty=1873/2140 |
| liver_transplant_date | liver_transplant_date | populated | non-empty=6/2140 |
| stool_test | stool_test | empty | non-empty=0/2140 |
| stool_test_finding | stool_test_finding | empty | non-empty=0/2140 |
| stool_test_date | stool_test_date | empty | non-empty=0/2140 |
| bariatric_surgery | bariatric_surgery | empty | non-empty=0/2140 |
| hospitalized_alc_hep | hospitalized_alc_hep | empty | non-empty=0/2140 |
| hospitalized_alc_hep_times | hospitalized_alc_hep_times | empty | non-empty=0/2140 |
| hospitalized_at_enrollment | hospitalized_at_enrollment | empty | non-empty=0/2140 |
| admission_date | admission_date | empty | non-empty=0/2140 |
| liver_score_collected | liver_score_collected | empty | non-empty=0/2140 |
| liver_score_date | liver_score_date | populated | non-empty=1187/2140 |
| meld_score | meld_score | populated | non-empty=1938/2140 |
| child_pugh_score | child_pugh_score | populated | non-empty=1748/2140 |
| lille_score | lille_score | empty | non-empty=0/2140 |
| maddreys_score | maddreys_score | populated | non-empty=1918/2140 |
| tlfb_collected | tlfb_collected | empty | non-empty=0/2140 |
| tlfb_number_drinks | tlfb_number_drinks | populated | non-empty=1710/2140 |
| tlfb_drinking_days | tlfb_drinking_days | populated | non-empty=1706/2140 |
| cases | cases.submitter_id | populated | non-empty=2140/2140 |
| demographics | demographics.submitter_id | populated | non-empty=2140/2140 |
| project_id | project_id | populated | non-empty=2140/2140 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 110  
Physical headers: 106  
DD properties materialized: 106  
DD properties absent: 4  
Materialized but entirely empty: 57  
Physical headers not mapped to DD: 0

### 3.12.7 Machine-generated findings

- EMPTY: 57/106 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 2,140 distinct values in 2,140 non-empty rows.
- BROKEN_FK: 0/4,280 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv

### 3.13.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv |
| DD entity | follow_up |
| Entity category | administrative |
| Study track | rct |
| Source class | unclassified |
| Rows | 834 |
| Physical columns | 106 |
| DD-defined properties | 110 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | cases.submitter_id |
| Primary/row identifier | *submitter_id |

### 3.13.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 834 |
| Distinct primary IDs | 834 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

Rows per subject:

| Rows per subject | Subjects | Share of subjects |
|---|---|---|
| 1 | 10 | 6.8% |
| 2 | 6 | 4.1% |
| 3 | 11 | 7.5% |
| 4 | 16 | 10.9% |
| 5 | 19 | 12.9% |
| 6 | 17 | 11.6% |
| 7 | 26 | 17.7% |
| 8 | 42 | 28.6% |

### 3.13.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | follow_up.type | const | string | 834 | 834 | 0 | 100.0% | 1 | 0.1% | constant=follow_up | follow_up | CONST |
| project_id | follow_up.project_id | const | string | 834 | 834 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | follow_up.submitter_id | id | string | 834 | 834 | 0 | 100.0% | 834 | 100.0% | unique 834/834; duplicates=0 | 11***_0, 11***_3, 11***_7 | UNIQUE |
| cases.submitter_id | follow_up.cases | fk | string | 834 | 834 | 0 | 100.0% | 147 | 17.6% | distinct parents=147; rows/parent median=6.0, max=8 | 11***al, 11***al, 11***al | — |
| demographics.submitter_id | follow_up.demographics | fk | string | 834 | 834 | 0 | 100.0% | 147 | 17.6% | distinct parents=147; rows/parent median=6.0, max=8 | 11***ic, 11***ic, 11***ic | — |
| *days_to_follow_up | follow_up.days_to_follow_up | dayoff | number | 834 | 834 | 0 | 100.0% | 8 | 1.0% | min=0; max=180; negative=0; zero=147; common=0:147, 7:126, 3:121, 14:109, 28:103, 60:83, 90:76, 180:69 | 0, 3, 7 | — |
| admission_date | follow_up.admission_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_culture | follow_up.ascites_culture | const | string | 834 | 117 | 717 | 14.0% | 1 | 0.9% | constant=Not Done | Not Done | CONST,ENUM_UNUSED,SPARSE |
| ascites_culture_result | follow_up.ascites_culture_result | cat | string | 834 | 78 | 756 | 9.4% | 3 | 3.8% | Negative=70 (89.7%); Positive=5 (6.4%); Missing=3 (3.8%); observed/allowed=3/3 | Negative, Positive, Missing | SPARSE |
| ascites_date | follow_up.ascites_date | date | string | 834 | 76 | 758 | 9.1% | 38 | 50.0% | earliest=—; latest=—; invalid=76 | -2, 26, 10 | SPARSE |
| ascites_diagnosis_date | follow_up.ascites_diagnosis_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ascites_organism | follow_up.ascites_organism | cat | string | 834 | 5 | 829 | 0.6% | 5 | 100.0% | Klebsiella pneumoniae=1 (20.0%); Rare WBCs present; No organisms present=1 (20.0%); Staphylococcus hominis No antimicrobial susceptibility to follow *contaminant=1 (20.0%); Aerobic Culture with Gram Klebsiella pneumoniae (A)=1 (20.0%); Aerobic Culture with Gram	 Rare Staphylococcus aureus, Methicillin Resistant Abnormal=1 (20.0%) | Klebsiella pneumoniae, Rare WBCs present; No organism, Staphylococcus hominis No anti | SPARSE,UNIQUE |
| bariatric_surgery | follow_up.bariatric_surgery | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture | follow_up.blood_culture | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_culture_date | follow_up.blood_culture_date | date | string | 834 | 158 | 676 | 18.9% | 52 | 32.9% | earliest=—; latest=—; invalid=158 | -1, 16, 0 | SPARSE |
| blood_culture_result | follow_up.blood_culture_result | cat | string | 834 | 158 | 676 | 18.9% | 2 | 1.3% | Negative=146 (92.4%); Positive=12 (7.6%); observed/allowed=2/2 | Negative, Positive | SPARSE |
| blood_organism | follow_up.blood_organism | text | string | 834 | 12 | 822 | 1.4% | 12 | 100.0% | length min=5; mean=35.1; max=105; blank-string=0 | Klebsiella pneumoniae, Micrococcus species; Comment: , Finegoldia magna | SPARSE,UNIQUE |
| bmi | follow_up.bmi | num | number | 834 | 643 | 191 | 77.1% | 243 | 37.8% | min=13.5; p25=24.1; median=28.1; mean=29.0178; p75=32.9; max=62.1 | 29, 29.4, 31 | — |
| cdc_hiv_risk_factors | follow_up.cdc_hiv_risk_factors | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| child_pugh_score | follow_up.child_pugh_score | num | number | 834 | 716 | 118 | 85.9% | 10 | 1.4% | min=5; p25=8; median=9; mean=9.17318; p75=11; max=14 | 8, 9, 6 | — |
| ct_date | follow_up.ct_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result | follow_up.ct_result | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_finding | follow_up.ct_result_finding | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ct_result_sig | follow_up.ct_result_sig | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| duodenum_ulcer_bleed | follow_up.duodenum_ulcer_bleed | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| duodenum_ulcer_size | follow_up.duodenum_ulcer_size | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy | follow_up.endoscopy | cat | string | 834 | 429 | 405 | 51.4% | 2 | 0.5% | No=374 (87.2%); Yes=55 (12.8%); observed/allowed=2/2 | No, Yes | — |
| endoscopy_date | follow_up.endoscopy_date | date | string | 834 | 18 | 816 | 2.2% | 15 | 83.3% | earliest=—; latest=—; invalid=18 | 0, 7, -3 | SPARSE |
| endoscopy_ulcer_present | follow_up.endoscopy_ulcer_present | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| endoscopy_varices_present | follow_up.endoscopy_varices_present | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| esophageal_ulcer_bleed | follow_up.esophageal_ulcer_bleed | cat | string | 834 | 6 | 828 | 0.7% | 2 | 33.3% | No=4 (66.7%); Yes=2 (33.3%); observed/allowed=2/4 | No, Yes | ENUM_UNUSED,SPARSE |
| esophageal_ulcer_size | follow_up.esophageal_ulcer_size | cat | string | 834 | 6 | 828 | 0.7% | 2 | 33.3% | Large=4 (66.7%); Small=2 (33.3%); observed/allowed=2/5 | Large, Small | ENUM_UNUSED,SPARSE |
| esophageal_varices_bleed | follow_up.esophageal_varices_bleed | cat | string | 834 | 31 | 803 | 3.7% | 3 | 9.7% | No=21 (67.7%); Missing=5 (16.1%); Yes=5 (16.1%); observed/allowed=3/4 | No, Missing, Yes | ENUM_UNUSED,SPARSE |
| esophageal_varices_size | follow_up.esophageal_varices_size | cat | string | 834 | 31 | 803 | 3.7% | 4 | 12.9% | Small=17 (54.8%); Large=7 (22.6%); Medium=6 (19.4%); Missing=1 (3.2%); observed/allowed=4/5 | Small, Medium, Large | ENUM_UNUSED,SPARSE |
| event_type | follow_up.event_type | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_capmed | follow_up.fibro_capmed | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_e | follow_up.fibro_e | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_iqr | follow_up.fibro_iqr | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_probe | follow_up.fibro_probe | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibro_total_number | follow_up.fibro_total_number | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan | follow_up.fibroscan | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| fibroscan_date | follow_up.fibroscan_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_e_iqr | follow_up.firbro_e_iqr | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| firbro_valid_number | follow_up.firbro_valid_number | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gastric_ulcer_bleed | follow_up.gastric_ulcer_bleed | const | string | 834 | 5 | 829 | 0.6% | 1 | 20.0% | constant=No | No | CONST,ENUM_UNUSED,SPARSE |
| gastric_ulcer_size | follow_up.gastric_ulcer_size | cat | string | 834 | 5 | 829 | 0.6% | 2 | 40.0% | Small=4 (80.0%); Large=1 (20.0%); observed/allowed=2/5 | Small, Large | ENUM_UNUSED,SPARSE |
| gastric_varices_bleed | follow_up.gastric_varices_bleed | const | string | 834 | 2 | 832 | 0.2% | 1 | 50.0% | constant=No | No | CONST,ENUM_UNUSED,SPARSE |
| gastric_varices_size | follow_up.gastric_varices_size | const | string | 834 | 2 | 832 | 0.2% | 1 | 50.0% | constant=Missing | Missing | CONST,ENUM_UNUSED,SPARSE |
| height | follow_up.height | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_carcinoma | follow_up.hep_carcinoma | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_enceph | follow_up.hep_enceph | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hep_enceph_diagnosis_date | follow_up.hep_enceph_diagnosis_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hepcar_diagnosis_date | follow_up.hepcar_diagnosis_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_alc_hep | follow_up.hospitalized_alc_hep | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_alc_hep_times | follow_up.hospitalized_alc_hep_times | num | number | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| hospitalized_at_enrollment | follow_up.hospitalized_at_enrollment | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| infection_screen_date | follow_up.infection_screen_date | date | string | 834 | 196 | 638 | 23.5% | 62 | 31.6% | earliest=—; latest=—; invalid=196 | -1, 16, -2 | — |
| infection_screen_done | follow_up.infection_screen_done | cat | string | 834 | 429 | 405 | 51.4% | 2 | 0.5% | No=234 (54.5%); Yes=195 (45.5%); observed/allowed=2/2 | Yes, No | — |
| lille_score | follow_up.lille_score | num | number | 834 | 120 | 714 | 14.4% | 110 | 91.7% | min=0.005; p25=0.11675; median=0.21; mean=0.354833; p75=0.60675; max=0.994 | 0.234, 0.011, 0.315 | SPARSE |
| liver_abdomen_imaging | follow_up.liver_abdomen_imaging | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_imaging_type | follow_up.liver_imaging_type | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_collected | follow_up.liver_score_collected | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_score_date | follow_up.liver_score_date | date | string | 834 | 782 | 52 | 93.8% | 118 | 15.1% | earliest=—; latest=—; invalid=782 | 0, 1, 7 | — |
| liver_transplant | follow_up.liver_transplant | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| liver_transplant_date | follow_up.liver_transplant_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| maddreys_score | follow_up.maddreys_score | num | number | 834 | 736 | 98 | 88.2% | 530 | 72.0% | min=-7.1; p25=16.1; median=35.4; mean=41.0643; p75=57.225; max=205.9 | 28, 17.1, 1.7 | NEG |
| medical_info_collected | follow_up.medical_info_collected | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| meld_score | follow_up.meld_score | num | number | 834 | 770 | 64 | 92.3% | 41 | 5.3% | min=6; p25=17; median=22; mean=21.6095; p75=26; max=50 | 21, 19, 11 | — |
| mri_date | follow_up.mri_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_finding | follow_up.mri_finding | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_result | follow_up.mri_result | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| mri_sig | follow_up.mri_sig | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_date | follow_up.other_imaging_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_finding | follow_up.other_imaging_finding | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_result | follow_up.other_imaging_result | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_sig | follow_up.other_imaging_sig | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| other_imaging_type | follow_up.other_imaging_type | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| portal_hypertensive_gastropathy | follow_up.portal_hypertensive_gastropathy | cat | string | 834 | 37 | 797 | 4.4% | 5 | 13.5% | Yes, Mild=18 (48.6%); Yes, Moderate=10 (27.0%); Missing=6 (16.2%); Yes, Severe=2 (5.4%); Yes, Unknown severity=1 (2.7%); observed/allowed=5/7 | Missing, Yes, Mild, Yes, Moderate | ENUM_UNUSED,SPARSE |
| soc_collected | follow_up.soc_collected | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test | follow_up.stool_test | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_date | follow_up.stool_test_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| stool_test_finding | follow_up.stool_test_finding | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_collected | follow_up.tlfb_collected | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| tlfb_drinking_days | follow_up.tlfb_drinking_days | num | number | 834 | 381 | 453 | 45.7% | 30 | 7.9% | min=0; p25=0; median=0; mean=6.33071; p75=10; max=30 | 13, 3, 0 | — |
| tlfb_number_drinks | follow_up.tlfb_number_drinks | num | number | 834 | 383 | 451 | 45.9% | 105 | 27.4% | min=0; p25=0; median=0; mean=55.3773; p75=64.5; max=1200 | 106, 24, 0 | — |
| ultrasound_date | follow_up.ultrasound_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_finding | follow_up.ultrasound_finding | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result | follow_up.ultrasound_result | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| ultrasound_result_sig | follow_up.ultrasound_result_sig | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| urine_culture | follow_up.urine_culture | const | string | 834 | 97 | 737 | 11.6% | 1 | 1.0% | constant=Not Done | Not Done | CONST,ENUM_UNUSED,SPARSE |
| urine_culture_date | follow_up.urine_culture_date | date | string | 834 | 97 | 737 | 11.6% | 43 | 44.3% | earliest=—; latest=—; invalid=97 | 18, 6, 3 | SPARSE |
| urine_culture_fungal_result | follow_up.urine_culture_fungal_result | cat | string | 834 | 32 | 802 | 3.8% | 3 | 9.4% | No; Positive for other organisms only=27 (84.4%); Yes=4 (12.5%); Missing=1 (3.1%); observed/allowed=3/4 | Yes, No; Positive for other organis, Missing | ENUM_UNUSED,SPARSE |
| urine_culture_organism | follow_up.urine_culture_organism | text | string | 834 | 32 | 802 | 3.8% | 30 | 93.8% | length min=3; mean=39.2; max=148; blank-string=0 | Candida albicans, Enterococcus faecium, Candida , Klebsiella pneumoniae, Enteroc | SPARSE |
| urine_culture_result | follow_up.urine_culture_result | cat | string | 834 | 98 | 736 | 11.8% | 3 | 3.1% | Negative=64 (65.3%); Positive=32 (32.7%); Missing=2 (2.0%); observed/allowed=3/3 | Negative, Positive, Missing | SPARSE |
| varices | follow_up.varices | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| varices_diagnosis_date | follow_up.varices_diagnosis_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| visit_day | follow_up.visit_day | dayoff | number | 834 | 834 | 0 | 100.0% | 8 | 1.0% | min=0; max=180; negative=0; zero=147; common=0:147, 7:126, 3:121, 14:109, 28:103, 60:83, 90:76, 180:69 | 0, 3, 7 | ENUM_UNUSED |
| weight | follow_up.weight | num | number | 834 | 703 | 131 | 84.3% | 441 | 62.7% | min=33.5; p25=71.6; median=84.3; mean=88.1123; p75=99.75; max=207.6 | 105.2, 106.6, 112.6 | — |
| xray | follow_up.xray | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_date | follow_up.xray_date | date | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_findings | follow_up.xray_findings | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_impression | follow_up.xray_impression | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_infiltrates | follow_up.xray_infiltrates | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_last_4_weeks | follow_up.xray_last_4_weeks | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_normal | follow_up.xray_normal | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| xray_pleural_effusion | follow_up.xray_pleural_effusion | cat | string | 834 | 0 | 834 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.13.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 7 |
| EMPTY | 65 |
| ENUM_UNUSED | 13 |
| NEG | 1 |
| SPARSE | 88 |
| UNIQUE | 3 |

### 3.13.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| cases.submitter_id | case.submitter_id | 834 | 147 | 834 | 0 | 100.0% | distinct parents=147; rows/parent median=6.0, max=8 |
| demographics.submitter_id | demographic.submitter_id | 834 | 147 | 834 | 0 | 100.0% | distinct parents=147; rows/parent median=6.0, max=8 |

### 3.13.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=834/834 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=834/834 |
| days_to_follow_up | *days_to_follow_up | populated | non-empty=834/834 |
| event_type | event_type | empty | non-empty=0/834 |
| visit_day | visit_day | populated | non-empty=834/834 |
| cdc_hiv_risk_factors | cdc_hiv_risk_factors | empty | non-empty=0/834 |
| height | height | empty | non-empty=0/834 |
| weight | weight | populated | non-empty=703/834 |
| bmi | bmi | populated | non-empty=643/834 |
| soc_collected | soc_collected | empty | non-empty=0/834 |
| infection_screen_done | infection_screen_done | populated | non-empty=429/834 |
| infection_screen_date | infection_screen_date | populated | non-empty=196/834 |
| blood_culture | blood_culture | empty | non-empty=0/834 |
| blood_culture_result | blood_culture_result | populated | non-empty=158/834 |
| blood_organism | blood_organism | populated | non-empty=12/834 |
| blood_culture_date | blood_culture_date | populated | non-empty=158/834 |
| urine_culture | urine_culture | populated | non-empty=97/834 |
| urine_culture_result | urine_culture_result | populated | non-empty=98/834 |
| urine_culture_organism | urine_culture_organism | populated | non-empty=32/834 |
| urine_culture_date | urine_culture_date | populated | non-empty=97/834 |
| urine_culture_fungal_result | urine_culture_fungal_result | populated | non-empty=32/834 |
| ascites_culture | ascites_culture | populated | non-empty=117/834 |
| ascites_culture_result | ascites_culture_result | populated | non-empty=78/834 |
| ascites_organism | ascites_organism | populated | non-empty=5/834 |
| ascites_date | ascites_date | populated | non-empty=76/834 |
| xray | xray | empty | non-empty=0/834 |
| xray_last_4_weeks | xray_last_4_weeks | empty | non-empty=0/834 |
| xray_date | xray_date | empty | non-empty=0/834 |
| xray_infiltrates | xray_infiltrates | empty | non-empty=0/834 |
| xray_impression | xray_impression | empty | non-empty=0/834 |
| xray_pleural_effusion | xray_pleural_effusion | empty | non-empty=0/834 |
| xray_normal | xray_normal | empty | non-empty=0/834 |
| xray_findings | xray_findings | empty | non-empty=0/834 |
| endoscopy | endoscopy | populated | non-empty=429/834 |
| endoscopy_date | endoscopy_date | populated | non-empty=18/834 |
| endoscopy_varices_present | endoscopy_varices_present | empty | non-empty=0/834 |
| esophageal_varices_size | esophageal_varices_size | populated | non-empty=31/834 |
| esophageal_varices_bleed | esophageal_varices_bleed | populated | non-empty=31/834 |
| gastric_varices_size | gastric_varices_size | populated | non-empty=2/834 |
| gastric_varices_bleed | gastric_varices_bleed | populated | non-empty=2/834 |
| portal_hypertensive_gastropathy | portal_hypertensive_gastropathy | populated | non-empty=37/834 |
| endoscopy_ulcer_present | endoscopy_ulcer_present | empty | non-empty=0/834 |
| esophageal_ulcer_size | esophageal_ulcer_size | populated | non-empty=6/834 |
| esophageal_ulcer_bleed | esophageal_ulcer_bleed | populated | non-empty=6/834 |
| gastric_ulcer_size | gastric_ulcer_size | populated | non-empty=5/834 |
| gastric_ulcer_bleed | gastric_ulcer_bleed | populated | non-empty=5/834 |
| duodenum_ulcer_size | duodenum_ulcer_size | empty | non-empty=0/834 |
| duodenum_ulcer_bleed | duodenum_ulcer_bleed | empty | non-empty=0/834 |
| fibroscan | fibroscan | empty | non-empty=0/834 |
| fibroscan_date | fibroscan_date | empty | non-empty=0/834 |
| fibro_capmed | fibro_capmed | empty | non-empty=0/834 |
| fibro_iqr | fibro_iqr | empty | non-empty=0/834 |
| fibro_e | fibro_e | empty | non-empty=0/834 |
| firbro_e_iqr | firbro_e_iqr | empty | non-empty=0/834 |
| fibro_probe | fibro_probe | empty | non-empty=0/834 |
| firbro_valid_number | firbro_valid_number | empty | non-empty=0/834 |
| fibro_total_number | fibro_total_number | empty | non-empty=0/834 |
| liver_abdomen_imaging | liver_abdomen_imaging | empty | non-empty=0/834 |
| liver_imaging_type | liver_imaging_type | empty | non-empty=0/834 |
| ultrasound_date | ultrasound_date | empty | non-empty=0/834 |
| ultrasound_result | ultrasound_result | empty | non-empty=0/834 |
| ultrasound_result_sig | ultrasound_result_sig | empty | non-empty=0/834 |
| ultrasound_finding | ultrasound_finding | empty | non-empty=0/834 |
| ct_date | ct_date | empty | non-empty=0/834 |
| ct_result | ct_result | empty | non-empty=0/834 |
| ct_result_sig | ct_result_sig | empty | non-empty=0/834 |
| ct_result_finding | ct_result_finding | empty | non-empty=0/834 |
| mri_date | mri_date | empty | non-empty=0/834 |
| mri_result | mri_result | empty | non-empty=0/834 |
| mri_sig | mri_sig | empty | non-empty=0/834 |
| mri_finding | mri_finding | empty | non-empty=0/834 |
| other_imaging_date | other_imaging_date | empty | non-empty=0/834 |
| other_imaging_type | other_imaging_type | empty | non-empty=0/834 |
| other_imaging_result | other_imaging_result | empty | non-empty=0/834 |
| other_imaging_sig | other_imaging_sig | empty | non-empty=0/834 |
| other_imaging_finding | other_imaging_finding | empty | non-empty=0/834 |
| medical_info_collected | medical_info_collected | empty | non-empty=0/834 |
| ascites_diagnosis_date | ascites_diagnosis_date | empty | non-empty=0/834 |
| hep_enceph | hep_enceph | empty | non-empty=0/834 |
| hep_enceph_diagnosis_date | hep_enceph_diagnosis_date | empty | non-empty=0/834 |
| varices | varices | empty | non-empty=0/834 |
| varices_diagnosis_date | varices_diagnosis_date | empty | non-empty=0/834 |
| hep_carcinoma | hep_carcinoma | empty | non-empty=0/834 |
| hepcar_diagnosis_date | hepcar_diagnosis_date | empty | non-empty=0/834 |
| liver_transplant | liver_transplant | empty | non-empty=0/834 |
| liver_transplant_date | liver_transplant_date | empty | non-empty=0/834 |
| stool_test | stool_test | empty | non-empty=0/834 |
| stool_test_finding | stool_test_finding | empty | non-empty=0/834 |
| stool_test_date | stool_test_date | empty | non-empty=0/834 |
| bariatric_surgery | bariatric_surgery | empty | non-empty=0/834 |
| hospitalized_alc_hep | hospitalized_alc_hep | empty | non-empty=0/834 |
| hospitalized_alc_hep_times | hospitalized_alc_hep_times | empty | non-empty=0/834 |
| hospitalized_at_enrollment | hospitalized_at_enrollment | empty | non-empty=0/834 |
| admission_date | admission_date | empty | non-empty=0/834 |
| liver_score_collected | liver_score_collected | empty | non-empty=0/834 |
| liver_score_date | liver_score_date | populated | non-empty=782/834 |
| meld_score | meld_score | populated | non-empty=770/834 |
| child_pugh_score | child_pugh_score | populated | non-empty=716/834 |
| lille_score | lille_score | populated | non-empty=120/834 |
| maddreys_score | maddreys_score | populated | non-empty=736/834 |
| tlfb_collected | tlfb_collected | empty | non-empty=0/834 |
| tlfb_number_drinks | tlfb_number_drinks | populated | non-empty=383/834 |
| tlfb_drinking_days | tlfb_drinking_days | populated | non-empty=381/834 |
| cases | cases.submitter_id | populated | non-empty=834/834 |
| demographics | demographics.submitter_id | populated | non-empty=834/834 |
| project_id | project_id | populated | non-empty=834/834 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 110  
Physical headers: 106  
DD properties materialized: 106  
DD properties absent: 4  
Materialized but entirely empty: 65  
Physical headers not mapped to DD: 0

### 3.13.7 Machine-generated findings

- EMPTY: 65/106 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 834 distinct values in 834 non-empty rows.
- BROKEN_FK: 0/1,668 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_lab_PI_DCC_data_release_v2-1-0_minor.tsv

### 3.14.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_lab_PI_DCC_data_release_v2-1-0_minor.tsv |
| DD entity | lab |
| Entity category | administrative |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 11 |
| Physical columns | 20 |
| DD-defined properties | 24 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.14.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 11 |
| Distinct primary IDs | 11 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.14.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | lab.type | const | string | 11 | 11 | 0 | 100.0% | 1 | 9.1% | constant=lab | lab | CONST |
| project_id | lab.project_id | const | string | 11 | 11 | 0 | 100.0% | 1 | 9.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | lab.submitter_id | id | string | 11 | 11 | 0 | 100.0% | 11 | 100.0% | unique 11/11; duplicates=0 | la***_1, la***_2, la***_3 | UNIQUE |
| *projects.code | lab.projects | const | string | 11 | 11 | 0 | 100.0% | 1 | 9.1% | constant=AlcHepNet | AlcHepNet | CONST |
| *name_of_institute | lab.name_of_institute | text | string | 11 | 11 | 0 | 100.0% | 10 | 90.9% | length min=12; mean=22.2; max=34; blank-string=0 | University of Massachusetts, Cleveland Clinic, Indiana University | — |
| PI_email | lab.PI_email | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| PI_name | lab.PI_name | text | string | 11 | 11 | 0 | 100.0% | 11 | 100.0% | length min=4; mean=7.5; max=13; blank-string=0 | Szabo, Nagy, Liangpunsakul | UNIQUE |
| address | lab.address | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| center_type | lab.center_type | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| code | lab.code | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| contact_email | lab.contact_email | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| contact_name | lab.contact_name | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| description_of_lab | lab.description_of_lab | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| keyword_name | lab.keyword_name | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| name | lab.name | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| namespace | lab.namespace | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| note | lab.note | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| short_name | lab.short_name | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| translational_projects_title | lab.translational_projects_title | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| url_of_lab_website | lab.url_of_lab_website | cat | string | 11 | 0 | 11 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.14.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 14 |
| SPARSE | 14 |
| UNIQUE | 2 |

### 3.14.5 Relationship integrity

No physical `*.submitter_id` foreign-key columns detected.

### 3.14.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=11/11 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=11/11 |
| code | code | empty | non-empty=0/11 |
| namespace | namespace | empty | non-empty=0/11 |
| name | name | empty | non-empty=0/11 |
| short_name | short_name | empty | non-empty=0/11 |
| center_type | center_type | empty | non-empty=0/11 |
| keyword_name | keyword_name | empty | non-empty=0/11 |
| PI_name | PI_name | populated | non-empty=11/11 |
| PI_email | PI_email | empty | non-empty=0/11 |
| contact_name | contact_name | empty | non-empty=0/11 |
| contact_email | contact_email | empty | non-empty=0/11 |
| description_of_lab | description_of_lab | empty | non-empty=0/11 |
| name_of_institute | *name_of_institute | populated | non-empty=11/11 |
| url_of_lab_website | url_of_lab_website | empty | non-empty=0/11 |
| address | address | empty | non-empty=0/11 |
| note | note | empty | non-empty=0/11 |
| translational_projects_title | translational_projects_title | empty | non-empty=0/11 |
| projects | *projects.code | populated | non-empty=11/11 |
| project_id | project_id | populated | non-empty=11/11 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 24  
Physical headers: 20  
DD properties materialized: 20  
DD properties absent: 4  
Materialized but entirely empty: 14  
Physical headers not mapped to DD: 0

### 3.14.7 Machine-generated findings

- EMPTY: 14/20 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 11 distinct values in 11 non-empty rows.

---

## mod_molecular-test_liangpunsakul-orm1_DCC_data_release_v2-1-0_minor.tsv

### 3.15.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_molecular-test_liangpunsakul-orm1_DCC_data_release_v2-1-0_minor.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 164 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.15.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 164 |
| Distinct primary IDs | 164 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.15.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 164 | 164 | 0 | 100.0% | 1 | 0.6% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 164 | 164 | 0 | 100.0% | 1 | 0.6% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 164 | 164 | 0 | 100.0% | 164 | 100.0% | unique 164/164; duplicates=0 | 11***M1, 11***M1, 11***M1 | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 164 | 164 | 0 | 100.0% | 164 | 100.0% | distinct parents=164; rows/parent median=1.0, max=1 | 11***04, 11***05, 11***06 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 164 | 164 | 0 | 100.0% | 164 | 100.0% | distinct parents=164; rows/parent median=1.0, max=1 | 11***_0, 11***_0, 11***_0 | UNIQUE |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 164 | 164 | 0 | 100.0% | 1 | 0.6% | constant=ORM1 | ORM1 | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 164 | 0 | 164 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 164 | 164 | 0 | 100.0% | 1 | 0.6% | constant=µg/ml | µg/ml | CONST |
| test_value | molecular_test.test_value | num | string | 164 | 164 | 0 | 100.0% | 154 | 93.9% | min=109.494; p25=454.114; median=651.266; mean=747.7; p75=988.608; max=2036.08 | 479.1139240506330, 574.0506329113920, 550.0000000000000 | — |

### 3.15.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 3 |

### 3.15.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 164 | 164 | 164 | 0 | 100.0% | distinct parents=164; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 164 | 164 | 164 | 0 | 100.0% | distinct parents=164; rows/parent median=1.0, max=1 |

### 3.15.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=164/164 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=164/164 |
| gene_symbol | gene_symbol | empty | non-empty=0/164 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/164 |
| test_result | test_result | empty | non-empty=0/164 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/164 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/164 |
| days_to_test | days_to_test | empty | non-empty=0/164 |
| laboratory_test | laboratory_test | populated | non-empty=164/164 |
| test_value | test_value | populated | non-empty=164/164 |
| test_unit | test_unit | populated | non-empty=164/164 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=164/164 |
| aliquots | aliquots.submitter_id | populated | non-empty=164/164 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=164/164 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.15.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 164 distinct values in 164 non-empty rows.
- BROKEN_FK: 0/328 populated foreign-key rows are unmatched across detected parent mappings.

---

## mod_molecular-test_szabo_DCC_data_release_v2-1-0_fixed_duplicates_minor.tsv

### 3.16.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | mod_molecular-test_szabo_DCC_data_release_v2-1-0_fixed_duplicates_minor.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 993 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.16.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 993 |
| Distinct primary IDs | 993 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.16.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 993 | 993 | 0 | 100.0% | 1 | 0.1% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 993 | 993 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 993 | 993 | 0 | 100.0% | 993 | 100.0% | unique 993/993; duplicates=0 | 11***bo, 11***_1, 11***bo | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 993 | 993 | 0 | 100.0% | 993 | 100.0% | distinct parents=993; rows/parent median=1.0, max=1 | 11***04, 11***05, 11***05 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 993 | 993 | 0 | 100.0% | 648 | 65.3% | distinct parents=648; rows/parent median=2.0, max=3 | 11***28, 11***90, 11***80 | — |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 993 | 993 | 0 | 100.0% | 1 | 0.1% | constant=IL-1RA | IL-1RA | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 993 | 0 | 993 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 993 | 993 | 0 | 100.0% | 1 | 0.1% | constant=pg/mL | pg/mL | CONST |
| test_value | molecular_test.test_value | num | string | 993 | 993 | 0 | 100.0% | 451 | 45.4% | min=0.35; p25=12.12; median=34.38; mean=5998.57; p75=155.59; max=393175 | 2.65, 4.49, 19.37 | — |

### 3.16.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 2 |

### 3.16.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 993 | 993 | 993 | 0 | 100.0% | distinct parents=993; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 993 | 648 | 993 | 0 | 100.0% | distinct parents=648; rows/parent median=2.0, max=3 |

### 3.16.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=993/993 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=993/993 |
| gene_symbol | gene_symbol | empty | non-empty=0/993 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/993 |
| test_result | test_result | empty | non-empty=0/993 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/993 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/993 |
| days_to_test | days_to_test | empty | non-empty=0/993 |
| laboratory_test | laboratory_test | populated | non-empty=993/993 |
| test_value | test_value | populated | non-empty=993/993 |
| test_unit | test_unit | populated | non-empty=993/993 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=993/993 |
| aliquots | aliquots.submitter_id | populated | non-empty=993/993 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=993/993 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.16.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 993 distinct values in 993 non-empty rows.
- BROKEN_FK: 0/1,986 populated foreign-key rows are unmatched across detected parent mappings.

---

## molecular-test_liangpunsakul-orm1_part2_DCC_data_release_v2-1-0.tsv

### 3.17.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | molecular-test_liangpunsakul-orm1_part2_DCC_data_release_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 40 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.17.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 40 |
| Distinct primary IDs | 40 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.17.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 40 | 40 | 0 | 100.0% | 1 | 2.5% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 40 | 40 | 0 | 100.0% | 1 | 2.5% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 40 | 40 | 0 | 100.0% | 40 | 100.0% | unique 40/40; duplicates=0 | 11***M1, 11***M1, 11***M1 | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 40 | 40 | 0 | 100.0% | 40 | 100.0% | distinct parents=40; rows/parent median=1.0, max=1 | 11***06, 11***06, 11***03 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 40 | 40 | 0 | 100.0% | 40 | 100.0% | distinct parents=40; rows/parent median=1.0, max=1 | 11***_0, 11***_0, 11***_0 | UNIQUE |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 40 | 40 | 0 | 100.0% | 1 | 2.5% | constant=ORM1 | ORM1 | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 40 | 0 | 40 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 40 | 40 | 0 | 100.0% | 1 | 2.5% | constant=µg/ml | µg/ml | CONST |
| test_value | molecular_test.test_value | num | string | 40 | 40 | 0 | 100.0% | 39 | 97.5% | min=193.727; p25=384.864; median=610.545; mean=602.955; p75=774.864; max=1269.18 | 791.9090909090909, 437.3636363636364, 860.0909090909091 | — |

### 3.17.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 3 |

### 3.17.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 40 | 40 | 40 | 0 | 100.0% | distinct parents=40; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 40 | 40 | 40 | 0 | 100.0% | distinct parents=40; rows/parent median=1.0, max=1 |

### 3.17.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=40/40 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=40/40 |
| gene_symbol | gene_symbol | empty | non-empty=0/40 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/40 |
| test_result | test_result | empty | non-empty=0/40 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/40 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/40 |
| days_to_test | days_to_test | empty | non-empty=0/40 |
| laboratory_test | laboratory_test | populated | non-empty=40/40 |
| test_value | test_value | populated | non-empty=40/40 |
| test_unit | test_unit | populated | non-empty=40/40 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=40/40 |
| aliquots | aliquots.submitter_id | populated | non-empty=40/40 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=40/40 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.17.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 40 distinct values in 40 non-empty rows.
- BROKEN_FK: 0/80 populated foreign-key rows are unmatched across detected parent mappings.

---

## molecular-test_mehal-ace_DCC_data_release_v2-1-0.tsv

### 3.18.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | molecular-test_mehal-ace_DCC_data_release_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 192 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.18.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 192 |
| Distinct primary IDs | 192 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.18.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | unique 192/192; duplicates=0 | 11***CE, 11***CE, 11***CE | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 | 11***07, 11***07, 11***07 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 | 11***_0, 11***28, 11***_0 | UNIQUE |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=ACE | ACE | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=µg/l | µg/l | CONST |
| test_value | molecular_test.test_value | num | string | 192 | 192 | 0 | 100.0% | 186 | 96.9% | min=4.1919; p25=47.5614; median=92.5519; mean=129.722; p75=154.102; max=759.585 | 119.6379630058864, 90.3579602047552, 127.0522079030392 | — |

### 3.18.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 3 |

### 3.18.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 192 | 192 | 192 | 0 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 192 | 192 | 192 | 0 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 |

### 3.18.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=192/192 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=192/192 |
| gene_symbol | gene_symbol | empty | non-empty=0/192 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/192 |
| test_result | test_result | empty | non-empty=0/192 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/192 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/192 |
| days_to_test | days_to_test | empty | non-empty=0/192 |
| laboratory_test | laboratory_test | populated | non-empty=192/192 |
| test_value | test_value | populated | non-empty=192/192 |
| test_unit | test_unit | populated | non-empty=192/192 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=192/192 |
| aliquots | aliquots.submitter_id | populated | non-empty=192/192 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=192/192 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.18.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 192 distinct values in 192 non-empty rows.
- BROKEN_FK: 0/384 populated foreign-key rows are unmatched across detected parent mappings.

---

## molecular-test_mehal-renin_DCC_data_release_v2-1-0.tsv

### 3.19.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | molecular-test_mehal-renin_DCC_data_release_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 192 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.19.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 192 |
| Distinct primary IDs | 192 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.19.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | unique 192/192; duplicates=0 | 11***in, 11***in, 11***in | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 | 11***07, 11***07, 11***07 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 192 | 192 | 0 | 100.0% | 192 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 | 11***_0, 11***28, 11***_0 | UNIQUE |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=Renin | Renin | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 192 | 0 | 192 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 192 | 192 | 0 | 100.0% | 1 | 0.5% | constant=ng/mL | ng/mL | CONST |
| test_value | molecular_test.test_value | num | string | 192 | 192 | 0 | 100.0% | 184 | 95.8% | min=0; p25=0.756332; median=1.58135; mean=2.91277; p75=2.86196; max=37.5106 | 3.4668358835575916, 6.088055546298103, 10.802418819652639 | — |

### 3.19.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 3 |

### 3.19.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 192 | 192 | 192 | 0 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 192 | 192 | 192 | 0 | 100.0% | distinct parents=192; rows/parent median=1.0, max=1 |

### 3.19.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=192/192 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=192/192 |
| gene_symbol | gene_symbol | empty | non-empty=0/192 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/192 |
| test_result | test_result | empty | non-empty=0/192 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/192 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/192 |
| days_to_test | days_to_test | empty | non-empty=0/192 |
| laboratory_test | laboratory_test | populated | non-empty=192/192 |
| test_value | test_value | populated | non-empty=192/192 |
| test_unit | test_unit | populated | non-empty=192/192 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=192/192 |
| aliquots | aliquots.submitter_id | populated | non-empty=192/192 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=192/192 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.19.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 192 distinct values in 192 non-empty rows.
- BROKEN_FK: 0/384 populated foreign-key rows are unmatched across detected parent mappings.

---

## molecular-test_nagy-urine_DCC_data_release_v2-1-0.tsv

### 3.20.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | molecular-test_nagy-urine_DCC_data_release_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 1160 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.20.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 1160 |
| Distinct primary IDs | 1160 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.20.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 1160 | 1160 | 0 | 100.0% | 1 | 0.1% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 1160 | 1160 | 0 | 100.0% | 1 | 0.1% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 1160 | 1160 | 0 | 100.0% | 1160 | 100.0% | unique 1160/1160; duplicates=0 | 11***ne, 11***M1, 11***18 | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 1160 | 1160 | 0 | 100.0% | 232 | 20.0% | distinct parents=232; rows/parent median=5.0, max=5 | 11***07, 11***07, 11***06 | — |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 1160 | 1160 | 0 | 100.0% | 232 | 20.0% | distinct parents=232; rows/parent median=5.0, max=5 | 11***_0, 11***_7, 11***28 | — |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | cat | string | 1160 | 1160 | 0 | 100.0% | 5 | 0.4% | Urine Creatinine=232 (20.0%); Urine KIM-1=232 (20.0%); Urine IL-18=232 (20.0%); Urine L-FABP=232 (20.0%); Urine NGAL=232 (20.0%); observed/allowed=5/95 | Urine Creatinine, Urine KIM-1, Urine IL-18 | ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 1160 | 0 | 1160 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | cat | string | 1160 | 1160 | 0 | 100.0% | 3 | 0.3% | ng/mL=464 (40.0%); pg/mL=464 (40.0%); mg/dL=232 (20.0%) | mg/dL, ng/mL, pg/mL | — |
| test_value | molecular_test.test_value | num | string | 1160 | 1129 | 31 | 97.3% | 1122 | 99.4% | min=0.0157902; p25=16.7506; median=91.6801; mean=3606.99; p75=273.505; max=338210 | 78.55672874019231, 1.216930925139896, 73.3436864230882 | — |

### 3.20.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 2 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 1 |

### 3.20.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 1160 | 232 | 1160 | 0 | 100.0% | distinct parents=232; rows/parent median=5.0, max=5 |
| *follow_ups.submitter_id | follow_up.submitter_id | 1160 | 232 | 1160 | 0 | 100.0% | distinct parents=232; rows/parent median=5.0, max=5 |

### 3.20.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=1160/1160 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=1160/1160 |
| gene_symbol | gene_symbol | empty | non-empty=0/1160 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/1160 |
| test_result | test_result | empty | non-empty=0/1160 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/1160 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/1160 |
| days_to_test | days_to_test | empty | non-empty=0/1160 |
| laboratory_test | laboratory_test | populated | non-empty=1160/1160 |
| test_value | test_value | populated | non-empty=1129/1160 |
| test_unit | test_unit | populated | non-empty=1160/1160 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=1160/1160 |
| aliquots | aliquots.submitter_id | populated | non-empty=1160/1160 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=1160/1160 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.20.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 1,160 distinct values in 1,160 non-empty rows.
- BROKEN_FK: 0/2,320 populated foreign-key rows are unmatched across detected parent mappings.

---

## molecular-test_schnabl_DCC_data_release_v2-1-0.tsv

### 3.21.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | molecular-test_schnabl_DCC_data_release_v2-1-0.tsv |
| DD entity | molecular_test |
| Entity category | clinical |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 297 |
| Physical columns | 14 |
| DD-defined properties | 19 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.21.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 297 |
| Distinct primary IDs | 297 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.21.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | molecular_test.type | const | string | 297 | 297 | 0 | 100.0% | 1 | 0.3% | constant=molecular_test | molecular_test | CONST |
| project_id | molecular_test.project_id | const | string | 297 | 297 | 0 | 100.0% | 1 | 0.3% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | molecular_test.submitter_id | id | string | 297 | 297 | 0 | 100.0% | 297 | 100.0% | unique 297/297; duplicates=0 | 11***bl, 11***bl, 11***bl | UNIQUE |
| aliquots.submitter_id | molecular_test.aliquots | fk | string | 297 | 297 | 0 | 100.0% | 297 | 100.0% | distinct parents=297; rows/parent median=1.0, max=1 | 11***02, 11***02, 11***02 | UNIQUE |
| *follow_ups.submitter_id | molecular_test.follow_ups | fk | string | 297 | 297 | 0 | 100.0% | 297 | 100.0% | distinct parents=297; rows/parent median=1.0, max=1 | 11***_0, 11***_0, 11***_0 | UNIQUE |
| blood_test_normal_range_lower | molecular_test.blood_test_normal_range_lower | num | number | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| blood_test_normal_range_upper | molecular_test.blood_test_normal_range_upper | num | number | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| days_to_test | molecular_test.days_to_test | dayoff | number | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| gene_symbol | molecular_test.gene_symbol | cat | string | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| laboratory_test | molecular_test.laboratory_test | const | string | 297 | 297 | 0 | 100.0% | 1 | 0.3% | constant=AhR Activity | AhR Activity | CONST,ENUM_UNUSED |
| molecular_analysis_method | molecular_test.molecular_analysis_method | cat | string | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_result | molecular_test.test_result | cat | string | 297 | 0 | 297 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| test_unit | molecular_test.test_unit | const | string | 297 | 297 | 0 | 100.0% | 1 | 0.3% | constant=fold change | fold change | CONST |
| test_value | molecular_test.test_value | num | string | 297 | 297 | 0 | 100.0% | 295 | 99.3% | min=0.496024; p25=0.927134; median=1.27071; mean=1.53731; p75=1.87794; max=4.92945 | 3.837012925580739, 1.1447189908725424, 1.4489707450279787 | — |

### 3.21.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 4 |
| EMPTY | 6 |
| ENUM_UNUSED | 1 |
| SPARSE | 6 |
| UNIQUE | 3 |

### 3.21.5 Relationship integrity

| Physical FK column | Target entity/key | Populated | Distinct FK values | Matched | Unmatched | Match rate | Multiplicity summary |
|---|---|---|---|---|---|---|---|
| aliquots.submitter_id | aliquot.submitter_id | 297 | 297 | 297 | 0 | 100.0% | distinct parents=297; rows/parent median=1.0, max=1 |
| *follow_ups.submitter_id | follow_up.submitter_id | 297 | 297 | 297 | 0 | 100.0% | distinct parents=297; rows/parent median=1.0, max=1 |

### 3.21.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=297/297 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=297/297 |
| gene_symbol | gene_symbol | empty | non-empty=0/297 |
| molecular_analysis_method | molecular_analysis_method | empty | non-empty=0/297 |
| test_result | test_result | empty | non-empty=0/297 |
| blood_test_normal_range_lower | blood_test_normal_range_lower | empty | non-empty=0/297 |
| blood_test_normal_range_upper | blood_test_normal_range_upper | empty | non-empty=0/297 |
| days_to_test | days_to_test | empty | non-empty=0/297 |
| laboratory_test | laboratory_test | populated | non-empty=297/297 |
| test_value | test_value | populated | non-empty=297/297 |
| test_unit | test_unit | populated | non-empty=297/297 |
| follow_ups | *follow_ups.submitter_id | populated | non-empty=297/297 |
| aliquots | aliquots.submitter_id | populated | non-empty=297/297 |
| labs | — | absent | not materialized in this physical file |
| project_id | project_id | populated | non-empty=297/297 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 19  
Physical headers: 14  
DD properties materialized: 14  
DD properties absent: 5  
Materialized but entirely empty: 6  
Physical headers not mapped to DD: 0

### 3.21.7 Machine-generated findings

- EMPTY: 6/14 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 297 distinct values in 297 non-empty rows.
- BROKEN_FK: 0/594 populated foreign-key rows are unmatched across detected parent mappings.

---

## study_DCC_data_release_v2-1-0.tsv

### 3.22.1 Identity and grain

| Property | Generated or source-backed value |
|---|---|
| Physical file(s) | study_DCC_data_release_v2-1-0.tsv |
| DD entity | study |
| Entity category | administrative |
| Study track | shared/unknown |
| Source class | unclassified |
| Rows | 2 |
| Physical columns | 8 |
| DD-defined properties | 12 |
| Row grain | UNKNOWN — requires source or human review |
| Subject identifier, if available | — |
| Primary/row identifier | *submitter_id |

### 3.22.2 Key and duplication profile

| Measure | Result |
|---|---|
| Exact duplicate physical rows | 0 |
| Non-empty primary IDs | 2 |
| Distinct primary IDs | 2 |
| Duplicate primary-ID values | 0 |
| Rows carrying a duplicated primary ID | 0 |
| Primary-ID uniqueness ratio | 100.0% |
| Missing primary IDs | 0 |

### 3.22.3 Column profile

| Physical column | Canonical DD field | Role | Parsed type | Rows | Non-empty | Missing | Complete | Distinct | Uniqueness | Summary | Masked examples | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *type | study.type | const | string | 2 | 2 | 0 | 100.0% | 1 | 50.0% | constant=study | study | CONST |
| project_id | study.project_id | const | string | 2 | 2 | 0 | 100.0% | 1 | 50.0% | constant=ARDaC-AlcHepNet | ARDaC-AlcHepNet | CONST |
| *submitter_id | study.submitter_id | id | string | 2 | 2 | 0 | 100.0% | 2 | 100.0% | unique 2/2; duplicates=0 | ***, cl***al | UNIQUE |
| *projects.code | study.projects | const | string | 2 | 2 | 0 | 100.0% | 1 | 50.0% | constant=AlcHepNet | AlcHepNet | CONST |
| *study_name | study.study_name | cat | string | 2 | 2 | 0 | 100.0% | 2 | 100.0% | observational=1 (50.0%); clinical_trial=1 (50.0%) | observational, clinical_trial | UNIQUE |
| data_description | study.data_description | cat | string | 2 | 0 | 2 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| study_description | study.study_description | cat | string | 2 | 0 | 2 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |
| type_of_data | study.type_of_data | cat | string | 2 | 0 | 2 | 0.0% | 0 | — | no observed values | — | EMPTY,SPARSE |

### 3.22.4 Generated quality flags

| Flag | Triggered columns |
|---|---|
| CONST | 3 |
| EMPTY | 3 |
| SPARSE | 3 |
| UNIQUE | 2 |

### 3.22.5 Relationship integrity

No physical `*.submitter_id` foreign-key columns detected.

### 3.22.6 Schema-versus-physical comparison

| DD property | Physical column | State | Detail |
|---|---|---|---|
| type | *type | populated | non-empty=2/2 |
| id | — | absent | not materialized in this physical file |
| state | — | absent | not materialized in this physical file |
| submitter_id | *submitter_id | populated | non-empty=2/2 |
| study_name | *study_name | populated | non-empty=2/2 |
| data_description | data_description | empty | non-empty=0/2 |
| study_description | study_description | empty | non-empty=0/2 |
| type_of_data | type_of_data | empty | non-empty=0/2 |
| projects | *projects.code | populated | non-empty=2/2 |
| project_id | project_id | populated | non-empty=2/2 |
| created_datetime | — | absent | not materialized in this physical file |
| updated_datetime | — | absent | not materialized in this physical file |

DD properties: 12  
Physical headers: 8  
DD properties materialized: 8  
DD properties absent: 4  
Materialized but entirely empty: 3  
Physical headers not mapped to DD: 0

### 3.22.7 Machine-generated findings

- EMPTY: 3/8 physical columns mapped to DD are entirely empty.
- UNIQUE: *submitter_id has 2 distinct values in 2 non-empty rows.

# 4. Cross-table integrity summary

| Source table | FK | Target table | Populated | Matched | Unmatched | Match rate |
|---|---|---|---|---|---|---|
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001.tsv | *follow_ups.submitter_id | follow_up | 20000 | 20000 | 0 | 100.0% |
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001.tsv | labs.submitter_id | lab | 20000 | 20000 | 0 | 100.0% |
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_002.tsv | *follow_ups.submitter_id | follow_up | 6529 | 6529 | 0 | 100.0% |
| aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_002.tsv | labs.submitter_id | lab | 6529 | 6529 | 0 | 100.0% |
| audit_obs_DCC_data_release_v2-1-0.tsv | cases.submitter_id | case | 1060 | 1060 | 0 | 100.0% |
| audit_rct_DCC_data_release_v2-1-0.tsv | cases.submitter_id | case | 134 | 134 | 0 | 100.0% |
| bbt-molecular-merged_valid_followupsdel1_v2-1-0.tsv | aliquots.submitter_id | aliquot | 1748 | 1748 | 0 | 100.0% |
| bbt-molecular-merged_valid_followupsdel1_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 1748 | 1748 | 0 | 100.0% |
| demographic_obs_DCC_data_release_v2-1-0.tsv | *cases.submitter_id | case | 1133 | 1133 | 0 | 100.0% |
| demographic_rct_DCC_data_release_v2-1-0.tsv | *cases.submitter_id | case | 147 | 147 | 0 | 100.0% |
| mod_aliquot-inventory_DCC_data_release_v2-1-0_updated_labs_250815.tsv | *follow_ups.submitter_id | follow_up | 50254 | 50254 | 0 | 100.0% |
| mod_aliquot-inventory_DCC_data_release_v2-1-0_updated_labs_250815.tsv | labs.submitter_id | lab | 50143 | 50143 | 0 | 100.0% |
| mod_case_obs_DCC_data_release_v2-1-0_250815_minor.tsv | *studies.submitter_id | study | 1133 | 1133 | 0 | 100.0% |
| mod_case_rct_DCC_data_release_v2-1-0_250815_minor.tsv | *studies.submitter_id | study | 147 | 147 | 0 | 100.0% |
| mod_follow-up_add-on_cleaned_v2-1-0.tsv | cases.submitter_id | case | 25 | 25 | 0 | 100.0% |
| mod_follow-up_add-on_cleaned_v2-1-0.tsv | demographics.submitter_id | demographic | 25 | 25 | 0 | 100.0% |
| mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv | cases.submitter_id | case | 2140 | 2140 | 0 | 100.0% |
| mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv | demographics.submitter_id | demographic | 2140 | 2140 | 0 | 100.0% |
| mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv | cases.submitter_id | case | 834 | 834 | 0 | 100.0% |
| mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv | demographics.submitter_id | demographic | 834 | 834 | 0 | 100.0% |
| mod_molecular-test_liangpunsakul-orm1_DCC_data_release_v2-1-0_minor.tsv | aliquots.submitter_id | aliquot | 164 | 164 | 0 | 100.0% |
| mod_molecular-test_liangpunsakul-orm1_DCC_data_release_v2-1-0_minor.tsv | *follow_ups.submitter_id | follow_up | 164 | 164 | 0 | 100.0% |
| mod_molecular-test_szabo_DCC_data_release_v2-1-0_fixed_duplicates_minor.tsv | aliquots.submitter_id | aliquot | 993 | 993 | 0 | 100.0% |
| mod_molecular-test_szabo_DCC_data_release_v2-1-0_fixed_duplicates_minor.tsv | *follow_ups.submitter_id | follow_up | 993 | 993 | 0 | 100.0% |
| molecular-test_liangpunsakul-orm1_part2_DCC_data_release_v2-1-0.tsv | aliquots.submitter_id | aliquot | 40 | 40 | 0 | 100.0% |
| molecular-test_liangpunsakul-orm1_part2_DCC_data_release_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 40 | 40 | 0 | 100.0% |
| molecular-test_mehal-ace_DCC_data_release_v2-1-0.tsv | aliquots.submitter_id | aliquot | 192 | 192 | 0 | 100.0% |
| molecular-test_mehal-ace_DCC_data_release_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 192 | 192 | 0 | 100.0% |
| molecular-test_mehal-renin_DCC_data_release_v2-1-0.tsv | aliquots.submitter_id | aliquot | 192 | 192 | 0 | 100.0% |
| molecular-test_mehal-renin_DCC_data_release_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 192 | 192 | 0 | 100.0% |
| molecular-test_nagy-urine_DCC_data_release_v2-1-0.tsv | aliquots.submitter_id | aliquot | 1160 | 1160 | 0 | 100.0% |
| molecular-test_nagy-urine_DCC_data_release_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 1160 | 1160 | 0 | 100.0% |
| molecular-test_schnabl_DCC_data_release_v2-1-0.tsv | aliquots.submitter_id | aliquot | 297 | 297 | 0 | 100.0% |
| molecular-test_schnabl_DCC_data_release_v2-1-0.tsv | *follow_ups.submitter_id | follow_up | 297 | 297 | 0 | 100.0% |

Additional requested cross-table summaries that require an authoritative release manifest or explicit study/source-scope rules are marked **UNKNOWN** rather than inferred: subjects present only in one study track; canonical/supplement overlap; and correction-file supersession.

# 5. Release-to-release changes

Not generated: only one physical release was supplied.

# 6. Coverage boundary

This profile describes only the physical files and source scope listed in Section 1. It does not define clinical concepts, endpoints, eligibility, analysis methods, or protocol intent. A field absent or empty in this release must not be described as clinically absent; it is only unavailable in the profiled physical scope.

# 7. Reproducibility checks

- [x] Every number in generated sections was generated programmatically.
- [x] Generator timestamp is supplied explicitly, so the same inputs and command can produce byte-identical Markdown.
- [x] Exact generator command is recorded; repository/commit are UNKNOWN because they were not supplied.
- [x] Every source TSV has a SHA-256 hash.
- [ ] Authoritative source classification could not be completed because no manifest/registry was supplied.
- [x] Identifier examples are masked.
- [x] RCT and OBS files are profiled separately when filenames identify the track.
- [x] Enum validation is entity/property scoped where an enum is directly available in the supplied DD.
- [x] Foreign-key checks use detected physical parent-ID fields and supplied target tables.
- [x] No clinical interpretation was generated.

Independent primary-ID checks are written to `submitter_id_audit.csv`. Four primary-ID counts were independently reproduced with Python's standard `csv` module (not pandas): follow-up OBS 2,140/2,140 distinct; aliquot inventory 50,254/50,254; demographic OBS 1,133/1,133; case OBS 1,133/1,133. The standard-library parser was used because at least one TSV contains an embedded line break, making raw `wc -l` unsafe.
