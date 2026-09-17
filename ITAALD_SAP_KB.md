---
id: itaald_sap_kb_v1_0
type: statistical_analysis_knowledge
study: ITAALD-01
title: "ITAALD Statistical Analysis Plan Knowledge Base"
source: "ITAALD SAP-03-31-25 Final(1).docx"
source_version: "SAP Version 1.0"
sap_date: "2025-03-31"
approval_reference: "Approved at protocol finalization on 2025-03-27"
last_verified: "2026-09-17"
---

# ITAALD Statistical Analysis Plan Knowledge Base

## 1. Purpose and authority

This KB represents ITAALD SAP Version 1.0. Use it for analysis populations, power, multiplicity, endpoint methods, safety analyses, interim monitoring, and missing-data rules. Use the signed Version 2 protocol KB for study conduct, eligibility, intervention, and collection schedules.

When the SAP and later signed protocol disagree, do not silently merge them. Record the discrepancy and obtain an approved amendment or statistical clarification.

## 2. Analysis framework

| Item | SAP rule |
|---|---|
| Design | Prospective, multicenter, sequentially randomized trial resembling a 2-by-2 factorial design |
| Enrollment | 216 participants |
| Stage 1 | F-652 versus prednisone on Day 1 |
| Stage 2 | AUD intervention versus usual care among Day-7 survivors |
| Primary assessment | Composite-event status at Day 180 |
| Main treatment effects | F-652 versus prednisone; AUD intervention versus usual care |
| Interaction | Exploratory F-652-by-AUD-treatment interaction |
| Type I error | Two main comparisons tested at two-sided alpha 0.025 each via Bonferroni control |

## 3. Analysis populations

### Intention-to-treat population

The primary analytical population includes randomized trial participants according to randomized assignment.

### Modified intention-to-treat population

The SAP defines mITT as randomized participants who received at least one dose of F-652. This wording is asymmetric because it does not state an equivalent exposure rule for prednisone or the second-stage AUD treatment. Preserve the definition as written and seek clarification before programming.

### Per-protocol population

Exploratory PP analysis includes participants who received the full intervention dose. The SAP does not fully specify deviations, adherence thresholds, or separate rules for the sAH and AUD interventions.

### Safety population

The SAP describes safety summaries by treatment group but does not provide a separate formal safety-population definition. Confirm whether treatment-emergent summaries use all treated participants and how the two randomization stages are represented.

## 4. Primary endpoint and estimand components

### Endpoint

The primary endpoint is occurrence by Day 180 of any component of the six-month composite:

- all-cause death;
- liver transplant;
- new clinically detectable ascites;
- hepatic encephalopathy;
- portal hypertensive bleeding;
- liver-related hospital admission;
- MELD increase greater than 5 points;
- return to alcohol drinking, defined as less than complete abstinence.

### Treatment contrasts

1. F-652 versus prednisone, stratified by AUD-treatment assignment.
2. AUD intervention versus usual care, stratified by sAH-treatment assignment.

### Primary method

- Compare composite-event rates with the Cochran-Mantel-Haenszel test.
- F-652 comparison uses AUD treatment as the stratification variable.
- AUD comparison uses F-652 versus prednisone as the stratification variable.
- An alternative implementation is logistic regression containing indicators for both treatments.
- The treatment interaction is exploratory.

### Intercurrent events and interpretation

- Death and transplant are components rather than censoring events.
- The SAP does not fully define handling of withdrawal, second-stage non-randomization, premature treatment discontinuation, rescue treatment, or incomplete ascertainment as estimand strategies.
- Because only Day-7 survivors receive the second randomization, the AUD comparison applies to the survivor population eligible for Stage 2, not all Day-1 randomized participants.

## 5. Sample size and power

- Recruit 216 participants over approximately 36 months.
- Assume 10% attrition, leaving 192 with complete six-month assessment.
- For F-652 versus prednisone, assumed prednisone composite-event rate is 0.45–0.65.
- For AUD intervention versus usual care, assumed usual-care rate is 0.50–0.55.
- Target power is 82% to detect odds ratios approximately 0.36–0.38.
- Each main-effect test uses two-sided alpha 0.025.
- Stratification follows the other randomized intervention.

## 6. Secondary endpoint analyses

Secondary endpoints are overall and transplant-free survival at Days 30, 90, and 180 and Years 1 and 2.

The SAP states:

- compare fixed-time rates using Cochran-Mantel-Haenszel methods;
- generate Kaplan-Meier curves;
- use log-rank tests for survival distributions;
- estimate hazard ratios using Cox proportional-hazards models, with baseline-covariate adjustment as needed.

The SAP does not give a hierarchical testing sequence or multiplicity adjustment for secondary endpoints. Treat these analyses as secondary and interpret inferential p-values accordingly unless an approved amendment supplies a hierarchy.

## 7. Exploratory analyses

### Clinical events

| Outcome | Planned methods |
|---|---|
| Event rates at fixed time points | Fisher exact or Cochran-Mantel-Haenszel tests |
| Time to clinical event | Kaplan-Meier, Cox models |
| Competing-risk outcomes | Cumulative-incidence functions and Fine-Gray subdistribution-hazard models |
| Longitudinal MELD and liver-function measures | Linear mixed-effects models with repeated measurements and baseline adjustment |
| AKI, multiorgan failure, SIRS, ICU transfer | Logistic regression for binary outcomes; time-to-event and competing-risk methods where applicable |
| Sepsis and infection outcomes | Chi-square or Fisher exact tests; multivariable logistic regression; sensitivity analyses using alternative sepsis definitions |
| Renal progression | Binary or ordinal logistic regression; survival and competing-risk methods for persistence or resolution |

Model covariates are described generally rather than exhaustively. Pre-specify exact covariates, functional forms, proportional-hazards checks, competing events, and repeated-measure covariance structures in programming specifications.

### Alcohol-use outcomes

TLFB at Days 90 and 180 covers baseline through six months.

| Outcome type | Examples | Planned method |
|---|---|---|
| Count | Drinks/week; drinks/drinking day | Mixed-effects Poisson regression |
| Percentage | Percent days abstinent; percent heavy-drinking days | Mixed-effects logistic regression as stated in SAP |
| Participant-level binary | Abstinent; no heavy-drinking days; WHO shift; negative PEth | Logistic regression |

Models include treatment indicators and participant characteristics as fixed effects and random participant effects for within-participant correlation. Distributional fit and the exact representation of percentage outcomes require prespecification.

### Patient-reported outcomes

- PROMIS-29 is exploratory.
- The SAP narrative emphasizes Day 90.
- Mixed-effects analysis uses PROMIS-29 score as the response.
- Fixed effects include sAH treatment, AUD treatment, measurement time, and selected patient characteristics such as age, sex, race, and baseline MELD.
- Random participant effects account for repeated observations.
- Adjusted mean differences compare groups at specified times.
- Inference applies to survivors observed at the assessment time, not the randomized population as a whole.

## 8. Interim analysis

- Trigger: 50% of participants have completed 90-day follow-up.
- Comparison: F-652 versus prednisone for overall 90-day survival.
- Purpose: safety/futility against inferior F-652 performance.
- Test: two-sided continuity-corrected Cochran-Mantel-Haenszel Z-test at alpha 0.05.
- Action: stop F-652 for future enrollment if significantly worse than prednisone; future participants receive prednisone.
- No early stop for positive efficacy.
- No alpha adjustment is planned because the interim analysis is safety-only and cannot stop for benefit.
- Unblinded statisticians conduct the analysis and report to the DSMB; investigators and coordinators remain blinded unless disclosure is necessary for safety.

The SAP describes a comparison of “time to all-cause mortality” using a CMH test, which ordinarily compares stratified proportions rather than full time-to-event distributions. The exact interim endpoint statistic and stratification variables require an executable interim-analysis specification.

## 9. Safety analyses

- Summarize AEs, SAEs, laboratory results, physical examinations, and other safety outcomes by treatment group.
- Define TEAE as an AE newly appearing, increasing in frequency, or worsening after study-medication initiation.
- Tabulate TEAEs by system organ class, preferred term, severity, relationship, treatment discontinuation, and seriousness.
- Compare proportions using Fisher exact tests and report odds ratios with 95% confidence intervals where specified.
- Assess continuous laboratory change with ANCOVA using baseline as a covariate and Type III sums of squares.
- Two-sided safety p-values are flagging tools and should not be over-interpreted.

The SAP does not fully specify coding-dictionary version, treatment-emergent window, repeated-event counting, denominator rules across the two randomizations, or laboratory shift-table rules.

## 10. Missing data

### Composite endpoint

- Use medical-record review, death records, registries, local searches, and other sources to minimize missing clinical events.
- Do not impute missing composite-endpoint values.
- Analyze and present observed values only.

The SAP does not state whether the primary denominator is all randomized participants, all participants with observable Day-180 status, or another set when any component is unknown. This must be clarified because complete-case analysis can conflict with an ITT analysis.

### TLFB outcomes

- Follow imputation practices from prior AUD-intervention trials.
- Assess robustness by changing the imputation method.

The exact primary TLFB imputation algorithm, missing-day rules, dropout assumptions, and sensitivity scenarios are not specified in the SAP and require a separate programming rule or amendment.

### Other endpoints

No complete missing-data strategy is provided for longitudinal MELD, PROMIS-29, laboratory outcomes, or time-to-event endpoints. Define censoring and model assumptions before analysis.

## 11. Data quality and presentation

- Apply logic and consistency checks.
- Use site training, monitoring, manuals, verification, cross-checking, and audits.
- Provide monthly performance reports.
- Summarize baseline characteristics by treatment group in the ITT population.
- Do not perform formal baseline comparisons unless otherwise stated.

The SAP mentions tables of TEAEs and descriptive summaries but does not include a complete table, figure, and listing shell package.

## 12. Statistical decision table

| Question | Governing SAP rule |
|---|---|
| Primary analysis population | ITT |
| Primary endpoint time point | Day 180 / six months |
| Main sAH comparison | F-652 vs prednisone, stratified by AUD treatment |
| Main AUD comparison | Acamprosate + MI + MET vs usual care, stratified by sAH treatment |
| Primary test | CMH test; logistic regression is an alternative implementation |
| Main-effect alpha | 0.025 per comparison |
| Interaction | Exploratory |
| Survival methods | Fixed-time CMH plus Kaplan-Meier, log-rank, and Cox models |
| Competing risks | Cumulative incidence and Fine-Gray methods |
| Longitudinal continuous outcomes | Linear mixed-effects models |
| Count alcohol outcomes | Mixed-effects Poisson models |
| Binary alcohol outcomes | Logistic regression |
| Composite missing values | No imputation; observed values only |
| TLFB missing values | Prior-trial imputation plus alternative sensitivity analyses; exact algorithm not specified |

## 13. Known conflicts and unresolved analysis gaps

| ID | Issue | Evidence | Required resolution |
|---|---|---|---|
| ITAALD-S-001 | Protocol uses time-to-first composite language; SAP primary method uses Day-180 event rates | Protocol endpoint section vs SAP primary analysis | Define the primary estimand and whether time-to-event is primary, supportive, or exploratory |
| ITAALD-S-002 | mITT definition is asymmetric | mITT includes participants receiving at least one dose of F-652 | Supply treatment-neutral mITT rules or confirm intended F-652-specific analysis |
| ITAALD-S-003 | Second-stage survivor population is not fully integrated into ITT language | Only Day-7 survivors are randomized to AUD treatment | Define Stage-2 analysis set, treatment assignment for deaths before Day 7, and denominator |
| ITAALD-S-004 | Primary missing-data denominator is unclear | ITT stated; composite missing values not imputed and observed only | Specify analysis denominator and sensitivity analyses |
| ITAALD-S-005 | TLFB imputation is not executable | Refers to prior trials without algorithm | Provide exact imputation and sensitivity procedures |
| ITAALD-S-006 | Interim statistic terminology is inconsistent | CMH Z-test described for time to death | Provide interim-analysis programming specification |
| ITAALD-S-007 | Secondary multiplicity is not specified | Multiple time points and contrasts | State whether secondary inferences are nominal, hierarchical, or adjusted |
| ITAALD-S-008 | Randomization-block language conflicts | Blocks of 4 and random blocks of 4/6 both appear | Use executable DCC randomization specification |
| ITAALD-S-009 | SAP metadata predates signed protocol | SAP lists IRB/IND pending; signed protocol provides identifiers | Use signed protocol identifiers for study operations; retain SAP version/date for analysis provenance |
| ITAALD-S-010 | PROMIS-29 timing differs | Protocol schedule includes Days 7/90/180; SAP narrative emphasizes Day 90 | Separate collection schedule from prespecified analysis time point and clarify longitudinal analysis inputs |

