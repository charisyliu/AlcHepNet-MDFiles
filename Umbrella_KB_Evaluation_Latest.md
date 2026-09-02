# AlcHepNet Umbrella Knowledge Base Evaluation and Error Log

**Evaluation date:** 2026-09-02  
**Evaluated file:** `AlcHepNet_Umbrella_KB_Final.md`  
**Supporting files:** `AlcHepNet_Concept_Index_Derivation.md`, `AlcHepNet_Physical_Data_KB_Final.md`, `AlcHepNet_submitter_id_QC.numbers`, and `generate_physical_data_kb.py`.

## 1. Evaluation Design

The evaluation was separated into two parts to avoid overstating performance:

1. **Development coverage set:** the 20 representative questions documented in `AlcHepNet_Concept_Index_Derivation.md`. These questions were used to build the original 15-entry Concept Index, so they test whether the intended mappings were implemented, not independent generalization.
2. **Independent extension set:** five new questions covering Lille score, infection, hepatic encephalopathy, specimen shipping, and PBMC availability. These concepts were not standalone entries in the original 15-entry index and therefore provide a limited generalization test.

For each question, the minimum passing route had to include the correct authority, study context, exact field or physical location when verified, a usage rule, and any necessary trap or unresolved-gap warning.

## 2. Scoring Rubric

| Status | Definition | Score |
|---|---|---:|
| Correct | Directly routes to the correct authority/location and preserves the required warning | 1.0 |
| Partial | Reaches a relevant family/source, but a direct field, rule, study distinction, or warning is missing | 0.5 |
| Incorrect | Misroutes, conflates concepts, or requires unsupported inference | 0.0 |

## 3. Results

| Test stage | Correct | Partial | Incorrect | Weighted score |
|---|---:|---:|---:|---:|
| Development coverage set | 20/20 | 0/20 | 0/20 | 100% |
| Extension set before revision | 0/5 | 5/5 | 0/5 | 50% |
| Combined initial evaluation | 20/25 | 5/25 | 0/25 | 90% |
| Combined retest after revision | 25/25 | 0/25 | 0/25 | 100% |

The 100% development-set score is expected because those questions generated the original index. The more informative result is that all five extension questions were initially only partial. They could reach a broad routing family, but lacked the same direct “definition → location → rule → trap” treatment as the original 15 concepts.

## 4. Development Coverage Test Log

| ID | Test Question | Expected Route | Initial Status | Evidence / Result | Retest |
|---|---|---|---|---|---|
| D01 | What is Day 0 in OBS, and where is it represented? | OBS protocol → Concept 2 → follow-up day 0 | Correct | Study meaning and physical selection rule both present | Pass |
| D02 | What is Day 0 in RCT, and where is it represented? | RCT protocol → Concept 2 → follow-up day 0 | Correct | Randomization/baseline distinction and encoding trap present | Pass |
| D03 | Where can I find baseline MELD? | Concept 1 → OBS/RCT follow-up files → `meld_score` at day 0 | Correct | Exact files, field, and baseline rule present | Pass |
| D04 | What MELD range is required for RCT eligibility, and is it the stored stratum? | RCT eligibility + Concepts 1 and 9 | Correct | Numeric MELD and `rct_meld_strata` are explicitly separated | Pass |
| D05 | What is the RCT primary endpoint and released Day-90 field? | RCT endpoint → Concept 4 → `case.days_90_survival` | Correct | Endpoint, field, and overall-vital-status trap present | Pass |
| D06 | Where is 180-day survival stored? | Concept 5 → `case.days_180_survival` | Correct | Direct location and Unknown warning present | Pass |
| D07 | Where is AKI stored for Day 90 versus overall status? | Concept 6 → time-specific case fields | Correct | Correct horizon-selection rule present | Pass |
| D08 | Which field identifies randomized treatment arm? | Concept 7 → `case.actarm` | Correct | Exact field and OBS-empty warning present | Pass |
| D09 | Which field distinguishes observational groups? | Concept 8 → `case.cohort` | Correct | Exact raw encodings and spelling trap present | Pass |
| D10 | What field should I use for sex versus gender? | Concept 10 → `demographic.sex` / `.gender` | Correct | Ambiguity rule and observed difference present | Pass |
| D11 | Where is BMI at baseline or a later visit? | Concept 11 → `follow_up.bmi` + visit row | Correct | Visit-specific selection rule present | Pass |
| D12 | Where are TLFB alcohol values stored? | Concept 12 → `follow_up.tlfb_*` | Correct | Quantitative fields and empty-indicator trap present | Pass |
| D13 | How do I identify a scheduled follow-up visit? | Concept 3 → `visit_day` / `days_to_follow_up` | Correct | OBS/RCT observed days and nominal-day trap present | Pass |
| D14 | Which table contains specimen type? | Concept 13 → `aliquot.specimen_type` | Correct | Protocol/MOP/DD/physical authority sequence present | Pass |
| D15 | How do I connect an aliquot to collection visit? | Concepts 13 and 15 → `follow_ups.submitter_id` | Correct | Row ID versus parent-FK distinction present | Pass |
| D16 | How do I find molecular-test result and units? | Concept 14 → test/value/unit fields | Correct | Assay and unit must be interpreted together | Pass |
| D17 | Is repeated `follow_ups.submitter_id` a duplicate-record problem? | Concept 15 + Physical Data Profile | Correct | Parent IDs are expected to repeat; row IDs are separate | Pass |
| D18 | Does empty `tlfb_collected` prove TLFB was not collected? | Concept 12 + physical profile | Correct | Empty indicator versus populated values explicitly handled | Pass |
| D19 | Does protocol collection prove a specimen exists in the release? | Concept 13 + authority table | Correct | Protocol, MOP, DD, and physical evidence boundaries stated | Pass |
| D20 | Does a DD field prove it is populated? | Source authority table + Physical Data Profile | Correct | Schema-versus-physical boundary explicit | Pass |

## 5. Independent Extension Error Log

| ID | New Test Question | Expected Minimum Route | Initial Result | Status | Error / Potential Reason | Improvement Made | Retest |
|---|---|---|---|---|---|---|---|
| E01 | Where is Lille score stored, and how does it affect treatment at Day 7? | RCT Lille rule → `follow_up.lille_score` → Day-7 context and threshold warning | Routing table reached RCT/statistics, but no standalone concept route | Partial | Concept not among the original 15; field and visit rule were not surfaced together | Added Concept 16 with field, visit, treatment rule, and OBS warning | Pass |
| E02 | Where are infection screening and culture results, and is screening equivalent to confirmed infection? | OBS/RCT definitions → `follow_up` screening/culture fields → warning | Broad endpoint route only | Partial | Clinical event and physical test evidence were not distinguished | Added Concept 17 with result/organism/date rule | Pass |
| E03 | Where is hepatic encephalopathy stored, and what severity does it represent? | Protocol → `follow_up.hep_enceph` and date → grade ≥2 warning | Endpoint and DD routes existed separately, but severity trap was absent | Partial | Variable-level qualifier was not elevated | Added Concept 18 with exact fields and severity | Pass |
| E04 | How often are specimens shipped, and does that prove a shipment record exists? | Protocol timing → MOP procedure → verified physical mapping or unknown | MOP routing worked, but physical-event boundary was indirect | Partial | Procedure and event availability were not joined | Added Concept 19; unverified shipment-event mapping remains unknown | Pass |
| E05 | Are PBMCs expected for every participant, and how should absence be interpreted? | Conditional protocol collection → MOP → aliquot type → missingness warning | Generic specimen route lacked PBMC-specific conditionality | Partial | Missingness mechanism was not preserved | Added Concept 20 with structural-absence warning | Pass |

## 6. Physical Data and `submitter_id` Verification

The final Physical Data KB and generator address the earlier concern about incorrect `*submitter_id` statistics:

- The profile covers exactly 22 TSVs, 88,335 physical rows, and 627 pre-deduplication columns.
- Each physical table is profiled separately instead of combining row identifiers with relationship identifiers.
- A table’s own `*submitter_id` is treated as its row/node ID; fields such as `follow_ups.submitter_id` are foreign keys and are expected to repeat.
- The first aliquot chunk contains 20,000 non-empty, 20,000 distinct row IDs and no duplicated row-ID values—not 10,000 unique IDs.
- Independent non-pandas checks reproduced follow-up OBS 2,140/2,140 distinct, aliquot inventory 50,254/50,254, demographic OBS 1,133/1,133, and case OBS 1,133/1,133.
- The script records hashes, masks identifier examples, reports denominators, checks schema mappings/enums/foreign keys, and marks unavailable authority as `UNKNOWN`.

## 7. Root Causes and Limitations

- The original 20 questions and 15-entry index are not independent, so their perfect score is described as intended coverage.
- General routing handled the five extension concepts, but direct executable entries were missing; Concepts 16–20 close those gaps.
- This remains a manual document-level routing evaluation, not a deployed-model benchmark.
- The latest Umbrella appropriately leaves release-file classification, pinned commit URLs, calendar index dates, and some SAP rules unresolved.
- The next step is to run all 25 questions through the actual interface, preserve verbatim outputs/citations, and have a second reviewer score them independently.

