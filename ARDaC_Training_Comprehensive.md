---
id: ardac_training_2026_06_24
type: study_knowledge
title: "ARDaC Training — Comprehensive Portal Guide"
organization: "AlcHepNet / Indiana University Data Coordinating Center"
training_date: "2026-06-24"
source_materials:
  - "Training_06242026_final(8).pdf"
  - "Pasted text(7).txt"
  - "Pasted text (2)(5).txt"
---

# ARDaC Training — Comprehensive Portal Guide

## Big Picture

**ARDaC** stands for **Alcohol Research Data Commons** and serves as the research data commons for the Alcohol-associated Hepatitis Network (AlcHepNet/AHN).

ARDaC is intended to function as:

- A **data center** for AlcHepNet data.
- A **collaboration hub** that helps investigators across the consortium work together.
- An **innovation engine** for generating hypotheses, inspiring studies, and supporting new research proposals.
- A platform that can gradually expand beyond the consortium to approved external research users.

The portal is designed primarily for **data exploration, feasibility assessment, hypothesis development, proposal planning, and review of available biospecimens, clinical data, laboratory results, and file-based translational data**.

> **Important:** Exploring information in ARDaC does **not** by itself authorize formal research use of AHN data. Research use and release of AHN data require the appropriate proposal/data-request approval process.

---

# 1. Training Overview

## Training Session

- **Title:** ARDaC Training — Welcome Onboard
- **Date:** June 24, 2026
- **Organization:** AlcHepNet – ITAALD Indiana University Data Coordinating Center
- **Institution:** Indiana University School of Medicine

## Instructors

| Instructor | Role |
|---|---|
| Hao Wang | Analytic Visualization |
| Mengting Xiong | ARDaC Project Manager |
| Carla Kettler | Director, Data Core |
| Jing Su, PhD | Director, Data Commons |
| Wanzhu Tu, PhD | IUDCC PI |

## Training Agenda

1. Welcome
2. Instructor introductions
3. ARDaC overview
4. ARDaC portal walkthrough
5. General portal functions
6. Data model and advanced functions
7. Q&A
8. User survey and feedback

---

# 2. What ARDaC Contains

## Study Sources

The training materials describe ARDaC as incorporating or planning to incorporate several study sources:

- **AHN observational study**
- **AHN randomized clinical trial**
- **TREAT 001 / TRT-001**, an observational study
- **ITAALD RCT** — future release after trial completion
- **External studies** — planned future expansion

The June 2026 update specifically added **TREAT 001 / TRT-001** so it can be explored alongside existing AlcHepNet resources.

## Major Data Domains

ARDaC currently focuses on several connected data domains:

### Clinical Data

Examples include:

- Baseline information
- Study design information
- Participant characteristics
- Follow-up data
- Clinical outcomes
- Adverse events
- Behavioral variables
- Survival and acute kidney injury outcomes

### Biospecimens

Examples include:

- Specimen type
- Specimen availability
- Lab assignment
- Shipment status
- Links to participants
- Links to follow-up and outcome context

A major use of the biospecimen section is determining whether samples are **still available for future translational work**.

### Laboratory Assays

Examples include:

- Study laboratory results
- Translational laboratory results
- Biomarkers
- Longitudinal biomarker measurements

### Omics / Translational Data

The updated portal includes **proteomics-related resources**. Proteomics data are represented through the data model using nodes such as **Protein Expression**, with links to biospecimens and clinical/follow-up context.

---

# 3. ARDaC Data Architecture and Standards

ARDaC uses a graph-based data commons model intended to harmonize data from different studies and provide a common interface for:

- Querying
- Visualization
- Data exploration
- Analysis
- Linking clinical and translational data

The training emphasizes a **FAIR design foundation** and use of standard data structures.

Referenced foundations include:

- **CDEs** — common/standard data elements
- **Graph Common Data Model**
- **NIH GDC**-style graph/genomics data model concepts
- **GA4GH** global data standards

The purpose of this standardized structure is to make data from different studies more interoperable and to allow reproducible querying and analysis.

---

# 4. Intended Use of ARDaC

The intended research workflow is:

## Step 1 — Explore Data

Use ARDaC to browse:

- Participants
- Follow-ups
- Biospecimens
- Lab results
- Data files

## Step 2 — Develop Hypotheses

Use the portal to:

- Assess feasibility
- Identify available data
- Identify available specimens
- Explore preliminary patterns
- Develop research questions
- Prepare proposal ideas
- Plan data-access requests

## Step 3 — Request Data

If the data appear appropriate for a proposed study:

- Submit the research proposal through the relevant AHN review process.
- Obtain approval through the **AHN Publication and Ancillary Study Subcommittee** or other designated approval pathway.

## Step 4 — Conduct Research

After approval and formal data release:

- Analyze the approved dataset.
- Generate findings.
- Prepare publications or other research outputs.
- Disseminate results.

---

# 5. ARDaC Access Roadmap

The training presents ARDaC access in three phases.

## Phase 1 — Completed

**Invited users**

- System testing
- Feedback
- Initial portal validation

Approximate period in the slides: **September 2025–May 2026**.

## Phase 2 — Current

**All AlcHepNet investigators**

- Consortium-wide access
- Current data release
- Expanded training and help-desk support

The slides identify **June 2026–present** as the current phase.

## Phase 3 — Future

**Approved external users**

- Future expansion beyond the consortium
- Broader research-community access

---

# 6. Current State of ARDaC

The June 2026 training describes four major areas of progress.

## Data Expanded

- AHN data
- TREAT 001
- More biospecimen information
- More lab results
- More outcomes and adverse events
- Translational proteomics data

## Portal Updated

- New data
- New portal features
- Cloud-based access
- Training resources
- Help-desk support

## Analytics Added

- Interactive exploration
- Survival analysis
- **Anagine Summary Reports**
- R/Python microservices
- Infrastructure intended to support AI, machine learning, and statistical methods

## Still Growing

Future development includes:

- Additional studies
- More data
- Additional analytical functions
- Broader user access
- Greater research-community impact

---

# 7. June 2026 Portal Update — Major Changes

## 7.1 New Portal Release

The updated portal was described as moving through alpha testing and preparation for official release.

Version information shown in the training:

- **Dictionary:** v2.4.0
- **Portal:** v3.3.4-2026.05

Version tracking is useful for:

- Reporting technical issues accurately
- Documenting exactly which portal release was used
- Identifying the data dictionary used by that portal version
- Supporting reproducibility in proposals, publications, screenshots, and analyses

### Portal Version vs. Dictionary Version

These are different:

- **Portal version** = version of the user-facing interface, layout, and application.
- **Dictionary version** = version of the underlying data definitions and structure.

The portal relies on the dictionary to organize and define the data.

For reproducibility, users should record relevant versions when using portal outputs in research documentation.

---

## 7.2 TREAT 001 / TRT-001 Added

Users can now include or exclude TREAT 001 when exploring data.

The study can be selected through study filters and examined alongside existing observational and clinical-trial data.

Study selection can affect:

- Participant counts
- Follow-up records
- Biospecimen counts
- Lab-result availability
- Summary charts
- Generated reports

---

## 7.3 Anagine Summary Reports

One of the largest updates is the **Summary Report powered by Anagine**.

The report is generated from the user's **current filtered Explorer cohort**.

### Basic Workflow

1. Select a data tab.
2. Apply filters.
3. Click **Summary Report**.
4. Report generation starts.
5. A status panel appears.
6. Multiple reports can be generated at the same time.
7. A report can be canceled while processing.
8. When finished, the report opens automatically.

### Supported Data Types

The training describes reports for four major data types:

- Participants
- Follow Ups
- Biospecimens
- Lab Results

### Report Contents

A generated report can include:

- Cover page
- Run information
- Selected filters
- Data statistics
- Data completeness
- Visual summaries
- Specific analyses
- Example data rows

### Why the Report Matters

The report serves as a **reproducible snapshot of what the investigator selected in Explorer**.

It can help with:

- Feasibility checking
- Proposal preparation
- Data-request planning
- Reviewing cohort composition
- Reviewing data completeness
- Reviewing specimen and laboratory coverage
- Communicating a proposed analysis cohort

### Example Participant-Level Report

The training slide gives an example report with:

- 1,280 selected participants
- 2,974 linked follow-ups
- 10 visit days represented
- Median MELD score: 20.0
- Median Child-Pugh: 9.0
- Median Maddrey DF: 26.1

Example visuals included:

- Alcohol-use distribution by visit day
- Median MELD trends over follow-up
- Median Child-Pugh trends over follow-up

> These values were explicitly presented as **example report outputs** to demonstrate scope and format, not as findings to interpret clinically.

### Example Biospecimen Report

For a serum-filter example:

- 2,484 selected biospecimens
- 486 linked participants
- 1,004 linked follow-ups

The report also summarized the distribution across labs.

### Example Lab-Result Report

For a serum-albumin example:

- 764 selected lab results
- 449 linked participants
- 100% serum albumin coverage

Example related coverage included:

- Albumin: 100%
- Bilirubin: 99%
- Creatinine: 98%
- ALT: 99%
- AST: 99%
- INR: 97%
- eGFR: 23%

These reports can help determine whether the selected samples and associated clinical/laboratory context are sufficient for a proposal or data request.

---

## 7.4 Anagine Architecture and Future Analytics

Anagine is described as supporting:

- Ad hoc query-based online analysis
- Visualization
- Report generation
- Statistical analysis
- Potential AI/ML workflows

The architecture shown in the training connects multiple components, including:

- Data layer
- Elasticsearch
- GraphQL
- Backend/middleware services
- Portal frontend
- Workspace
- AI/ML components

The training also states that R and Python microservices are being used or developed to support statistical, machine-learning, and AI models.

Users were encouraged to recommend:

- New analyses
- Statistical models
- Machine-learning functions
- AI functions
- New visualizations
- Additional report elements

---

## 7.5 Data File Download Functions

The update enables download options under the **Data Files** tab, including:

- **Download Manifest**
- **Download Metadata (JSON)**

### Important Distinction

This download capability does **not** mean that unrestricted AHN research data can be downloaded for research use.

The training repeatedly clarifies:

- Manifest or metadata functions may be available in the Data Files interface.
- Formal AHN research data use still requires the appropriate proposal and approval process.
- Investigators should obtain approval before using or downloading controlled research data for formal analysis.

---

## 7.6 Proteomics Data Resources

Proteomics data are represented through nodes such as **Protein Expression**.

These nodes connect molecular measurements with:

- Biospecimens
- Participants
- Follow-ups
- Other clinical context
- Molecular tests

Investigators can use these resources to:

- Check proteomics data availability
- Review what translational data have already been generated
- Compare existing data with available biospecimens
- Develop translational hypotheses
- Plan proposals that complement existing data

The live demonstration noted that proteomics data contributed by a translational lab were already visible in the portal.

---

# 8. Portal URLs

The training materials provide:

- **Training portal:** https://training.ardac.org/
- **Official portal:** https://portal.ardac.org/
- **Archived/old portal:** https://archive.portal.ardac.org
- **ARDaC website:** https://ardac.org/
- **AlcHepNet website:** https://www.alchepnet.org/

---

# 9. Login and Authentication

## Login Workflow

1. Open the ARDaC homepage.
2. Click **Login** in the upper-right corner.
3. Choose an identity provider.
4. Authenticate.
5. Authorize the requested identity information.
6. After successful login, return to the ARDaC dashboard.

## Identity Options

The training describes:

- **CILogon**
- **ORCID**
- Institutional credentials through a selected identity provider

The system uses identity information such as name and affiliation to map:

- User role
- Project access
- Permissions

### Access Problems

During Q&A, one participant reported difficulty logging in and seeing data.

The recommended approach was:

- Capture a screenshot if possible.
- Contact the ARDaC technical team.
- Allow the team to review account and identity-provider mapping offline.

---

# 10. Dashboard Overview

After login, the user lands on the main dashboard.

## Top Navigation

The portal includes major navigation areas such as:

- **Dictionary**
- **Exploration**
- **Files**
- **Query**
- **Workspace**
- **Profile**
- **Anagine** / analytics area

The live training noted that some Anagine functionality may appear disabled or restricted in the main navigation when functionality is still internal/developer-facing, even though Anagine-backed reporting is available through the Explorer workflow.

## Top-Right Area

May include:

- Browse/Submit Data
- Documentation
- User/login status
- Logout

## Central Dashboard

The dashboard provides:

- A short description of ARDaC
- High-level counts
- Study counts
- Participant counts
- Follow-up counts
- File counts
- Data-distribution graphics

The cards and charts help users quickly understand the scale and composition of available data.

## Quick Actions

The bottom area provides shortcuts for common tasks such as:

- Learn about the data dictionary
- Explore data
- Query data
- Browse or submit data

The AlcHepNet icon can be used to return to the main homepage.

---

# 11. Core Exploration Workflow

The **Exploration** page is the main area for routine portal use.

## Five Main Data Tabs

1. Participants
2. Follow Ups
3. Biospecimens
4. Lab Results
5. Data Files

## Main Page Areas

### Explorer Filters

Usually displayed on the left.

Filters define the cohort or records being explored.

Depending on the active tab, filters may include:

- Study
- Participant
- Behavior
- Outcome
- Lab test
- Follow-up
- Biospecimen
- Lab
- Data-file fields

### Summary Statistics / Chart Panel

Usually displayed on the right.

As filters change:

- Counts update
- Charts update
- Proportions update
- Available categories change

Users can hover over visualizations to see additional details.

### Table of Records

At the bottom of the page.

The table shows the row-level records matching the current filters and can be used as a **sanity check** to verify that the filtered data look as expected.

A **Show Empty Columns** option can reveal fields that are blank for the selected records.

## Basic Explorer Workflow

**Choose data tab → set filters → review counts and charts → inspect table → generate report if needed**

---

# 12. Advanced Filtering

## Search Within Filters

A search icon can be used to quickly find filter options.

## AND/OR Logic

A settings/gear control can be used to change how selected values are combined.

Possible logic includes:

- **AND**
- **OR**

This allows more precise cohort definitions.

## Real-Time Updating

When filters are changed:

- Counts update immediately.
- Charts update immediately.
- Tables reflect the selected cohort.
- Anagine reports use the resulting filtered cohort.

---

# 13. Participants Tab

The **Participants** tab is used for participant-level exploration.

## Study Filters

Examples include:

- Project
- Study name
- Observational group
- Treatment arm in RCT

## Participant Filters

Examples include:

- Sex
- Race
- Ethnicity
- Clinical site
- Other demographics

## Behavior Filters

Examples shown include alcohol-use variables such as:

- Drinking frequency
- Drinks per day
- Frequency of heavy drinking

## Outcome Filters

Examples include:

- AKI status
- Days to AKI
- 90-day survival
- 180-day survival
- 90-day AKI
- 180-day AKI

Numeric variables may appear as sliders.

Categorical variables generally appear as checkboxes.

## Laboratory-Test Filters

Users can select whether particular laboratory measurements are available.

Examples shown include:

- ALT
- AST
- Alkaline phosphatase
- Total bilirubin
- Creatinine
- Albumin
- Estimated GFR
- INR
- Prothrombin time
- Total protein
- Direct bilirubin
- AHR activity
- ORM1
- IL-1RA
- BUN
- ACE
- Cystatin-C
- Renin
- Urine creatinine
- Urine IL-18
- Urine KIM-1
- Urine L-FABP
- Urine NGAL

---

# 14. Survival Curve Analysis

The Participants tab includes a customized **Kaplan-Meier survival analysis** component.

## Outcomes

The user can select:

- **Death / Overall Survival**
- **AKI / Time to AKI**

## Grouping Options

Possible grouping choices include:

- No grouping
- Observational group
- Treatment arm
- Sex

## Output

The component includes:

- Main Kaplan-Meier curve
- Censoring marks
- Number-at-risk information
- Event counts
- Hover details such as survival probability at a selected time point

## Index Date / Time Origin

This differs by study type:

### RCT Participants

For survival and AKI analyses, the portal uses the **treatment start date** as the start/index date.

The training identifies the variable:

`rct_trtstdat`

### Observational Participants

For observational participants, the portal uses the **enrollment date** as the start/index date.

## RCT Filtering

If the Explorer is filtered to the clinical trial only:

- Observational groups are removed from relevant grouping choices.
- Curves can then focus on trial treatment arms.

The demonstration included treatment-arm comparisons such as:

- Prednisone
- Anakinra + Zinc

---

# 15. Follow Ups Tab

The **Follow Ups** tab is designed for longitudinal records.

## Filters

Users can filter by:

- Study
- Participant characteristics
- Follow-up attributes
- Outcome
- Lab test

## Longitudinal Clinical Scores

The portal includes customized analyses for important liver-disease scores:

- **MELD Score**
- **Child-Pugh Score**
- **Maddrey's Discriminant Function**
- **Lille Score**

These can be displayed across visit days.

## Visualization Types

The training shows or discusses:

- Box plots
- Spaghetti plots
- Longitudinal trajectories

Users can hover over plots to see more information such as:

- Quantiles
- Ranges
- Values at specific visit days

## Downloading Visualizations

The chart menu can be used to download:

- Plot images
- Underlying data
- Different supported formats

The demonstration notes that clicking the three-line chart menu provides download options.

---

# 16. Biospecimens Tab

The **Biospecimens** tab is used to examine sample availability and sample context.

## Filters

Possible filters include:

- Study
- Participant characteristics
- Clinical site
- Biospecimen type
- Lab
- Follow-up
- Outcome

## Key Use Case — Available Samples

A particularly important filter is:

**Biospecimens → Labs → Not assigned**

Selecting **Not assigned** identifies biospecimens that have not yet been assigned or shipped to a lab.

This supports:

- Feasibility checking
- Translational research planning
- Identifying available specimen types
- Determining whether enough material is available for a proposed study

During the live demonstration, the presenters noted that **more than 50,000 biospecimens** were still in the not-assigned/not-shipped category at that time.

The portal can also help investigators compare:

- What specimens remain available
- What specimens were already shipped
- What data have already been generated
- Whether a new proposal could create useful synergy with existing data

---

# 17. Lab Results Tab

The **Lab Results** tab is used to explore laboratory and translational results.

## Filters

Users can filter by:

- Study
- Laboratory
- Participant characteristics
- Clinical site
- Laboratory test
- Outcome

## Lab-Specific Exploration

After selecting a laboratory, corresponding laboratory tests and biomarker visualizations become available.

Examples from the training include laboratory-specific exploration for:

- Nagy lab
- Liangpunsakul lab

## Example Biomarkers

Customized examples include:

- Urine L-FABP
- Urine Creatinine
- Urine IL-18
- Urine KIM-1
- Urine NGAL
- ORM1

## Visualization

Biomarkers can be viewed across groups or visits using:

- Box plots
- Overlaid spaghetti plots

The purpose is to quickly understand:

- Which biomarkers are available
- How much data exist
- How measurements vary over time
- How results differ across study or treatment groups

---

# 18. Data Files Tab

The **Data Files** tab is intended primarily for large or file-based datasets such as:

- Omics data
- Proteomics
- Imaging
- Other file collections

Depending on permissions and data type, users may be able to:

- Browse file records
- Review metadata
- Download a manifest
- Download metadata in JSON format

This tab is part of the Explorer workflow, so file records can be viewed together with filters, summaries, and record tables.

---

# 19. Files Section vs. Data Files Tab

The training distinguishes two related interfaces.

## Data Files Tab in Exploration

Used within the normal Explorer workflow.

Supports:

- Filtering
- Summaries
- Tables
- File-level records

## Files in Top Navigation

Provides a more direct route to file-level information.

May support:

- Browsing available files
- Reviewing metadata
- File-oriented access for large omics/imaging datasets

---

# 20. Data Dictionary

The **Dictionary** page shows the ARDaC data model.

## What It Contains

- Nodes
- Attributes/properties
- Definitions
- Relationships
- Categories

## Table View

Users can:

- Search terms
- Browse nodes
- Read descriptions
- Review properties
- Download dictionary information in formats such as JSON or TSV

## Graph View

The data model can be displayed as connected nodes.

Users can:

- Zoom in/out
- Follow relationships
- Click a node
- View node properties
- View connected/parent nodes

## Main Uses

The dictionary is especially useful for:

- Understanding variable definitions
- Understanding how data entities connect
- Preparing GraphQL queries
- Validating a data structure before submission
- Ensuring submitted data conform to the required model

---

# 21. Query Page

The **Query** page is an advanced feature intended for:

- Developers
- Informaticians
- Data scientists

It allows direct **GraphQL** queries against the database.

## Workflow

1. Enter a GraphQL query in the query panel.
2. Run the query.
3. Review the returned results.
4. Optionally switch to a graph-model/schema view.

The graph structure in the Data Dictionary helps users understand how to construct valid GraphQL queries.

Most routine users do **not** need the Query page because standard exploration can be done through the Explorer interface.

---

# 22. Restricted / Advanced Functions

The training identifies some functions as advanced or permission-dependent.

Examples include:

- Direct GraphQL querying
- Workspace/Jupyter environments
- Programmatic access
- Data submission
- Some direct data-access functions

These functions may require:

- Additional authorization
- A data request
- Project-specific permission
- DCC approval

---

# 23. Browse Data / Submit Data

The Browse/Submit Data area provides a project-oriented view.

## Project List

The page may show project-level counts such as:

- Cases
- Experiments
- Aliquots
- Files

## Browse Data

A **Browse Data** button can open a project's data structure.

The graph may contain nodes such as:

- Project
- Study
- Case
- Demographic
- Follow-up
- Aliquot
- Lab
- Protein expression

Node colors distinguish different categories such as:

- Administrative
- Biospecimen
- Clinical
- Data file

Users can toggle between different graph views.

## Submission Page

For authorized users, the submission interface can:

- Display the current data structure
- Accept new TSV data files
- Validate data against the dictionary structure

The training states that, at the time of the session, data submission was primarily restricted to **DCC data managers** who review and upload cleaned data.

---

# 24. Workspace

The **Workspace** area provides access to external or cloud analysis environments.

The training describes a Jupyter-based workflow in which an authorized user can:

- Launch a Jupyter Notebook environment
- Upload notebooks
- Pull or access approved datasets
- Run Python
- Run R

The functionality exists but is **not open by default** to every user.

Access requires a request and appropriate authorization.

---

# 25. Profile Page

The **Profile** page contains account and access information.

## API Keys

Users may be able to:

- Create API keys
- View API keys
- Revoke/delete API keys

API keys enable programmatic access through:

- Scripts
- Applications
- Notebooks

> API keys should be treated like passwords.

## Project Access

The profile can also show:

- Projects the user can access
- Permissions
- Available methods
- Query/submission access

This helps the user understand exactly what they are authorized to do.

---

# 26. Approval and Data-Request Process

ARDaC is an **exploration and planning platform**, not a replacement for the formal AHN research approval process.

## Core Rule

Investigators can explore available information and use it to formulate a proposal.

Before formal research use of AHN data:

1. Prepare the research proposal.
2. Submit through the official AHN process.
3. Obtain approval from the appropriate publication/ancillary study review group.
4. Request release of the approved dataset.
5. Conduct the analysis only after data access is authorized.

## Clarification About Downloads

The updated portal may contain a **download** function under Data Files for manifests or metadata.

That does not automatically authorize research use of the underlying AHN data.

Formal research data release remains approval-controlled.

---

# 27. Quick Reference / Cheat Sheet

| Task | Portal Path |
|---|---|
| Generate Summary Report | Exploration → choose data tab → apply filters → Summary Report |
| Survival analysis | Exploration → Participants → Chart panel → Survival Analysis |
| MELD analysis | Exploration → Follow Ups → Chart panel |
| Child-Pugh analysis | Exploration → Follow Ups → Chart panel |
| Maddrey DF analysis | Exploration → Follow Ups → Chart panel |
| Lille Score analysis | Exploration → Follow Ups → Chart panel |
| Other biomarkers | Exploration → Lab Results → select lab/test → Chart panel |
| Find available biospecimens | Exploration → Biospecimens → Biospecimen filters → Labs → Not assigned |
| Inspect row-level records | Exploration → Table of Records |
| Search dictionary | Dictionary → search box |
| Explore graph model | Dictionary → Graph View |
| Run GraphQL | Query → enter query → Run |
| Review account access | Profile → Project Access |
| Manage API keys | Profile → API Keys |
| Browse project structure | Browse Data → select project |
| Launch notebook environment | Workspace → Launch, if authorized |

---

# 28. Practical Research Workflows

## Workflow A — Check Whether a Cohort Exists

1. Open **Exploration**.
2. Select **Participants**.
3. Choose study.
4. Apply demographic and clinical filters.
5. Add outcome or lab-test constraints if needed.
6. Review participant counts.
7. Review charts.
8. Check the Table of Records.
9. Generate an Anagine report for documentation.

## Workflow B — Evaluate a Biospecimen Proposal

1. Open **Biospecimens**.
2. Filter to the relevant study/cohort.
3. Select specimen type.
4. Select **Labs → Not assigned**.
5. Review available specimen counts.
6. Review participant and clinical context.
7. Compare with existing translational data.
8. Generate a Summary Report.
9. Use results to prepare a formal proposal.

## Workflow C — Explore a Biomarker

1. Open **Lab Results**.
2. Select a lab.
3. Select a laboratory test or biomarker.
4. Filter to a study/cohort if needed.
5. Review available measurements.
6. Examine box/spaghetti plots.
7. Review outcome context.
8. Generate a Summary Report if useful.

## Workflow D — Compare RCT Treatment Arms

1. Open **Participants**.
2. Filter to **clinical_trial**.
3. Select treatment arms.
4. Choose overall survival or AKI.
5. Group survival curves by treatment arm.
6. Review number-at-risk and event tables.
7. Use hover details for time-point information.
8. Remember that RCT survival/AKI time starts at treatment start date.

## Workflow E — Review Longitudinal Clinical Severity

1. Open **Follow Ups**.
2. Filter to the desired study/cohort.
3. Select a score:
   - MELD
   - Child-Pugh
   - Maddrey DF
   - Lille
4. Review the score across visit days.
5. Use boxplot or spaghetti-plot views.
6. Download figures/data if appropriate.

---

# 29. Important Interpretation Notes

## Portal Counts Are Filter-Dependent

Any count, chart, or report reflects the active filters.

Changing a filter changes the selected records and therefore changes the output.

## Summary Reports Are Snapshots

An Anagine report reflects the specific selected cohort at the time it was generated.

It should be treated as a reproducible snapshot rather than a permanent description of the entire data commons.

## Example Training Numbers Are Not Study Conclusions

Several slides show example counts and summary statistics.

These were used to demonstrate portal features and report format.

They should not automatically be interpreted as formal research findings.

## Study Type Affects Time Origin

For Kaplan-Meier analyses:

- RCT → treatment start date
- Observational study → enrollment date

This difference is important when interpreting curves.

## Permissions Matter

A feature appearing in the portal does not necessarily mean every user is authorized to use it.

Workspace, submission, API, programmatic access, and formal data downloading can depend on role and approval.

---

# 30. Support and Contacts

## Research Proposal / Data Request Questions

Training materials list:

**Savannah Yarnelle**  
`samussel@iu.edu`

## Technical ARDaC Questions

**ARDaC support**  
`ardac@iu.edu`

The training also lists the ARDaC mailing list:

`ardac4in@iu.edu`

---

# 31. Additional Resources

## Source Code

ARDaC source-code resources are hosted through the Su Informatics Lab GitHub organization/repositories.

The training specifically references repositories for:

- ARDaC Dictionary
- ARDaC Portal
- General ARDaC source code

## Training Videos

The training session and portal demonstrations were planned to be distributed through the AlcHepNet training-video YouTube channel.

## Documentation

Training materials indicate that documentation, training resources, and guides would be shared through:

- ARDaC website
- GitHub
- YouTube
- Portal documentation area

At the time of one demo, some documentation pages were still under development.

---

# 32. Acknowledgements

The training materials acknowledge:

- **NIAAA** support
- Grant/support reference: **U24AA026969**
- Indiana University Data Coordinating Center
- AHN investigators
- Translational investigators
- Indiana University Genetic Biobank as the central AHN biorepository
- The ARDaC training-material development team

---

# 33. Key Takeaways

1. **ARDaC is primarily an exploration and research-planning platform.**
2. It integrates participant, follow-up, biospecimen, laboratory, and file-based translational data.
3. The June 2026 release added **TREAT 001**, expanded data resources, and introduced major new reporting capabilities.
4. **Anagine Summary Reports** turn the current filtered Explorer selection into a structured, reproducible report.
5. The **Participants** tab supports survival and AKI analysis.
6. The **Follow Ups** tab supports longitudinal MELD, Child-Pugh, Maddrey DF, and Lille analyses.
7. The **Biospecimens** tab can identify samples that remain unassigned/unshipped.
8. The **Lab Results** tab supports laboratory- and biomarker-specific exploration.
9. The **Data Dictionary** explains the graph data model and supports advanced querying and submission.
10. GraphQL, Workspace, API, data submission, and other advanced functions can require additional permission.
11. Manifest/metadata downloads are different from authorization to use AHN research data.
12. Formal research use still requires the appropriate AHN proposal and data-request approval process.

---

# 34. Terminology

| Term | Meaning in ARDaC |
|---|---|
| ARDaC | Alcohol Research Data Commons |
| AHN | Alcohol-associated Hepatitis Network / AlcHepNet |
| OBS | Observational study/group |
| RCT | Randomized clinical trial |
| AKI | Acute kidney injury |
| MELD | Model for End-Stage Liver Disease score |
| Child-Pugh | Liver-disease severity score |
| Maddrey DF | Maddrey's Discriminant Function |
| Lille Score | Score used in alcohol-associated hepatitis follow-up/treatment assessment |
| Biospecimen | Biological sample stored for laboratory/translational analysis |
| Anagine | ARDaC analytics/reporting engine used to generate filtered summary reports |
| GraphQL | Query language used in the advanced Query page |
| Data Dictionary | Structured definitions of ARDaC nodes, properties, and relationships |
| Node | An entity in the ARDaC graph data model |
| API Key | Credential used for programmatic access |
| Manifest | File/index describing selected data-file resources or metadata |
| Workspace | Permission-controlled analysis environment such as Jupyter |
| CILogon | Federated authentication method used for ARDaC login |
| ORCID | Researcher identity option used for login/authentication |

---

# 35. Source Note

This file consolidates the June 24, 2026 ARDaC training slide deck with both provided training/demo transcripts. Obvious speech-to-text errors in the transcripts were normalized using terminology shown in the slide deck (for example, **ARDaC**, **Anagine**, **biospecimen**, **MELD**, **Child-Pugh**, and **Lille**). Where the live transcript added operational details not explicit in the slide text, those details were incorporated when consistent with the training materials.
