# AlcHepNet / ARDaC Umbrella Knowledge Base

> This file is a routing and conflict-resolution layer. It does not replace the protocol, MOP/training, DD/schema, or Physical Data Profile.

## 0. How to use this file
1. Classify the question with the Routing Table (Block 1). Also check the Concept Index (Block 2) whenever a concept affects interpretation, data selection, filtering, endpoint definition, or analysis.
2. Open the linked source. Protocols govern study concepts/rules; the DD governs field names/types/relationships; the Physical Data Profile governs what is physically present and how it is encoded; the MOP/training governs documented operational procedures within scope.
3. If a concept cannot be verified, use Block 5 and stop or ask for clarification. Do not infer a plausible definition or field mapping.

## 1. Routing table

| Question family | Example triggers | Go to | Section / target |
|---|---|---|---|
| eligibility and study population | eligible, included, excluded, AH case, control, MELD range | relevant protocol KB | Eligibility / Population |
| ITAALD study design or conduct | ITAALD, F-652, IL-22, acamprosate, integrated treatment, sequential randomization | ITAALD Protocol KB | design, interventions, eligibility, schedule, endpoints |
| ITAALD statistical analysis | ITAALD estimand, ITT, mITT, CMH, Fine-Gray, missing data, interim analysis | ITAALD SAP KB | analysis population, endpoint model, multiplicity, missing data, interim monitoring |
| study timeline and visits | Day 0, Week 4, Day 90, follow-up, visit window | relevant protocol KB | Timeline / Study Procedures |
| endpoint or clinical concept definition | survival, AKI, MELD, outcome, baseline | relevant protocol KB | Outcomes / Definitions |
| treatment/randomization | arm, prednisone, anakinra, randomization | RCT protocol KB | Treatment / Randomization |
| biospecimen collection/processing | serum, PBMC, urine, aliquot, storage, shipping | Biorepository MOP KB | specimen-specific procedure |
| field name / relationship | table, column, join, parent, submitter_id | DD/schema | relevant entity/property/link |
| physical availability / encoding | populated, missing, values, distribution, duplicates | Physical Data Profile | relevant physical table profile |
| portal / website operation | portal, download, explore, export | ARDaC training / approved SOP | relevant workflow section |
| statistical analysis rule | ITT, Cox, log-rank, summary method | protocol/SAP/MOP as applicable | Statistical Analysis |

## 2. Concept index

### 1. baseline MELD
- **Also asked as** baseline MELD / MELD at enrollment / Day-0 MELD / MELD score
- **Defined in** OBS protocol KB § Questionnaires and Clinical Scores / §4.3.5; RCT protocol KB § Eligibility and Outcomes
- **Lives in** DD: `follow_up.meld_score`; physical files: `mod_follow-up_obs_DCC_data_release_v2-1-0_indexday.tsv` → `meld_score` and `mod_follow-up_rct_DCC_data_release_v2-1-0_indexday.tsv` → `meld_score`
- **Rule** select `meld_score` from the follow-up row with physical `visit_day == 0` (equivalently physical `*days_to_follow_up == 0` in this supplied release; DD property `days_to_follow_up`); do not substitute case-level `rct_meld_strata` for the numeric score
- **Trap** `rct_meld_strata` is only the RCT stratification category (`Low(<=25)` / `High(>25)`), not the numeric MELD; missing MELD is not zero
- **last_verified** 2026-08-27

### 2. Day 0 / index visit
- **Also asked as** Day 0 / baseline / index visit / time zero
- **Defined in** OBS protocol evaluation: baseline visit after consent and eligibility verification; RCT protocol: Day 0 is randomization/baseline
- **Lives in** DD: `follow_up.visit_day` / `follow_up.days_to_follow_up`; physical follow-up TSVs use `visit_day` / `*days_to_follow_up`; `case.index_date` is present but contains the label `Study Enrollment`, not an actual date
- **Rule** use the follow-up row with `visit_day == 0` for released baseline measurements; do not treat `case.index_date` as a calendar date
- **Trap** RCT protocol meaning (randomization) and physical `case.index_date` encoding (`Study Enrollment`) are not identical representations
- **last_verified** 2026-08-27

### 3. follow-up visit / visit day
- **Also asked as** visit day / follow-up timepoint / scheduled visit / which day
- **Defined in** OBS protocol Timeline; RCT protocol Timeline
- **Lives in** DD: `follow_up.visit_day` and `follow_up.days_to_follow_up`; physical headers: `visit_day` and `*days_to_follow_up`
- **Rule** use the physical follow-up row and its day-offset field; supplied OBS values are `{0,28,84,168}` and supplied RCT values are `{0,3,7,14,28,60,90,180}`
- **Trap** protocol visit windows and nominal stored visit days are different concepts; do not infer actual visit date from nominal day alone
- **last_verified** 2026-08-27

### 4. 90-day survival
- **Also asked as** alive at Day 90 / 90-day mortality / primary RCT survival endpoint
- **Defined in** RCT protocol KB § Primary Endpoint: 90-day all-cause survival; OBS protocol records survival as a longitudinal outcome
- **Lives in** `case.days_90_survival`; supporting overall status also exists in `demographic.vital_status` and `demographic.days_to_death`
- **Rule** for the released 90-day status use `case.days_90_survival`; use protocol/SAP for endpoint analysis/censoring rules
- **Trap** `demographic.vital_status` is overall observed status, not specifically Day-90 status; `Unknown` is not alive
- **last_verified** 2026-08-27

### 5. 180-day survival
- **Also asked as** alive at Day 180 / 180-day mortality / final survival follow-up
- **Defined in** RCT protocol KB § Secondary Endpoints / Day 180; OBS protocol long-term survival follow-up
- **Lives in** `case.days_180_survival`; overall status also appears in `demographic.vital_status`
- **Rule** use `case.days_180_survival` for the released Day-180 status
- **Trap** do not replace a Day-180 `Unknown` with overall `vital_status` unless an approved analysis rule explicitly allows it
- **last_verified** 2026-08-27

### 6. acute kidney injury (AKI)
- **Also asked as** AKI / acute renal injury / kidney injury event
- **Defined in** OBS protocol: event of special interest / clinical outcome; RCT protocol: secondary/safety outcome
- **Lives in** `case.aki_status`, `case.days_to_aki`, `case.days_90_aki`, `case.days_180_aki`
- **Rule** choose the field that matches the question's time horizon; use `aki_status` only for overall released status, not automatically for Day 90 or Day 180
- **Trap** time-specific and overall AKI fields are not interchangeable; protocol definitions must control clinical interpretation
- **last_verified** 2026-08-27

### 7. RCT treatment arm
- **Also asked as** treatment group / randomized arm / prednisone arm / anakinra plus zinc arm
- **Defined in** RCT protocol KB § Treatment Arms
- **Lives in** `case.actarm`; physical RCT case file contains `Anakinra + Zinc` and `Prednisone`
- **Rule** use `case.actarm` for released randomized-treatment assignment
- **Trap** OBS `case.actarm` is empty in the supplied release; do not infer an arm for observational participants
- **last_verified** 2026-08-27

### 8. observational cohort / participant group
- **Also asked as** AH case / heavy drinking control / healthy control / cohort / study group
- **Defined in** OBS protocol KB § Population / Eligibility
- **Lives in** `case.cohort`; physical OBS values include `Heavy Drinker with Alcoholic Hepatits`, `Heavy Drinker without Alcoholic Hepatits`, and `Healthy Donor`
- **Rule** use the observed `case.cohort` encoding for released grouping and the protocol for the clinical definition of each group
- **Trap** physical labels contain spelling/wording different from protocol terminology; do not silently rewrite raw values when filtering
- **last_verified** 2026-08-27

### 9. RCT MELD stratum
- **Also asked as** MELD subgroup / low vs high MELD / randomization MELD stratum
- **Defined in** RCT protocol randomization/stratification and planned subgroup analysis
- **Lives in** `case.rct_meld_strata`
- **Rule** use the observed values `Low(<=25)` and `High(>25)` when the question is explicitly about stratification; use `follow_up.meld_score` for numeric MELD
- **Trap** this is a category, not a score; it is empty in OBS
- **last_verified** 2026-08-27

### 10. sex / gender
- **Also asked as** sex / gender / male / female
- **Defined in** OBS protocol demographics; DD defines separate `demographic.sex` and `demographic.gender`
- **Lives in** `demographic.sex` and `demographic.gender`
- **Rule** use the exact field requested; if the question does not distinguish sex from gender, report the ambiguity rather than choosing one silently
- **Trap** the two fields are not guaranteed identical; supplied OBS data include one `gender=unknown` while `sex` remains male/female
- **last_verified** 2026-08-27

### 11. BMI
- **Also asked as** body mass index / BMI at baseline / BMI at visit
- **Defined in** protocol anthropometric measurements; DD `follow_up.bmi`
- **Lives in** `follow_up.bmi`
- **Rule** select BMI from the follow-up row corresponding to the requested visit; baseline means `visit_day == 0`
- **Trap** do not apply healthy-control eligibility BMI thresholds to other cohorts unless the protocol says so
- **last_verified** 2026-08-27

### 12. alcohol consumption / TLFB
- **Also asked as** Timeline Follow-Back / drinks / drinking days / alcohol use at follow-up
- **Defined in** OBS protocol: TLFB at baseline and scheduled follow-up; RCT protocol: TLFB at screening and selected follow-up visits
- **Lives in** `follow_up.tlfb_number_drinks`, `follow_up.tlfb_drinking_days`, and related TLFB fields; `tlfb_collected` is physically present but empty in supplied OBS/RCT files
- **Rule** use the quantitative TLFB fields for observed released values; do not use empty `tlfb_collected` as evidence that TLFB was not performed
- **Trap** an empty indicator and populated TLFB result fields coexist in this release
- **last_verified** 2026-08-27

### 13. specimen type / aliquot
- **Also asked as** biospecimen type / serum / plasma / PBMC / urine / aliquot
- **Defined in** Biorepository MOP KB specimen-specific sections; study protocol determines whether/when collection is required
- **Lives in** `aliquot.specimen_type`; physical aliquot files also link through `follow_ups.submitter_id` and `labs.submitter_id`
- **Rule** use protocol for collection schedule, MOP for handling, DD for relationship path, and Physical Data Profile for actual specimen records
- **Trap** MOP handling rules do not establish that a specimen exists for every participant/visit; physical availability must be checked separately
- **last_verified** 2026-08-27

### 14. molecular/laboratory test result
- **Also asked as** assay result / molecular test / lab assay / test value
- **Defined in** DD `molecular_test.laboratory_test`, `molecular_test.test_value`, `molecular_test.test_unit`; protocol/MOP defines study or laboratory context when applicable
- **Lives in** `molecular_test.laboratory_test`, `molecular_test.test_value`, `molecular_test.test_unit`, linked to follow-up and/or aliquot records
- **Rule** identify the assay by `laboratory_test`, then interpret `test_value` together with `test_unit`; use relationship fields to locate visit/specimen context
- **Trap** different physical molecular-test files represent different assays; never combine values across files without checking assay name/unit and source scope
- **last_verified** 2026-08-27

### 15. submitter identifier / join key
- **Also asked as** submitter_id / participant ID / row ID / parent ID / join key
- **Defined in** DD: entity `submitter_id` is a project-specific node identifier; relationships use target `*.submitter_id`
- **Lives in** each table's `*submitter_id` for the row identifier; parent relationship fields such as `cases.submitter_id`, `follow_ups.submitter_id`, `aliquots.submitter_id`, `labs.submitter_id`, `studies.submitter_id`
- **Rule** treat the table's own `*submitter_id` as the row/node identifier and `entity.submitter_id` fields as foreign keys to parent entities
- **Trap** parent submitter IDs are expected to repeat. In the supplied release every table's own `*submitter_id` is complete and unique within that file, while parent submitter-ID columns often have low uniqueness because many child rows map to one parent
- **last_verified** 2026-08-27

## 3. Source register

**Repository snapshot used:** [`f209bdf5cebc7ed4758329bff075403c58718be7`](https://github.com/charisyliu/AlcHepNet-MDFiles/tree/f209bdf5cebc7ed4758329bff075403c58718be7)  
**Repository:** `charisyliu/AlcHepNet-MDFiles`  
All GitHub links below are pinned to this commit and will not change when the `main` branch changes.

| Source | Type | Scope | Primary purpose | Can decide | Cannot decide | Version | last_verified | Link/address |
|---|---|---|---|---|---|---|---|---|
| `alchepnet 01 version 3 clean protocol 3 9 21_updated.md` | protocol KB | OBS | study design, population, procedures, concepts, timing | official OBS study meaning as represented in KB/source | actual field existence/population | V3 2021-03-09 | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/alchepnet%2001%20version%203%20clean%20protocol%203%209%2021_updated.md) |
| `CLEAN AHN RCT Protocol Amendment 5 v2.md` | protocol KB | RCT | design, treatment, eligibility, endpoints, timing | RCT protocol rules | actual released encoding | V6 Amendment 5 2022-01-25 | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/CLEAN%20AHN%20RCT%20Protocol%20Amendment%205%20v2.md) |
| `AlcHepNet_Biorepository_MOP_v2.0 10-2021 (004)_updated.md` | MOP KB | biospecimen operations | collection, processing, labeling, storage, shipping | MOP procedures | study-specific requirement unless protocol agrees; actual availability | V2.0 2021-10-25 | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/AlcHepNet_Biorepository_MOP_v2.0%2010-2021%20%28004%29_updated.md) |
| `ARDaC_Training_Comprehensive.md` | training | portal/workflow | portal and training workflow | documented training workflow | official protocol meaning or physical availability | 2026-06-24 training compilation | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/ARDaC_Training_Comprehensive.md) |
| `schema.json` | data dictionary/schema | DD 2.1.1 | entities, properties, types, enums, links | schema names/relationships | clinical intent or actual completeness | 2.1.1 | 2026-08-27 | supplied `dd/schema.json`; not present in this repository snapshot |
| `AlcHepNet_Physical_Data_KB_Final.md` | generated physical profile | supplied v2-1-0 TSV scope | actual rows, columns, encodings, missingness, distributions, link checks | what is physically present in supplied scope | clinical definitions or protocol rules | generated 2026-08-27 | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/AlcHepNet_Physical_Data_KB_Final.md) |
| `Umbrella_KB_Evaluation_Latest.md` | QA | umbrella KB | representative questions, coverage, traceability, and identified gaps | QA evidence about KB coverage | cannot override primary source | latest at pinned commit | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/Umbrella_KB_Evaluation_Latest.md) |
| `AlcHepNet_Concept_Index_Derivation.md` | QA / derivation | umbrella KB | derivation of the original concept index and development question set | traceability for concept-index coverage | cannot override primary source | latest at pinned commit | 2026-09-17 | [Pinned source](https://github.com/charisyliu/AlcHepNet-MDFiles/blob/f209bdf5cebc7ed4758329bff075403c58718be7/AlcHepNet_Concept_Index_Derivation.md) |
| `ITAALD_Protocol_KB.md` | protocol KB | ITAALD | design, population, interventions, visits, endpoint definitions, safety, specimen schedule | official ITAALD study meaning and conduct represented in signed Protocol V2 | formal analysis rules when the SAP is more specific; actual released encoding | Protocol V2; 2025-05-22; signed 2025-07-23 | 2026-09-17 | generated from `Sponsor signed-ITAALD Protocol v2 05-22-2025 Clean (1)(1).pdf`; repository commit link pending upload |
| `ITAALD_SAP_KB.md` | SAP KB | ITAALD | analysis populations, models, multiplicity, interim analysis, missing data, safety analysis | prespecified ITAALD statistical-analysis rules represented in SAP V1.0 | study conduct, actual released encoding, unresolved SAP ambiguities | SAP V1.0; 2025-03-31 | 2026-09-17 | generated from `ITAALD SAP-03-31-25 Final(1).docx`; repository commit link pending upload |

## 4. Source authority and relationships

| Information being decided | Primary authority | Boundary |
|---|---|---|
| study concept, endpoint, eligibility, time rule | relevant protocol | protocol does not prove field exists/populated |
| ITAALD formal analysis population, model, multiplicity, missing-data, or interim rule | ITAALD SAP | SAP does not override later signed protocol for study conduct; unresolved conflicts require clarification |
| specimen handling, labeling, shipping, storage | MOP | MOP does not by itself prove study-specific collection requirement or physical availability |
| portal/training workflow | training / approved SOP | training cannot override protocol/DD |
| field name, type, entity, relationship | DD/schema | expected schema is not actual release completeness |
| column presence, missingness, values, distributions, key behavior | Physical Data Profile | physical data cannot redefine clinical meaning |

Standard workflow:
1. Confirm concept/study rule in protocol or MOP as appropriate.
2. Use DD to identify exact `table.column` and relationships.
3. Use Physical Data Profile to verify field/materialization/encoding in the supplied release.
4. Apply operational training only within its documented scope.
5. If sources disagree, use Block 5; never resolve by majority vote.

## 5. Known contradictions and unresolved gaps

### 5A. Known contradictions

| Concept | Source A | Source B | Which we follow | Authority / reason | last_verified |
|---|---|---|---|---|---|
| OBS AST threshold for AH | formal eligibility: AST >50 IU/L | Research Strategy §4.3.2: AST >40 U/L | formal eligibility for eligibility decisions; retain contradiction | formal eligibility is the operative eligibility section; study-team clarification still desirable | 2026-08-27 |
| OBS heavy-control follow-up | Executive Summary/Table 2: baseline + Week 24 | §5.2.2: Weeks 4,12,24 | unresolved for operational use; current KB follows Executive Summary/Table 2 | source inconsistency documented in evaluation | 2026-08-27 |
| platelet-poor plasma aliquot count | MOP sections/appendix indicate six | MOP processing section indicates nine | unresolved | same-authority source conflict | 2026-08-27 |
| HCl plasma cap/storage details | MOP sections differ on cap wording and general KB says -80°C | operational section specifies violet/blue-dot wording and -70°C | unresolved pending operational authority | source inconsistency | 2026-08-27 |
| ITAALD primary endpoint representation | Protocol describes time from treatment initiation to first composite event | SAP primary analysis compares composite-event rates at Day 180 using CMH or logistic regression | SAP governs the prespecified primary analysis, but estimand reconciliation is required | protocol/SAP describe different endpoint representations | 2026-09-17 |
| ITAALD eligible MELD range vs randomization strata | Protocol eligibility allows MELD 20–35 | Protocol randomization text lists strata 20–25 and 26–30 | unresolved for MELD 31–35 | executable DCC randomization specification is needed | 2026-09-17 |
| ITAALD randomization block size | Protocol/SAP passage specifies blocks of 4 | Another passage specifies random block sizes of 4 and 6 | unresolved | use executable DCC randomization specification | 2026-09-17 |
| ITAALD PROMIS-29 timing | Protocol schedule lists Days 7, 90, and 180 | SAP narrative emphasizes Day 90 while proposing a repeated-measures model | protocol schedule governs collection; SAP governs analysis, pending clarification of included visits | collection and analysis descriptions differ | 2026-09-17 |

### 5B. Unresolved gaps

| Gap ID | Concept/question | Triggered by | Sources checked | What is missing/uncertain | Needed authority / next action | Status | last_verified |
|---|---|---|---|---|---|---|---|
| GAP-001 | authoritative canonical/supplement/correction file classification | Physical Data Profile generation | supplied TSV names + DD | no release manifest/registry supplied | obtain release manifest/registry | open | 2026-08-27 |
| GAP-002 | pinned commit URLs for repository-hosted umbrella sources | umbrella source register | repository files at commit `f209bdf5cebc7ed4758329bff075403c58718be7` | resolved for repository-hosted sources; supplied `dd/schema.json` is not present in this repository snapshot | preserve pinned links; add a separately versioned schema address if it is later published | partially resolved | 2026-09-17 |
| GAP-003 | actual calendar index date | Day 0/index concept | protocol, DD, physical case/follow-up | release contains nominal day offsets and `index_date=Study Enrollment`, not a calendar date | identify portal/date source if one exists | open | 2026-08-27 |
| GAP-004 | exact analysis treatment of `Unknown` 90/180-day survival | survival concepts | protocol KB + released fields | physical status exists, but imputation/censoring rule requires SAP/protocol-specific analysis context | consult SAP/approved analysis rule | open | 2026-08-27 |
| GAP-005 | ITAALD Stage-2 analysis population | sequential randomization | ITAALD Protocol V2 + SAP V1.0 | only Day-7 survivors are randomized to AUD treatment; SAP does not fully define Stage-2 denominator or handling of deaths before Day 7 | obtain approved estimand/programming specification | open | 2026-09-17 |
| GAP-006 | ITAALD mITT definition | SAP analysis populations | ITAALD SAP V1.0 | mITT is defined only as randomized participants receiving at least one F-652 dose, without a treatment-neutral rule | clarify intended mITT population | open | 2026-09-17 |
| GAP-007 | ITAALD primary missing-data denominator | SAP missing-data section | ITAALD SAP V1.0 | ITT is specified, but missing composite values are not imputed and only observed values are analyzed | specify denominator and sensitivity analysis | open | 2026-09-17 |
| GAP-008 | ITAALD TLFB imputation algorithm | SAP missing-data section | ITAALD SAP V1.0 | SAP refers to prior AUD trials but does not provide an executable algorithm | obtain programming rules for primary and sensitivity imputations | open | 2026-09-17 |
| GAP-009 | repository-pinned links for ITAALD KBs and source documents | new ITAALD integration | local generated KBs and supplied source files | ITAALD files were not present at the repository snapshot used by the source register | upload files, commit, then replace working paths with commit-pinned URLs | open | 2026-09-17 |

## 6. Not covered
This draft does not establish: authoritative release-file classification; a repository-pinned address for the externally supplied `dd/schema.json`; SAP-only rules not present in the reviewed protocol KBs; or portal behavior not supported by the available training material.

If a request is not covered, check the relevant protocol/MOP/DD directly, then create an unresolved gap rather than infer a definition, field mapping, filter, endpoint, or statistical rule.

## 7. Evaluation-driven navigation additions

The original 15 concepts passed all 20 questions used to derive the Concept Index. Five additional questions were then used to test generalization beyond that development set. The following entries close the partial routes observed in that second test set.

### 16. Lille score / Day-7 treatment rule
- **Also asked as** Lille / Day-7 Lille / steroid response / prednisone continuation
- **Defined in** RCT protocol KB § Day 7 Lille Rule
- **Lives in** DD: `follow_up.lille_score`; verify physical presence and completeness in the RCT follow-up profile before analysis
- **Rule** use the Day-7 RCT follow-up row and the protocol-defined threshold to determine the prednisone or matching-placebo rule; retain zinc or matching placebo according to the protocol
- **Trap** a stored Lille value does not independently establish that the correct visit or protocol threshold was used; do not apply this RCT rule to OBS participants
- **last_verified** 2026-09-02

### 17. infection screen / culture result
- **Also asked as** infection / sepsis / blood culture / urine culture / organism
- **Defined in** OBS protocol events of special interest; RCT protocol infection and sepsis outcomes
- **Lives in** DD `follow_up.infection_screen_done` plus source-specific culture result, organism, and date fields; use the Physical Data Profile to confirm which are materialized and populated
- **Rule** distinguish whether screening was performed from whether infection was confirmed; interpret the result, organism, and date together
- **Trap** `infection_screen_done=Yes` is not a positive infection diagnosis, and an empty culture field is not automatically a negative culture
- **last_verified** 2026-09-02

### 18. hepatic encephalopathy
- **Also asked as** encephalopathy / HE / liver-related confusion
- **Defined in** OBS protocol clinical outcomes/events of special interest; RCT protocol outcomes and standard clinical care
- **Lives in** DD `follow_up.hep_enceph` and `follow_up.hep_enceph_diagnosis_date`
- **Rule** use the protocol for clinical meaning and the visit-scoped fields for released status and timing
- **Trap** the DD field describes spontaneous hepatic encephalopathy grade 2 or higher; it is not an any-grade flag
- **last_verified** 2026-09-02

### 19. specimen shipping and storage
- **Also asked as** shipment schedule / quarterly shipment / repository / freezer / receiving site
- **Defined in** protocol KB for collection/shipment expectation; Biorepository MOP KB for operational preparation, temperature, receipt, inventory, deviations, and storage
- **Lives in** physical specimen records only where a verified shipment/receipt field or table is documented; no universal shipment-event mapping was established in the supplied sources
- **Rule** use the protocol to answer when shipment is expected and the MOP to answer how it is performed; use the Physical Data Profile only for verified released fields
- **Trap** a protocol statement that specimens are shipped quarterly does not prove a particular shipment event exists in the release
- **last_verified** 2026-09-02

### 20. PBMC availability
- **Also asked as** PBMC collected / PBMC missing / cellular specimen availability
- **Defined in** protocol biospecimen schedule and MOP PBMC section
- **Lives in** `aliquot.specimen_type=PBMC` for physical aliquot records in the supplied release
- **Rule** use protocol/MOP to determine conditional collection and processing; use the Physical Data Profile to quantify actual PBMC records within a named file and denominator
- **Trap** PBMC collection is limited to selected sites/conditions; absence can be structurally expected and must not automatically be treated as random missingness
- **last_verified** 2026-09-02

### 21. ITAALD study track
- **Also asked as** ITAALD / ITAALD-01 / integrated therapies trial / new AlcHepNet trial
- **Defined in** ITAALD Protocol KB § Study Identity and § Trial Design; ITAALD SAP KB § Analysis Framework
- **Lives in** ARDaC mapping not established in the supplied DD or physical release
- **Rule** route study-conduct questions to the ITAALD Protocol KB and statistical-analysis questions to the ITAALD SAP KB
- **Trap** ITAALD is distinct from the earlier AlcHepNet observational cohort and anakinra-plus-zinc RCT; do not reuse their arms, visit schedules, or endpoint rules
- **last_verified** 2026-09-17

### 22. ITAALD sequential randomization
- **Also asked as** two-stage randomization / SMART design / Day-1 randomization / Day-7 randomization
- **Defined in** ITAALD Protocol KB § Trial Design and Sequential Randomization
- **Lives in** no verified ARDaC field mapping supplied
- **Rule** Day 1 randomizes F-652 versus prednisone; only survivors reaching Stage 2 are randomized on Day 7 or discharge to AUD intervention versus usual care
- **Trap** the four observed treatment combinations are not assigned in one baseline randomization, and the Stage-2 population is conditional on survival
- **last_verified** 2026-09-17

### 23. ITAALD sAH treatment
- **Also asked as** F-652 / IL-22 / prednisone / severe-AH treatment arm
- **Defined in** ITAALD Protocol KB § Study Treatments
- **Lives in** no verified ARDaC field mapping supplied
- **Rule** distinguish the blinded Stage-1 assignment from actual treatment received and apply the Day-7 Lille stopping rule to prednisone or prednisone placebo
- **Trap** F-652 is not anakinra; the ITAALD arms must not be mapped to the older RCT `case.actarm` values without a new release mapping
- **last_verified** 2026-09-17

### 24. ITAALD AUD intervention
- **Also asked as** acamprosate / MI / MET / usual care / alcohol treatment
- **Defined in** ITAALD Protocol KB § Trial Design and § Study Treatments
- **Lives in** no verified ARDaC field mapping supplied
- **Rule** the active AUD intervention combines acamprosate, inpatient motivational interviewing, and four motivational-enhancement sessions; the comparator is brief advice plus 12-step referral
- **Trap** AUD assignment occurs only for Stage-2 survivors and is not blinded
- **last_verified** 2026-09-17

### 25. ITAALD six-month composite endpoint
- **Also asked as** primary endpoint / Day-180 composite / alcohol- and liver-related event
- **Defined in** ITAALD Protocol KB § Endpoints; ITAALD SAP KB § Primary Endpoint and Estimand Components
- **Lives in** no verified ARDaC field mapping supplied
- **Rule** the composite is positive when any defined component occurs by six months; use the SAP for the formal treatment comparison
- **Trap** the protocol uses time-to-first-event language while the SAP specifies a Day-180 event-rate comparison; do not silently treat those as the same estimand
- **last_verified** 2026-09-17

### 26. ITAALD Day-7 Lille stopping rule
- **Also asked as** Lille >0.45 / steroid stopping / prednisone discontinuation
- **Defined in** ITAALD Protocol KB § Trial Design and § Study Treatments
- **Lives in** a verified ITAALD data-field mapping has not been supplied
- **Rule** stop prednisone or prednisone placebo when the Day-7 Lille score is greater than 0.45
- **Trap** this is a treatment-stopping rule within blinded Stage 1, not the criterion for Stage-2 AUD randomization
- **last_verified** 2026-09-17

### 27. ITAALD survival endpoints
- **Also asked as** overall survival / transplant-free survival / 30-day / 90-day / 180-day / one-year / two-year survival
- **Defined in** ITAALD Protocol KB § Secondary Endpoints; ITAALD SAP KB § Secondary Endpoint Analyses
- **Lives in** no verified ITAALD ARDaC mapping supplied
- **Rule** use the named time point and distinguish overall from transplant-free survival; consult the SAP for fixed-time and time-to-event analyses
- **Trap** the ITAALD survival schedule and analysis must not be inferred from the earlier RCT’s released Day-90/Day-180 fields
- **last_verified** 2026-09-17

### 28. ITAALD analysis population
- **Also asked as** ITT / mITT / per protocol / Stage-2 population / safety population
- **Defined in** ITAALD SAP KB § Analysis Populations
- **Lives in** derived analysis datasets; no verified released field mapping supplied
- **Rule** ITT is primary; treat mITT, PP, Stage-2, and safety sets as unresolved until executable inclusion rules are approved
- **Trap** the SAP’s mITT wording is F-652-specific and the AUD comparison is conditioned on survival to the second randomization
- **last_verified** 2026-09-17

## 8. Validation status

| Test set | Questions | Correct | Partial | Incorrect | Weighted score |
|---|---:|---:|---:|---:|---:|
| Development coverage set from `AlcHepNet_Concept_Index_Derivation.md` | 20 | 20 | 0 | 0 | 100% |
| Independent extension set before additions above | 5 | 0 | 5 | 0 | 50% |
| Combined initial test | 25 | 20 | 5 | 0 | 90% |
| Combined retest after additions | 25 | 25 | 0 | 0 | 100% |

**Interpretation:** the first 20 questions verify intended coverage because they were used to derive the original 15 concepts. The five-question extension set provides a limited generalization check. These results apply to the pre-ITAALD content only. ITAALD concepts 21–28 received source-traceability review but have not yet been evaluated with an independent question set. These results measure document-level routing and traceability, not performance of a deployed AI model.
