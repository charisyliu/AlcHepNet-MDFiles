# Proposed AlcHepNet / ARDaC Knowledge Base Architecture (Draft)

## Vision

Create a scalable, AI-friendly knowledge platform that connects study protocols, operational documentation, training materials, database schema, raw data, and future study resources into a single navigable system.

---

# 1. Umbrella Knowledge Base (Master Navigation Layer)

**Purpose**

The entry point for the entire knowledge base.

This document does **not** duplicate other resources. Instead, it defines:

- Overall architecture
- Resource hierarchy
- Source-of-truth rules
- AI retrieval rules
- Cross-resource relationships
- Knowledge routing
- Terminology mapping
- Database navigation
- Relationship framework
- Maintenance and version history

**Deliverables**

- Umbrella Knowledge Base
- Source hierarchy
- Relationship overview
- AI routing guide

---

# 2. Scientific Knowledge Layer

## 2.1 Study Protocols

For each protocol:

- Executive Summary
- Background
- Objectives
- Study Design
- Timeline
- Eligibility
- Enrollment
- Participant Groups
- Randomization (if applicable)
- Visit Schedule
- Clinical Assessments
- Laboratory Assessments
- Questionnaires
- Biospecimen Collection
- Outcomes
- Statistical Analysis
- Safety Monitoring
- Data Management
- References
- Appendices

Current examples

- AlcHepNet-01 Observational Study
- AlcHepNet-02 Randomized Clinical Trial

Future

- Additional protocols

## 2.2 Publications

- Publications
- Conference abstracts
- Presentations

## 2.3 Scientific Concepts

- Disease definitions
- Biomarkers
- Clinical endpoints
- Outcome definitions
- Study terminology

---

# 3. Operational Knowledge Layer

## 3.1 Biorepository

- Purpose
- Specimen lifecycle
- Collection
- Processing
- Aliquoting
- Labeling
- Storage
- Shipping
- Receipt
- Inventory
- Distribution
- Quality Control
- Biosafety

## 3.2 Laboratory Operations

- Laboratory SOPs
- Instrument procedures
- Laboratory workflows

## 3.3 Site Operations

- Recruitment
- Monitoring
- Data entry
- Regulatory workflow

## 3.4 Training

- ARDaC Training
- Portal walkthroughs
- User guides
- FAQs

---

# 4. Data Knowledge Layer

## 4.1 Database Overview

- Database architecture
- Entity catalog
- Categories
- Navigation hubs

## 4.2 Entity Documentation

One document per entity including:

- Purpose
- Record level
- Required fields
- Primary key
- Foreign keys
- Relationships
- Important variables
- AI retrieval notes

Examples

- Case
- Follow-up
- Diagnosis
- Treatment
- Sample
- Aliquot
- Molecular Test
- Laboratory
- Demographic
- Exposure

## 4.3 Variable Dictionary

For every variable:

- Definition
- Description
- Data type
- Required status
- Allowed values
- Appears in
- Related entities

## 4.4 Relationship Documentation

- Entity relationships
- Foreign keys
- Cardinality
- Parent-child relationships
- ER diagrams
- Mermaid diagrams

## 4.5 Controlled Vocabulary

- Terminology
- Synonyms
- Standard definitions

## 4.6 Schema Documentation

Generated directly from schema.

---

# 5. Data Assets Layer

Actual study data.

- Clinical data
- Follow-up data
- Laboratory data
- Biospecimens
- Molecular data
- Omics
- Imaging
- Metadata
- Released datasets

---

# 6. Crosswalk Layer

Connects all knowledge resources.

## Protocol → Database

Protocol

↓

Database table

↓

Variables

↓

Raw data

## Protocol → Biospecimens

Protocol

↓

Collection schedule

↓

Biorepository MOP

↓

Sample table

↓

Aliquot table

↓

Laboratory

## Visit Crosswalk

Protocol Visit

↓

Follow-up

↓

Clinical Data

↓

Questionnaires

↓

Specimens

↓

Laboratory

## Variable Crosswalk

Scientific Concept

↓

Variable

↓

Entity

↓

Raw Table

## Participant Flow

Participant

↓

Enrollment

↓

Visit

↓

Diagnosis

↓

Treatment

↓

Outcome

↓

Long-term Follow-up

---

# 7. AI Knowledge Layer

- AI routing
- Retrieval rules
- Context preservation
- Conflict resolution
- Synonyms
- Example prompts
- AI guardrails

Guardrails include:

- Preserve participant group
- Preserve study
- Preserve visit
- Preserve treatment arm
- Prevent hallucinations
- Prevent mixing protocols

---

# 8. Evaluation & Quality Assurance

- Protocol evaluations
- Biorepository evaluation
- Coverage reports
- Missing information
- Error tracking
- Validation
- Version history

---

# 9. Future Expansion

- Additional protocols
- Additional studies
- Publications
- Analysis pipelines
- Code repositories
- APIs
- External resources

---

# 10. Overall Knowledge Flow

```text
                    Umbrella Knowledge Base
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
 Scientific Knowledge    Operational Knowledge   Data Knowledge
        │                      │                      │
        └──────────────┬──────────────┬──────────────┘
                       ▼
               Crosswalk Layer
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Database       Raw Data      AI Retrieval
                       │
                       ▼
             Evaluation & Quality Assurance
                       │
                       ▼
               Future Expansion
```

---

# Deliverables

| Status | Deliverable |
|---------|-------------|
| ✅ Completed | Protocol 01 Knowledge Base |
| ✅ Completed | Protocol 02 Knowledge Base |
| ✅ Completed | Biorepository Knowledge Base |
| ✅ Completed | ARDaC Training Knowledge Base |
| ✅ Completed | Database Knowledge Base |
| ✅ Completed | Umbrella Knowledge Base |
| 🚧 Proposed | Crosswalk Layer |
| 🚧 Proposed | AI Knowledge Layer |
| 🚧 Proposed | Future Expansion Modules |
