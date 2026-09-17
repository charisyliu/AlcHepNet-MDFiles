---
id: itaald_protocol_kb_v2
type: study_knowledge
study: ITAALD-01
title: "ITAALD Protocol Knowledge Base"
source: "Sponsor signed-ITAALD Protocol v2 05-22-2025 Clean (1)(1).pdf"
source_version: "Protocol Version 2"
protocol_date: "2025-05-22"
signed_approval_date: "2025-07-23"
irb: "Pro00081215"
ind: "176797"
last_verified: "2026-09-17"
---

# ITAALD Protocol Knowledge Base

## 1. Purpose and authority

This KB represents the signed Version 2 protocol for the Integrated Therapies for Alcohol use in Alcohol-associated Liver Disease trial. Use it for study design, eligibility, intervention, schedule, endpoint definition, safety, and operational questions. Use the ITAALD SAP KB for formal statistical-analysis rules. Use the data dictionary and physical-data profile to determine field names and actual released data availability.

Do not use this KB to infer that a protocol-defined assessment or specimen is present in an ARDaC release.

## 2. Study identity

| Item | Protocol specification |
|---|---|
| Full title | Integrated Therapies for Alcohol use in Alcohol-associated Liver Disease trial |
| Short name | ITAALD / ITAALD-01 |
| Phase and design | Phase 2B, prospective, multicenter, sequentially randomized controlled trial |
| Sponsor framework | AlcHepNet, funded by NIAAA |
| Sites | Indiana University, Mayo Clinic, Virginia Commonwealth University, Cleveland Clinic Foundation, University of Louisville, University of Texas Southwestern Medical Center |
| Planned enrollment | 216 participants; target 36 per site |
| Population | Hospitalized adults with steroid-eligible severe alcohol-associated hepatitis |
| Treatment phase | Up to 6 months |
| Follow-up | Up to 2 years |
| Central support | Indiana University Data Coordinating Center; DCC also manages the biorepository |
| Oversight | Advarra single IRB and NIAAA-appointed DSMB |

## 3. Objectives

### Primary objective

Determine whether an AUD-directed intervention integrated with sAH therapy improves the six-month composite of alcohol- and liver-related events compared with usual care for AUD.

### Secondary objectives

- Compare 90-day survival for F-652 versus up to 28 days of prednisone, with the Day-7 Lille stopping rule.
- Compare one-year overall survival for IL-22 versus prednisone, with or without acamprosate.

## 4. Trial design and sequential randomization

ITAALD resembles a 2-by-2 factorial trial, but the two randomizations occur at different times.

### Stage 1 on Day 1

- Randomize all eligible participants 1:1 to F-652 or prednisone.
- This sAH-treatment comparison is double-blinded and placebo controlled.
- Participants assigned to F-652 also receive prednisone placebo.
- Participants assigned to prednisone also receive F-652 placebo.
- Prednisone or prednisone placebo is stopped when the Day-7 Lille score is greater than 0.45.

### Stage 2 on Day 7 or discharge

- Only participants surviving to the second randomization enter Stage 2.
- Randomize 1:1 to the AUD intervention or usual care.
- AUD treatment begins at hospital discharge or Day 7, whichever occurs first.
- The AUD intervention cannot be blinded because it contains behavioral treatment.

### Four treatment combinations

| Arm | sAH treatment | AUD treatment |
|---|---|---|
| 1 | F-652 on Days 1 and 7 plus prednisone placebo | Acamprosate for 6 months, inpatient MI, and four MET sessions during the first 3 months |
| 2 | F-652 on Days 1 and 7 plus prednisone placebo | Usual care for AUD |
| 3 | Prednisone for up to 28 days plus F-652 placebo on Days 1 and 7 | Acamprosate for 6 months, inpatient MI, and four MET sessions during the first 3 months |
| 4 | Prednisone for up to 28 days plus F-652 placebo on Days 1 and 7 | Usual care for AUD |

Usual care is a brief intervention advising abstinence plus referral to a 12-step program.

### Randomization implementation

- The DCC generates the randomization code and assigns treatment through Advarra EDC.
- Stage 1 is stratified by site and MELD score.
- The protocol lists MELD strata as 20–25 and 26–30.
- The protocol first mentions blocks of size 4 and later random block sizes of 4 and 6.
- Stage 2 randomizes survivors in equal proportions within the Stage-1 groups.

### Blinding

- Stage 1 is double-blinded.
- Stage 2 is open-label because MI and MET cannot be concealed.
- Authorized DCC personnel and pharmacy staff maintain treatment codes as specified by the protocol.
- Emergency unblinding is coordinated through the designated study physician, site investigator/sub-investigator, and DCC.
- Participants unblinded during Phase 1 are removed from study treatment; data after unblinding are not used in analyses.

## 5. Study treatments

| Product | Protocol dosing |
|---|---|
| F-652 or placebo | 60 mcg/kg in 100 mL IVPB over 1 hour on Days 1 and 7 |
| Prednisone or placebo | 40 mg orally daily on Days 1–28, represented as two 20 mg tablets; stop prednisone or placebo if Day-7 Lille >0.45 |
| Acamprosate | Three 333 mg tablets orally twice daily from Day 7/discharge through Day 180 |
| Motivational interviewing | One approximately 20–30 minute session during the index admission before discharge |
| Motivational enhancement therapy | Four approximately 60-minute sessions, in person or by telehealth, during the first 3 months |

The PDF text renders the F-652 dose as `60 mCg/kg`; this KB normalizes that typography to `60 mcg/kg` but does not independently validate the dose against the pharmacy manual or investigator brochure.

## 6. Eligibility

### Inclusion criteria

1. Age at least 18 and younger than 70.
2. MELD 20–35 on the day of randomization.
3. Definitive or probable AH by NIAAA criteria, including:
   - jaundice onset, defined as total bilirubin above 3 mg/dL, within the prior 8 weeks;
   - ongoing alcohol consumption above 40 g/day for females or 60 g/day for males for at least 6 months;
   - less than 8 weeks of abstinence before jaundice onset;
   - AST above 50 IU/L;
   - AST:ALT ratio above 1.5;
   - AST and ALT below 400 IU/L;
   - and/or histologic evidence of AH.
4. Negative serum or urine pregnancy test at screening for participants of childbearing potential.

When diagnosis is uncertain or competing causes exist, a standard-of-care liver biopsy may be used to confirm AH and exclude competing etiologies.

### Exclusion criteria

1. Active liver-transplant listing before screening.
2. MELD below 20 or above 35.
3. Uncontrolled infection after 48 hours of antibiotic therapy.
4. Progressive hemodynamic compromise requiring IV pressors.
5. Pneumonia on clinical and radiologic assessment.
6. eGFR below 35 mL/min.
7. Clinically active C. difficile infection.
8. Other active liver disease, including autoimmune, cholestatic, ischemic, sepsis-induced, or drug-induced disease.
9. Cancer other than non-melanoma skin cancer.
10. More than 2 days of systemic corticosteroid or immunosuppressive therapy in the prior 30 days.
11. Current naltrexone or acamprosate use.
12. Clinically significant pancreatitis as defined in the protocol.
13. Active GI bleeding meeting protocol hemodynamic or hemoglobin criteria.
14. Significant uncontrolled concomitant illness or progressive multiorgan failure.
15. Uncontrolled mental illness.
16. Uncontrolled HBV, HIV, or HCV with persistent viremia; protocol-specified controlled infections may be eligible.
17. Active illicit opiate, cocaine, ketamine, or methamphetamine use within 30 days.
18. Uncontrolled diabetes with HbA1c above 9%.
19. Pregnancy or breastfeeding.
20. Allergy or intolerance to study agents.
21. Unwillingness to stop alcohol use or undergo AUD treatment.
22. Unwillingness to use protocol-acceptable contraception during treatment and for at least 30 days after the last study-medication dose.
23. Any investigator-determined condition affecting safety, adherence, interpretability, bias, or suitability.

## 7. Study schedule

| Visit | Window | Key protocol activities |
|---|---:|---|
| Screening | Up to 2 days before Day 1 | Consent, eligibility, history/exam, vitals, anthropometrics, AUDIT, TLFB, PACS, PHQ-9, GAD-7, medications, ECG, safety labs, pregnancy test |
| Day 1 | Index randomization | sAH randomization, F-652/placebo and prednisone/placebo, clinical assessment, lipids, HbA1c, PEth, pregnancy test, specimen banking |
| Day 7 | ±1 day | Second treatment dose, Lille rule, AUD randomization, MI/acamprosate start at discharge or Day 7, assessments, ECG, compliance, specimen banking |
| Day 14 | ±5 days | MET session |
| Day 30 | ±7 days | Clinical assessment, PACS/PHQ-9/GAD-7, ECG, safety labs, PEth, pregnancy test, specimen banking, MET |
| Day 60 | ±14 days | MET session |
| Day 90 | ±14 days | Clinical assessment, TLFB/PACS/PHQ-9/PROMIS-29, ECG, safety labs, PEth, pregnancy test, specimen banking, MET |
| Day 180 | ±14 days | Clinical assessment, TLFB/AUDIT/PACS/PHQ-9/PROMIS-29, ECG, labs, lipids, HbA1c, PEth, pregnancy test, specimen banking |
| Day 360 | ±28 days | Survival verification; TLFB if telehealth visit occurs |
| Day 720 | ±28 days | Survival verification; TLFB if telehealth visit occurs |

When possible, participants fast at least 8 hours before clinic visits; water is permitted.

## 8. Endpoints

### Primary composite endpoint

Occurrence within 6 months after the first randomization of any of the following:

- death from any cause;
- liver transplant;
- new clinically detectable ascites;
- hepatic encephalopathy of New Haven grade 2 or higher;
- portal hypertensive bleeding due to gastroesophageal varices or portal gastropathy;
- liver-related hospital admission for ascites, hepatic encephalopathy, infection, or GI bleeding;
- MELD increase greater than 5 points;
- return to alcohol drinking, defined as less than 100% abstinence.

The composite is met when any component occurs. The protocol also states that treatment effects will be assessed using time from treatment initiation to occurrence of the composite.

### Secondary endpoints

- Overall survival at Days 30, 90, and 180 and Years 1 and 2.
- Transplant-free survival at the same time points.

### Exploratory clinical endpoints

- Change in MELD score.
- AKI.
- Multiorgan failure.
- ICU transfer.
- Infection and sepsis.

### Alcohol-use endpoints

- Percent days abstinent.
- Drinks per week.
- Drinks per drinking day.
- Percent heavy-drinking days.
- Percent with no heavy-drinking days.
- Percent abstinent.
- WHO one-level and two-level reductions.
- Percent with negative blood PEth.

Two retrospective 90-day TLFB assessments at Days 90 and 180 cover the first 6 months. A heavy-drinking day is at least 4 drinks for women or at least 5 drinks for men.

### Patient-reported outcome

PROMIS-29 assesses quality of life at Days 90 and 180 in the protocol schedule. Interpretation is limited to survivors observed at those visits and does not represent the originally randomized group as a whole.

## 9. Biospecimens

- Planned collection visits: Days 1, 7, 30, 90, and 180.
- Core banked specimens: fasting whole blood for DNA, serum, plasma, and urine.
- PBMC and stool are collected when feasible.
- PBMC, stool, and other collection details may vary by site.
- Protocol collection requirements do not establish physical availability in ARDaC.

## 10. Safety and discontinuation

- AE collection begins on Day 1 and continues through the end of treatment at Day 180.
- Focused risks include infection, drug-induced liver injury, injection-site reactions, and hematologic events.
- Investigators determine seriousness, severity, expectedness, and relationship to treatment.
- The DSMB reviews safety and may recommend trial modification or termination.
- Unscheduled safety visits and repeat assessments may be performed when clinically warranted.
- Participants discontinuing treatment may continue study assessments and survival follow-up unless they withdraw consent.

## 11. Protocol statistical summary

- Planned enrollment: 216.
- Anticipated complete six-month assessments: 192 after 10% attrition.
- Target power: 82% for each main treatment comparison under the protocol assumptions.
- Main-effect alpha: 0.025 for each of the two primary treatment comparisons using Bonferroni control.
- One safety interim analysis occurs when 50% complete 90-day follow-up.
- F-652 is stopped for future participants if 90-day survival is significantly worse than prednisone; there is no stop for positive efficacy.

Formal analysis populations, models, missing-data rules, and safety summaries are governed by the ITAALD SAP KB.

## 12. Known conflicts and gaps

| ID | Issue | Protocol evidence | Handling |
|---|---|---|---|
| ITAALD-P-001 | MELD randomization strata do not cover the full eligible range | Eligibility is MELD 20–35; randomization text lists 20–25 and 26–30 | Do not assign participants with MELD 31–35 to a stratum without clarification or the executable randomization specification |
| ITAALD-P-002 | Block-size description differs within the protocol | One passage says blocks of 4; another says random block sizes of 4 and 6 | Treat the DCC randomization specification as operational authority; request confirmation before reproducing the sequence |
| ITAALD-P-003 | Primary endpoint representation differs from SAP method | Protocol describes time to first composite event; SAP primary analysis compares event rates at Day 180 | Preserve both; SAP governs prespecified analysis, but reconciliation/estimand clarification is required |
| ITAALD-P-004 | PROMIS-29 timing differs between sources | Protocol schedule includes Days 7, 90, 180; SAP narrative emphasizes Day 90 | Use the schedule for collection and SAP for analysis until clarified |
| ITAALD-P-005 | Some specimen collections are site-dependent | PBMC and stool are feasible/site-specific | Verify site and release before treating absence as missingness |

## 13. Source navigation

| Question | Protocol location |
|---|---|
| Identity, design, arms, endpoints | Executive Summary, pp. 14–19 |
| Schedule of events | Table 1, pp. 20–21 and pp. 65–66 |
| Eligibility | Executive Summary, pp. 18–19 |
| Dosing and blinding | Study Products and Dose Administration, pp. 55–60 |
| Randomization and unblinding | pp. 60–63 |
| Visit procedures | pp. 64–70 |
| Endpoint definitions and specimen banking | pp. 70–72 |
| Safety | pp. 72–79 |
| Statistical methods | pp. 87–92 |

