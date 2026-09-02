# AlcHepNet Umbrella KB Regression Test Set

## Development Coverage Questions

1. What is Day 0 in the observational study, and where is it represented in the released data?
2. What is Day 0 in the RCT, and where is it represented in the released data?
3. Where can I find baseline MELD?
4. What MELD range is required for RCT eligibility, and is that the same as the stored MELD stratum?
5. What is the RCT primary endpoint, and which released field stores Day-90 status?
6. Where is 180-day survival stored?
7. Where is AKI stored, and which field should I use for Day 90 versus overall AKI?
8. Which field identifies the randomized treatment arm?
9. Which field distinguishes AH cases, heavy-drinking controls, and healthy controls?
10. What field should I use for sex versus gender?
11. Where do I find BMI at baseline or a later visit?
12. Where are TLFB alcohol-consumption values stored?
13. How do I identify the scheduled visit for a follow-up row?
14. Which table contains specimen type?
15. How do I connect an aliquot to the visit where it was collected?
16. How do I find a molecular-test result and its units?
17. Is a repeated `follow_ups.submitter_id` a duplicate-record problem?
18. Does an empty `tlfb_collected` mean TLFB was not collected?
19. If the protocol says a specimen is collected, does that prove it exists in the release?
20. If the DD defines a field, does that prove it is populated in this release?

## Independent Extension Questions

21. Where is Lille score stored, and how does it affect treatment at Day 7?
22. Where are infection screening and culture results, and is screening equivalent to confirmed infection?
23. Where is hepatic encephalopathy stored, and what severity does the field represent?
24. How often are specimens shipped, and does that prove a shipment record exists in the release?
25. Are PBMCs expected for every participant, and how should PBMC absence be interpreted?

## Scoring Form

| Question ID | Correct authority | Correct study/visit context | Correct field/physical location | Necessary trap or gap | Unsupported claim | Overall status | Notes |
|---|---|---|---|---|---|---|---|
| | Yes / Partial / No | Yes / Partial / No / N/A | Yes / Partial / No / N/A | Yes / No / N/A | Yes / No | Correct / Partial / Incorrect | |

