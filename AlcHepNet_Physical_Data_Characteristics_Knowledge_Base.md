---
id: alchepnet_physical_data_characteristics
title: AlcHepNet Physical Data Characteristics Knowledge Base
type: data_profile
database: ARDaC-AlcHepNet
schema_version: "2.1.1"
profile_scope: "Supplied physical data files"
profile_date: "2026-08-18"
---

# AlcHepNet Physical Data Characteristics Knowledge Base

## Purpose

This file summarizes the **physical data actually present in released AlcHepNet/ARDaC data tables** so that an AI system can understand the current contents and quality characteristics of the database without repeatedly scanning the underlying row-level files.

This file is intentionally different from the Data Dictionary / schema knowledge base:

- The **schema knowledge base** explains what entities and variables are allowed to exist.
- This **physical-data profile** explains what values are actually present in the supplied data release.
- The profile should be regenerated or updated whenever physical tables, rows, or columns change.

The current supplied physical-data file is:

`aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001(1).tsv`

The current profile therefore describes the supplied **aliquot** data chunk only. It must not be interpreted as a complete profile of every table in the full ARDaC database.

---

# 1. Profiling Standard

The following metrics are used for each physical table.

## Table-level metrics

| Metric | Meaning |
|---|---|
| Row count | Number of physical records in the table |
| Column count | Number of physical fields in the table |
| Entity / grain | What one row represents |
| Schema alignment | Schema entity associated with the physical table |
| Key fields | Identifiers used to distinguish or link records |
| Duplicate risk | Whether identifiers or complete rows show repetition |
| Data coverage | Whether the supplied file appears complete or is only a chunk/subset |
| Relationship fields | Physical foreign-key/link fields used to connect to other entities |

## Column-level metrics

| Metric | Meaning |
|---|---|
| Data type | Numeric, categorical/text, identifier, date/time, relationship key, etc. |
| Non-empty count | Number of rows containing a value |
| Missing count | Number of rows without a value |
| Completeness | Non-empty rows divided by total rows |
| Distinct values | Number of unique non-null values |
| Uniqueness ratio | Distinct values divided by non-empty rows |
| Example values | Representative observed values |
| Allowed values | Schema-defined domain, when available |
| Validity / conformity | Whether observed values are compatible with schema expectations |
| Distribution | Frequencies for categorical variables where available |
| Numeric summary | Mean, median, standard deviation, minimum, maximum, and quartiles when applicable |
| Quality note | Important missingness, duplication, sparsity, or interpretation issue |

## Data-quality dimensions

The profile uses the following dimensions when relevant:

- **Completeness** — whether expected values are populated.
- **Uniqueness** — whether values expected to identify records are distinct.
- **Validity** — whether values conform to schema-defined type/domain rules.
- **Consistency** — whether values and relationships are internally coherent.
- **Integrity** — whether relationship keys can support linkage across entities.
- **Volume** — whether row counts change unexpectedly.
- **Distribution** — whether values shift substantially across releases.
- **Freshness** — whether the profile reflects the latest supplied release.

---

# 2. Physical Table Registry

| Physical File | Schema Entity | Rows | Columns | Current Profile Status |
|---|---|---:|---:|---|
| `aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001(1).tsv` | `aliquot` | 20,000 | 9 | Profiled |

> Add one row to this registry whenever another physical table is supplied and profiled.

---

# 3. Aliquot Physical Table

## 3.1 Table Overview

**Physical file:** `aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001(1).tsv`  
**Schema entity:** `aliquot`  
**Entity category:** biospecimen  
**Rows:** 20,000  
**Columns:** 9  
**Project:** ARDaC-AlcHepNet  
**Profile scope:** supplied chunk only

### Row grain

One physical row represents an aliquot record linked to a follow-up record and, where populated, a laboratory identifier.

### Important schema relationships

- `follow_ups` → `follow_up`: many-to-one and required by the schema.
- `labs` → `lab`: many-to-one and optional by the schema.

The physical file represents these relationships in flattened form:

- `*follow_ups.submitter_id`
- `labs.submitter_id`

### Key observations

- All 20,000 rows have values for the record type, project, submitter identifier, follow-up identifier, laboratory identifier, and specimen type.
- Three schema-supported physical fields are completely empty in this supplied chunk: `aliquot_amount`, `aliquot_collection_unit`, and `container_type`.
- The 20,000 rows contain 10,000 distinct aliquot submitter IDs, so the supplied rows are **not one-row-per-submit­ter-ID**.
- The data contain 2,031 distinct follow-up identifiers and 10 distinct lab identifiers.
- Thirteen distinct specimen types are represented.
- Because the file is explicitly a chunk, counts and distributions in this file should not automatically be generalized to the complete ARDaC release.

---

## 3.2 Column Profile

| Column | Role / Type | Non-empty | Missing | Completeness | Distinct | Uniqueness Ratio | Examples | Quality / Interpretation |
|---|---|---:|---:|---:|---:|---:|---|---|
| `*type` | Entity-type field | 20,000 | 0 | 100.0% | 1 | 0.005% | `aliquot` | Constant as expected for an aliquot table |
| `project_id` | Project identifier | 20,000 | 0 | 100.0% | 1 | 0.005% | `ARDaC-AlcHepNet` | Constant; all supplied rows belong to the same project |
| `*submitter_id` | Aliquot identifier | 20,000 | 0 | 100.0% | 10,000 | 50.0% | `71063BW00SE04`; `71063BW00SE03`; `42092BW00SE04` | Fully populated, but each distinct value appears more than once on average; do not assume this raw column alone is row-unique |
| `*follow_ups.submitter_id` | Follow-up relationship key | 20,000 | 0 | 100.0% | 2,031 | 10.155% | `71063_obs_0`; `42092_obs_0`; `31115_obs_0` | Required relationship is fully populated in this chunk |
| `labs.submitter_id` | Laboratory relationship key | 20,000 | 0 | 100.0% | 10 | 0.05% | `lab_1`; `lab_14`; `lab_15`; `lab_6`; `lab_3` | Although schema marks lab optional, it is populated for every supplied row |
| `aliquot_amount` | Numeric quantity | 0 | 20,000 | 0.0% | 0 | N/A | — | Entirely unpopulated; numeric statistics cannot be calculated |
| `aliquot_collection_unit` | Categorical unit | 0 | 20,000 | 0.0% | 0 | N/A | — | Entirely unpopulated despite schema allowing `gram`, `ml`, or `Collection Kit` |
| `container_type` | Categorical container | 0 | 20,000 | 0.0% | 0 | N/A | — | Entirely unpopulated in this chunk |
| `specimen_type` | Categorical biospecimen type | 20,000 | 0 | 100.0% | 13 | 0.065% | `Serum`; `Stool`; `Platelet Rich Plasma`; `Urine`; `Platelet Poor Plasma` | Fully populated; 13 observed categories out of the broader schema-defined domain |

---

## 3.3 Completeness Summary

### Fully populated columns

Six of nine columns are 100% complete:

1. `*type`
2. `project_id`
3. `*submitter_id`
4. `*follow_ups.submitter_id`
5. `labs.submitter_id`
6. `specimen_type`

### Completely unpopulated columns

Three of nine columns are 0% complete:

1. `aliquot_amount`
2. `aliquot_collection_unit`
3. `container_type`

### Table-level completeness interpretation

At the field-population level, the table has a sharply bimodal pattern: columns are either fully populated or completely empty in the supplied chunk.

This is useful for AI retrieval because the machine should **not attempt to answer aliquot-volume, collection-unit, or container questions from this physical file**. Those questions should instead be routed to the schema, protocol, or biorepository MOP unless another physical table supplies those values.

---

# 4. Categorical Characteristics

## 4.1 `specimen_type`

**Distinct observed values:** 13

Examples observed in the supplied chunk include:

- Serum
- Stool
- Platelet Rich Plasma
- Urine
- Platelet Poor Plasma

The schema allows a broader set of specimen types, including:

- Platelet Poor Plasma
- HCl Acidified Plasma
- HCl Sodium Citrate Plasma
- CPT Plasma
- PBMC
- Serum
- DNA
- Lysed RBC
- Platelet Rich Plasma
- Urine
- Stool
- Anakinra
- NEAT Plasma
- Saliva
- Whole Blood (DNA)
- Unknown Code
- Liver Tissue

**Interpretation:** 13 schema-compatible specimen categories are represented in the supplied physical chunk. The absence of a schema-allowed category from this chunk does not prove that the category is absent from the complete database.

## 4.2 `labs.submitter_id`

**Distinct observed values:** 10

Examples:

- `lab_1`
- `lab_14`
- `lab_15`
- `lab_6`
- `lab_3`

**Interpretation:** aliquot records in this chunk are distributed across at least 10 laboratory identifiers. Exact laboratory frequency counts should be regenerated from the physical file whenever a complete release is profiled.

## 4.3 `project_id`

All 20,000 records contain:

`ARDaC-AlcHepNet`

There is no project-level variation in this supplied chunk.

## 4.4 `*type`

All 20,000 records contain:

`aliquot`

This is internally consistent with the table's schema entity.

---

# 5. Numeric Characteristics

The only physical column in this table that is conceptually numeric is:

`aliquot_amount`

However, it contains **0 populated values out of 20,000 rows**.

Therefore the following statistics are currently **not calculable**:

- mean
- median
- standard deviation
- minimum
- maximum
- 25th percentile
- 75th percentile

This absence should be represented explicitly rather than returning zero as though zero were an observed aliquot quantity.

---

# 6. Identifier and Duplication Characteristics

## `*submitter_id`

- Non-empty rows: 20,000
- Distinct values: 10,000
- Uniqueness ratio: 50.0%

The submitter identifier is therefore not unique at the physical-row level in this supplied chunk.

**AI rule:** Do not equate `COUNT(rows)` with `COUNT(DISTINCT submitter_id)`.

For example:

- physical rows = 20,000
- distinct aliquot submitter IDs = 10,000

The reason for repeated submitter IDs cannot be determined safely from the summary alone. A downstream analysis should inspect the full raw table and other key columns before labeling the repeats as duplicates.

## Follow-up linkage

- 20,000 populated relationship values
- 2,031 distinct follow-up submitter IDs

Multiple aliquot rows can therefore link to the same follow-up record, which is expected for a biospecimen-oriented data model in which multiple aliquots may be associated with one visit/timepoint.

---

# 7. Schema-versus-Physical-Data Differences

The schema defines **13 fields** for the aliquot entity, but the supplied physical chunk contains **9 columns**.

Not every schema field is materialized in the supplied TSV chunk.

Important examples:

| Schema concept | Present in supplied physical chunk? | Physical representation |
|---|---|---|
| `type` | Yes | `*type` |
| `submitter_id` | Yes | `*submitter_id` |
| `project_id` | Yes | `project_id` |
| `follow_ups` | Yes | `*follow_ups.submitter_id` |
| `labs` | Yes | `labs.submitter_id` |
| `aliquot_amount` | Yes, but empty | `aliquot_amount` |
| `aliquot_collection_unit` | Yes, but empty | `aliquot_collection_unit` |
| `container_type` | Yes, but empty | `container_type` |
| `specimen_type` | Yes | `specimen_type` |
| `id` | No | — |
| `state` | No | — |
| `created_datetime` | No | — |
| `updated_datetime` | No | — |

**Retrieval rule:** The schema describes possible/defined attributes; this profile describes actual availability in the supplied release.

---

# 8. Data Quality Findings

## Finding 1 — Complete linkage to follow-up

The required follow-up relationship is 100% populated in the supplied chunk.

**Status:** Good for relationship-based retrieval.

## Finding 2 — Laboratory linkage exceeds minimum schema requirement

The schema marks `labs` optional, but `labs.submitter_id` is populated in all 20,000 supplied rows.

**Status:** Strong coverage in this chunk.

## Finding 3 — Three fully empty physical fields

`aliquot_amount`, `aliquot_collection_unit`, and `container_type` have no observed values.

**Status:** Major physical-data availability limitation.

**AI implication:** Do not infer amounts, units, or containers from this physical table.

## Finding 4 — Submitter identifier is not row-unique

20,000 physical rows contain only 10,000 distinct `*submitter_id` values.

**Status:** Requires caution.

**AI implication:** Use distinct counts when the question concerns unique aliquot identifiers. Do not automatically call repeated IDs erroneous duplicates.

## Finding 5 — File is a chunk

The physical file name contains `chunk_001`.

**Status:** Scope limitation.

**AI implication:** Treat distributions and row counts as chunk-specific unless the full release is known to contain only this chunk.

---

# 9. AI Retrieval Guidance

When an AI system receives a question about the database, use this order:

### Question: "What variables can an aliquot have?"
Use the **schema/Data Dictionary**.

### Question: "What aliquot fields are actually populated in the supplied data?"
Use this **Physical Data Characteristics Knowledge Base**.

### Question: "How many distinct aliquot IDs are in this supplied chunk?"
Answer: **10,000 distinct `*submitter_id` values**.

### Question: "How many physical records are in this supplied chunk?"
Answer: **20,000 rows**.

### Question: "Does the physical data contain aliquot amount?"
Answer: The column exists, but **0 of 20,000 rows are populated**.

### Question: "Can I determine the aliquot container from this table?"
Answer: No. `container_type` is present as a column but is **0% complete** in this chunk.

### Question: "Are specimen types available?"
Answer: Yes. `specimen_type` is **100% populated** and has **13 distinct observed values** in this chunk.

### Question: "How is an aliquot linked to a visit?"
Use `*follow_ups.submitter_id`; it is 100% populated in the supplied chunk.

---

# 10. Maintenance Rules for Future Data Releases

Whenever a physical table changes, update this file using the following workflow.

## A. Table-level update

For each table, record:

- file/release name
- profile date
- row count
- column count
- entity/grain
- key identifiers
- relationship fields
- whether the file is complete, filtered, or chunked

## B. Column-level update

For every column, recalculate:

- inferred/declared data type
- non-empty count
- missing count
- completeness %
- number of distinct values
- uniqueness ratio
- representative values
- schema-validity status

For numeric columns also calculate:

- mean
- median
- standard deviation
- minimum
- 25th percentile
- 75th percentile
- maximum

For categorical columns also calculate:

- category counts
- category percentages
- most common values
- newly appearing values
- values that disappeared relative to the prior release

## C. Cross-release change detection

Compare the new profile with the prior profile and flag:

- row-count increases or decreases
- added/removed columns
- large completeness changes
- new categorical values
- lost categorical values
- major distribution shifts
- changes in unique-key behavior
- new missing relationship keys
- schema-invalid values

## D. Do not silently overwrite important changes

Maintain a small change log so an AI system can identify what changed between releases.

---

# 11. Update Log Template

| Profile Date | Physical File / Release | Change | Impact |
|---|---|---|---|
| 2026-08-18 | `aliquot_DCC_data_release_v2-1-0_shipped_mapped_chunk_001(1).tsv` | Initial physical-data profile created | Establishes baseline table/column characteristics |

---

# 12. Expansion Template for Additional Physical Tables

Copy this section once for every new table.

## `[TABLE NAME]`

**Physical file:**  
**Schema entity:**  
**Rows:**  
**Columns:**  
**Row grain:**  
**Primary/key identifiers:**  
**Relationship fields:**  
**Coverage note:**  

### Column Profile

| Column | Type | Non-empty | Missing | Completeness | Distinct | Uniqueness Ratio | Numeric/Categorical Summary | Quality Note |
|---|---|---:|---:|---:|---:|---:|---|---|

### Key Distributions

Document the most important categorical distributions and numeric summaries.

### Data Quality Findings

Document missingness, duplication, validity, relationship-integrity, and distribution issues.

### AI Retrieval Notes

State what the AI can and cannot safely infer from this table.

---

# 13. Relationship to Existing Knowledge-Base Files

This file should be used together with:

- `database_overview.md` — high-level entity catalog
- `database_relationships.md` — exact schema relationships
- `variable_index.md` — variable lookup
- `database_knowledge_base_consolidated.md` — detailed schema reference
- `AlcHepNet_Umbrella_Knowledge_Base.md` — routing across study, protocol, MOP, training, schema, and data layers

Recommended retrieval pattern:

```text
User question
    ↓
Umbrella knowledge base
    ↓
Is the question about what SHOULD exist?
    → Data Dictionary / schema KB
    ↓
Is the question about what ACTUALLY exists in the current physical data?
    → Physical Data Characteristics KB
    ↓
If exact row-level evidence is required
    → Raw physical table
```

---

# 14. Current Bottom Line

The supplied aliquot chunk provides a useful physical-data baseline:

- **20,000 physical rows**
- **9 physical columns**
- **10,000 distinct aliquot submitter IDs**
- **2,031 distinct follow-up IDs**
- **10 distinct lab IDs**
- **13 distinct specimen types**
- **6 columns at 100% completeness**
- **3 columns at 0% completeness**

The strongest immediately usable physical fields are the identifiers, follow-up linkage, lab linkage, and specimen type. Aliquot amount, collection unit, and container type cannot currently be characterized because they are entirely missing in the supplied chunk.

As additional physical tables are supplied, they should be profiled using the same structure so this file becomes a maintainable machine-readable summary of the current AlcHepNet database.
