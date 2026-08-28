# Concept Index Derivation — 20 Representative Questions

These 20 questions were selected from the existing OBS/RCT/MOP evaluation question sets and from the cross-source data-location questions now required by the umbrella. They intentionally emphasize questions that need a source definition plus a DD/physical-data mapping.

| # | Representative question | Needed concept(s) | Why it belongs in Concept Index |
|---:|---|---|---|
| 1 | What is Day 0 in the observational study, and where is it represented in the released data? | Day 0 / index visit | protocol meaning + physical timepoint mapping |
| 2 | What is Day 0 in the RCT, and where is it represented in the released data? | Day 0 / index visit | same wording, different protocol meaning |
| 3 | Where can I find baseline MELD? | baseline MELD | definition + exact table.column + baseline selection rule |
| 4 | What MELD range is required for RCT eligibility, and is that the same as the stored MELD stratum? | MELD; RCT MELD stratum | distinguishes numeric score from category |
| 5 | What is the RCT primary endpoint, and which released field stores Day-90 status? | 90-day survival | protocol endpoint + physical mapping |
| 6 | Where is 180-day survival stored? | 180-day survival | time-specific outcome mapping |
| 7 | Where is AKI stored, and which field should I use for Day 90 versus overall AKI? | AKI | multiple fields require usage rule |
| 8 | Which field identifies the randomized treatment arm? | RCT treatment arm | protocol arm definition + `case.actarm` |
| 9 | Which field distinguishes AH cases, heavy-drinking controls, and healthy controls? | observational cohort | protocol groups + raw encoding |
| 10 | What field should I use for sex versus gender? | sex/gender | two related but non-identical fields |
| 11 | Where do I find BMI at baseline or a later visit? | BMI; visit day | visit-scoped variable mapping |
| 12 | Where are TLFB alcohol-consumption values stored? | TLFB/alcohol consumption | protocol schedule + multiple physical fields |
| 13 | How do I identify the scheduled visit for a follow-up row? | visit day/follow-up | exact timepoint fields and trap about actual date |
| 14 | Which table contains specimen type? | specimen type/aliquot | MOP concept + aliquot entity mapping |
| 15 | How do I connect an aliquot to the visit where it was collected? | submitter IDs / joins | relationship path and FK rule |
| 16 | How do I find a molecular-test result and its units? | molecular/lab result | test name + value + unit required together |
| 17 | Is a repeated `follow_ups.submitter_id` a duplicate record problem? | submitter identifier / join key | distinguishes row ID from foreign key |
| 18 | Does an empty `tlfb_collected` mean TLFB was not collected? | TLFB + physical availability | physical trap requiring profile check |
| 19 | If the protocol says a specimen is collected, does that prove the specimen exists in the release? | specimen type / source authority | protocol versus physical-data authority |
| 20 | If DD defines a field, does that prove it is populated in this release? | source authority / physical availability | schema versus physical-data boundary |

## Selected first-draft Concept Index entries
The recurring concepts above were merged into 15 high-value entries:
1. baseline MELD
2. Day 0 / index visit
3. follow-up visit / visit day
4. 90-day survival
5. 180-day survival
6. AKI
7. RCT treatment arm
8. observational cohort / participant group
9. RCT MELD stratum
10. sex / gender
11. BMI
12. alcohol consumption / TLFB
13. specimen type / aliquot
14. molecular/laboratory test result
15. submitter identifier / join key
