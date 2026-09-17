---
id: ardac_web_portal_operational_guide
type: operational_guide
title: "ARDaC Web Portal Operational Guide"
organization: "AlcHepNet / Indiana University Data Coordinating Center"
guide_version: "1.0"
last_verified: "2026-09-17"
source_materials:
  - title: "ARDaC Training Slides"
    file: "Training_06242026_final(8).pdf"
    date: "2026-06-24"
  - title: "AlcHepNet ARDaC 2nd Training"
    date: "2026-06-24"
    url: "https://www.youtube.com/watch?v=v17qMbNVs3Y"
---

# ARDaC Web Portal Operational Guide

## Purpose and scope

This guide explains how to access, navigate, filter, inspect, and document work in the Alcohol Research Data Commons (ARDaC) web portal. It is intended for AlcHepNet investigators and authorized users performing data exploration, feasibility assessment, hypothesis development, proposal planning, and review of available clinical, biospecimen, laboratory, and translational data.

Portal exploration does not by itself authorize formal research use or unrestricted downloading of AlcHepNet data. Research use and release require the applicable proposal, approval, and data-access process.

## Portal addresses

| Resource | Address | Use |
|---|---|---|
| Training portal | https://training.ardac.org/ | Practice and training, when available |
| Official portal | https://portal.ardac.org/ | Authorized production access |
| Archived portal | https://archive.portal.ardac.org | Historical portal only |
| ARDaC website | https://ardac.org/ | General project information |
| AlcHepNet website | https://www.alchepnet.org/ | Consortium information |

## Recorded portal versions

The June 24, 2026 training materials identified:

- Portal: `v3.3.4-2026.05`
- Data dictionary: `v2.4.0`

The portal version describes the user interface and application release. The dictionary version describes the underlying entities, fields, relationships, and definitions. Record both versions when documenting reproducible portal work. Confirm the versions displayed in the portal because later releases may differ from this guide.

## 1. Log in

1. Open the official or training portal.
2. Select **Login** in the upper-right corner.
3. Choose the available identity provider, such as CILogon, ORCID, or an institutional provider.
4. Authenticate and authorize the requested identity information.
5. Confirm that the portal returns to the dashboard and displays the expected project access.

If login succeeds but no data are visible:

1. Capture the page and any error message in a screenshot.
2. Record the portal URL, date, time, identity provider, and account email.
3. Contact the ARDaC technical team so account, role, and identity-provider mappings can be reviewed.

Do not send passwords, authentication codes, or other credentials in a support request.

## 2. Understand the dashboard

After login, use the dashboard to confirm the available studies and the overall scale of accessible data.

Common navigation areas include:

- **Dictionary** for data definitions and relationships
- **Exploration** for interactive filtering and record review
- **Files** for file records, manifests, and metadata
- **Query** for structured data queries
- **Workspace** for supported analytical work
- **Profile** for user information
- **Anagine** or report functions for analytics and summary reports

Counts and charts on the dashboard are descriptive views of available portal content. They are not substitutes for an approved analytic dataset.

## 3. Use the Exploration page

The Exploration page is the main routine workflow. Its five principal tabs are:

1. Participants
2. Follow Ups
3. Biospecimens
4. Lab Results
5. Data Files

Each tab generally contains:

- filters on the left
- counts and charts on the right
- a row-level results table below

Use this sequence:

1. Select the data tab that matches the unit of interest.
2. Select the study or project before applying narrower filters.
3. Add demographic, clinical, visit, specimen, laboratory, or file filters.
4. Confirm whether multiple values are combined with **AND** or **OR** logic.
5. Review the updated counts and charts.
6. Inspect the row-level table as a sanity check.
7. Use **Show Empty Columns** when missing or structurally unavailable fields matter.
8. Record the filters and portal/dictionary versions before generating a report or using the result for proposal planning.

### Filtering rules

- Use **AND** when every selected condition must be true.
- Use **OR** when any selected value can qualify.
- Expect counts, charts, and tables to update as filters change.
- Recheck the active tab and study after changing filters.
- Do not interpret an empty field automatically as a negative result.
- Do not assume that similarly named fields have the same meaning across studies.
- Use the dictionary and study protocol to confirm definitions before interpreting a field.

## 4. Participants

Use the Participants tab for participant-level questions such as study membership, demographics, treatment arm, behavioral measures, outcomes, or availability of selected laboratory measures.

Typical filters include:

- project or study
- observational cohort or randomized treatment arm
- sex, race, ethnicity, and clinical site
- alcohol-use measures
- acute kidney injury status and timing
- 90-day or 180-day survival
- availability of laboratory tests

After filtering, verify that the participant count is the intended denominator. If a question is visit-specific, move to the Follow Ups tab rather than treating participant-level availability as a visit-level result.

## 5. Follow Ups

Use the Follow Ups tab for visit-level and longitudinal questions.

Typical filters include:

- study
- visit day or follow-up time point
- MELD, Child-Pugh, Lille, or Maddrey DF values
- clinical status or outcome variables
- alcohol-use measures
- linked laboratory or biospecimen context

Nominal visit day, actual assessment date, and protocol visit window are different concepts. Confirm the field definition and study protocol before using a visit as baseline or assigning a time point.

## 6. Biospecimens

Use the Biospecimens tab to assess whether specimens of a specified type and context appear to be available.

Typical filters include:

- study
- specimen type
- participant or follow-up context
- processing or storage attributes
- assigned laboratory
- shipment or availability status

Use biospecimen results for feasibility assessment only. A protocol collection schedule does not prove that a specimen exists, and a portal record does not by itself confirm that the specimen is releasable for a proposed study.

## 7. Lab Results and translational data

Use the Lab Results tab for clinical or translational assay records.

1. Select the study and laboratory test.
2. Check the unit, specimen context, and visit context.
3. Review missingness and coverage before interpreting a distribution.
4. Avoid combining values across assays, files, or units without confirming compatibility.

Proteomics and other translational measurements may be represented through linked entities such as Protein Expression, Molecular Test, Biospecimen, Participant, and Follow Up. Use the Dictionary or Graph Model to verify the relationship path.

## 8. Survival analysis

When a survival-analysis function is available:

1. Define the cohort in Explorer.
2. Confirm the endpoint, time origin, event coding, and censoring assumptions.
3. Generate the curve or comparison.
4. Record all filters and settings.
5. Treat portal output as exploratory unless an approved protocol or statistical analysis plan specifies formal use.

Overall vital status is not automatically interchangeable with a time-specific endpoint such as 90-day survival.

## 9. Generate an Anagine Summary Report

The Summary Report is generated from the active filtered Explorer cohort.

1. Select the appropriate Explorer tab.
2. Apply and verify all filters.
3. Inspect counts, charts, and row-level records.
4. Select **Summary Report**.
5. Monitor the report status; cancel the job if the cohort or filters are incorrect.
6. Open the completed report.
7. Verify that its run information and filter list match the intended cohort.
8. Save or cite the report only under the applicable data-governance rules.

A report may include run information, selected filters, statistics, completeness summaries, visualizations, analyses, and example records. It is a reproducible snapshot of the selected portal cohort, not independent authorization to use the underlying data.

## 10. Data Files and downloads

The Data Files tab may provide:

- **Download Manifest**
- **Download Metadata (JSON)**

These functions describe or enumerate file records. Their availability does not mean controlled AlcHepNet research data may be downloaded or analyzed without approval. Follow the applicable proposal, ancillary-study, publication, and data-release process.

## 11. Use the Dictionary and Graph Model

Use the Dictionary to confirm:

- entity and property names
- data types
- enumerated values
- descriptions
- parent-child relationships

Use the Graph Model to understand how entities connect. A common path is:

`Study → Participant/Case → Follow Up → Biospecimen/Aliquot → Molecular Test or Protein Expression`

The expected schema does not prove that a field is populated in the current release. Confirm physical availability in Explorer, the row-level table, or an approved physical-data profile.

## 12. Query and Workspace

Use Query when a question cannot be answered efficiently with Explorer filters and a structured portal query is supported. Validate entity names and relationships in the Dictionary first.

Use Workspace only for authorized analyses and supported environments. Do not move controlled data to an unapproved environment. Record the study, data release, portal version, dictionary version, query or filters, and analysis code needed for reproducibility.

## 13. Reproducibility checklist

For any result used in a proposal, presentation, support request, or analysis record, capture:

- portal URL and environment
- access date
- portal version
- dictionary version
- study or project
- active Explorer tab
- complete filter selections
- AND/OR settings
- displayed denominator and linked-record counts
- report run identifier, if available
- known missingness or coverage limitations
- approval or data-release reference, when applicable

## 14. Troubleshooting

### Cannot log in or see data

- confirm the intended identity provider and account
- try the official URL directly
- capture the exact error and a screenshot
- record the time and portal environment
- contact the ARDaC technical team

### Counts are unexpected

- confirm the active study and tab
- inspect AND/OR logic
- remove filters one at a time
- review the row-level table
- check whether linked-record counts differ from participant counts

### A field is absent or empty

- enable **Show Empty Columns**
- check the Dictionary
- verify the study and release scope
- distinguish “not collected,” “not released,” “not applicable,” and “missing” when the sources permit
- do not infer a value from a related field without an approved rule

### Report output does not match the intended cohort

- return to Explorer
- recheck the active tab and filters
- confirm the displayed denominator
- generate a new report and retain the correct run information

## 15. Training resources

| Resource | Date or version | Link or file | Notes |
|---|---|---|---|
| ARDaC training slides | 2026-06-24 | `Training_06242026_final(8).pdf` | Source slide deck for the portal release described in this guide |
| AlcHepNet Training Videos channel | Verified 2026-09-17 | https://www.youtube.com/channel/UCaSmdEnTZcyHXkfPvNx_DnQ/videos | Official channel identified as **AlcHepNet Training Videos** |
| ARDaC 1st Online Training | Published 2025-09-19 | https://www.youtube.com/watch?v=e5VIhFTh05Y | Introductory ARDaC training |
| AlcHepNet ARDaC 2nd Training 20260624 | Session date 2026-06-24 | https://www.youtube.com/watch?v=v17qMbNVs3Y | Training session corresponding to the June 24, 2026 portal materials |

Resource titles, dates, and links were checked on September 17, 2026. Portal behavior may change after a new release; use the displayed portal and dictionary versions as the controlling operational context.

## 16. Source boundaries

- Study protocols govern eligibility, endpoints, timing, and clinical meaning.
- The data dictionary governs expected field names, types, and relationships.
- A physical-data profile or the portal record table governs what is present in a named release.
- The biorepository MOP governs documented specimen procedures within its scope.
- This guide governs portal navigation and operational workflow only.

When sources disagree or a required definition cannot be verified, document the gap and request clarification rather than silently choosing a plausible interpretation.
