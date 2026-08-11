# Database Overview

**Schema version:** 2.1.1  
**Documented entities:** 54  
**Schema-defined relationships:** 102

## Entity categories

- **data_file:** 17 entities
- **administrative:** 12 entities
- **analysis:** 10 entities
- **clinical:** 7 entities
- **biospecimen:** 4 entities
- **notation:** 2 entities
- **index_file:** 1 entities
- **metadata_file:** 1 entities

## Entity catalog

| Entity | Title | Category | Fields | Links | Purpose |
|---|---|---:|---:|---:|---|
| [acknowledgement](entities/acknowledgement.md) | Acknowledgement | administrative | 9 | 1 | Acknowledgement of an individual involved in a project. |
| [aligned_reads](entities/aligned_reads.md) | Aligned Reads | data_file | 11 | 5 | Data file containing aligned reads that are generated internally by the GDC. |
| [aligned_reads_index](entities/aligned_reads_index.md) | Aligned Reads Index | index_file | 7 | 2 | Data file containing the index for a set of aligned reads. |
| [alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md) | Alignment Cocleaning Workflow | analysis | 5 | 2 | Metadata for the alignment and cocleaning pipeline used to align reads in the GDC harmonization pipelines. |
| [alignment_workflow](entities/alignment_workflow.md) | Alignment Workflow | analysis | 5 | 2 | Metadata for the alignment pipeline used to align reads in the GDC harmonization pipelines. |
| [aliquot](entities/aliquot.md) | Aliquot | biospecimen | 13 | 2 | Pertaining to a portion of the whole; any one of two or more samples of something, of the same volume or weight. |
| [audit](entities/audit.md) | Audit | administrative | 33 | 1 | audit to a case. |
| [case](entities/case.md) | Case | administrative | 27 | 1 | The collection of all data related to a specific subject in the context of a specific experiment. |
| [clinical_test](entities/clinical_test.md) | Clinical Test | clinical | 29 | 3 | Metadata concerning any clinical tests used in relation to a case diagnosis. |
| [copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md) | Copy Number Auxiliary File | data_file | 8 | 2 | Data file related to the copy number pipeline that contains any outputs not strictly defined in other nodes |
| [copy_number_estimate](entities/copy_number_estimate.md) | Copy Number Estimate | data_file | 10 | 4 | Data file containing copy number variation information generated internally by the GDC. |
| [copy_number_liftover_workflow](entities/copy_number_liftover_workflow.md) | Copy Number Liftover Workflow | analysis | 3 | 1 | Metadata for the copy number liftover workflow used to harmonize TCGA copy number data. |
| [copy_number_segment](entities/copy_number_segment.md) | Copy Number Segment | data_file | 10 | 4 | Data file containing the copy number data from a copy number liftover workflow. Contains all copy numbers detected. |
| [copy_number_variation_workflow](entities/copy_number_variation_workflow.md) | Copy Number Variation Workflow | analysis | 3 | 1 | Metadata for the Copy Number Variation pipeline used to estimate copy number changes from different molecular data sources. |
| [core_metadata_collection](entities/core_metadata_collection.md) | Core Metadata Collection | administrative | 16 | 1 | Structured description of a collection of several dataset |
| [demographic](entities/demographic.md) | Demographic | clinical | 23 | 1 | Data for the characterization of the patient by means of segementing the population (e.g., characterization by age, sex, or race). |
| [diagnosis](entities/diagnosis.md) | Diagnosis | clinical | 61 | 2 | Data from the investigation, analysis and recognition of the presence and nature of disease, condition, or injury from expressed signs and symptoms; also, the scientific determination of any kind; the concise results of such an investigation. |
| [experiment](entities/experiment.md) | Experiment | administrative | 21 | 1 | A coordinated set of actions and observations designed to generate data, with the ultimate goal of discovery or hypothesis testing. |
| [experimental_metadata](entities/experimental_metadata.md) | Experimental Metadata | metadata_file | 7 | 2 | Data file containing the metadata for the experiment performed. |
| [exposure](entities/exposure.md) | Exposure | clinical | 19 | 1 | Clinically relevant patient information not immediately resulting from genetic predispositions. |
| [family_history](entities/family_history.md) | Family History | clinical | 13 | 1 | Record of a patient's background regarding cancer events of blood relatives. |
| [follow_up](entities/follow_up.md) | Follow_up | administrative | 110 | 2 | follow_up for a project. |
| [gene_expression](entities/gene_expression.md) | Gene Expression | data_file | 7 | 2 | Data file containing gene expression information generated internally by the GDC. |
| [genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md) | Genomic Profile Harmonization Workflow | analysis | 3 | 1 | Metadata for the harmonization of genomic profiling reports. |
| [germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md) | Germline Mutation Calling Workflow | analysis | 5 | 2 | Metadata for the germline mutation calling pipeline used to call variants in the GDC DNA-Seq pipelines. |
| [keyword](entities/keyword.md) | Keyword | administrative | 9 | 1 | A keyword for a project. |
| [lab](entities/lab.md) | Lab | administrative | 24 | 1 | ARDaC: Lab node describes different lab centers, which are different data sources. |
| [mirna_expression](entities/mirna_expression.md) | miRNA Expression | data_file | 7 | 2 | Data file containing miRNA expression information generated internally by the GDC. |
| [mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md) | miRNA Expression Calling Workflow | analysis | 5 | 2 | Metadata for the miRNA expression calling pipeline. |
| [molecular_test](entities/molecular_test.md) | Molecular_test | clinical | 19 | 3 | Data for the characterization of the patient by means of segementing the population (e.g., characterization by age, sex, or race). |
| [program](entities/program.md) | Program | administrative | 4 | 0 | A broad framework of goals to be achieved. (NCIt C52647) |
| [project](entities/project.md) | Project | administrative | 17 | 1 | Any specifically defined piece of work that is undertaken or attempted to meet a single requirement. (NCIt C47885) |
| [publication](entities/publication.md) | Publication | administrative | 10 | 1 | Publication for a project. |
| [read_group](entities/read_group.md) | Read Group | biospecimen | 54 | 1 | Sequencing reads from one lane of an NGS experiment. |
| [read_group_qc](entities/read_group_qc.md) | Read Group QC | notation | 24 | 3 | GDC QC run metadata. |
| [rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md) | RNA Expression Calling Workflow | analysis | 6 | 3 | Metadata for the RNA expression pipeline used to quantify RNA gene and exon expression from unharmonized or GDC harmonized data. |
| [sample](entities/sample.md) | Sample | biospecimen | 35 | 2 | Any material sample taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes, including a sample obtained from a living organism or taken from the biological object after halting of all its life functions. Biospecimen can contain one or more components including but not limited to cellular molecules, cells, tissues, organs, body fluids, embryos, and body excretory products. |
| [simple_germline_variation](entities/simple_germline_variation.md) | Simple Germline Variation | data_file | 10 | 5 | Data file containing simple germline variations called from aligned reads. |
| [slide](entities/slide.md) | Slide | biospecimen | 30 | 1 | A digital image, microscopic or otherwise, of any sample, portion, or sub-part thereof. (GDC) |
| [slide_count](entities/slide_count.md) | Slide Count | notation | 20 | 1 | Information pertaining to processed results obtained from slides; often in the form of counts. |
| [slide_image](entities/slide_image.md) | Slide Image | data_file | 15 | 2 | Data file containing image of a slide. |
| [somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md) | Somatic Copy Number Workflow | analysis | 4 | 2 | Metadata for the Somatic Copy Number pipeline used to estimate copy number changes from different molecular data sources. |
| [structural_variant_calling_workflow](entities/structural_variant_calling_workflow.md) | Structural Variant Calling Workflow | analysis | 3 | 1 | Metadata for the structural variant calling pipeline used to call structural variants in the GDC DNA-Seq or RNA-Seq pipelines. |
| [structural_variation](entities/structural_variation.md) | structural_variation | data_file | 9 | 3 | Structural_variation reads that are used as input to GDC workflows. |
| [study](entities/study.md) | Study | administrative | 12 | 1 | The study node. |
| [submitted_aligned_reads](entities/submitted_aligned_reads.md) | Submitted Aligned Reads | data_file | 9 | 2 | Data file containing aligned reads that are used as input to GDC workflows. |
| [submitted_copy_number](entities/submitted_copy_number.md) | Submitted Copy Number | data_file | 9 | 3 | Data file containing normalized copy number information from an aliquot. |
| [submitted_genomic_profile](entities/submitted_genomic_profile.md) | Submitted Genomic Profile | data_file | 8 | 2 | Data file containing genomic profile information. |
| [submitted_genotyping_array](entities/submitted_genotyping_array.md) | Submitted Genotyping Array | data_file | 8 | 2 | Data file containing raw data from a genotyping array. |
| [submitted_methylation](entities/submitted_methylation.md) | Submitted Methylation | data_file | 10 | 2 | DNA methylation data files contain information on raw and normalized signal intensities, detection confidence and calculated beta values for methylated and unmethylated probes. DNA methylation is an epigenetic mark which can be associated with transcriptional inactivity when located in promoter regions. |
| [submitted_somatic_mutation](entities/submitted_somatic_mutation.md) | Submitted Somatic Mutation | data_file | 9 | 2 | Data file containing somatic mutation calls from a read group. |
| [submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md) | Submitted Tangent Copy Number | data_file | 7 | 2 | Data file containing tangent normalized copy number information from an aliquot. |
| [submitted_unaligned_reads](entities/submitted_unaligned_reads.md) | Submitted Unaligned Reads | data_file | 9 | 2 | Data file containing unaligned reads that have not been GDC Harmonized. |
| [treatment](entities/treatment.md) | Treatment | clinical | 18 | 2 | Record of the administration and intention of therapeutic agents provided to a patient to alter the course of a pathologic process. |

## Core navigation hubs

- **[core_metadata_collection](entities/core_metadata_collection.md):** 1 outgoing link(s), 19 incoming link(s).
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** 2 outgoing link(s), 9 incoming link(s).
- **[aligned_reads](entities/aligned_reads.md):** 5 outgoing link(s), 6 incoming link(s).
- **[aliquot](entities/aliquot.md):** 2 outgoing link(s), 6 incoming link(s).
- **[case](entities/case.md):** 1 outgoing link(s), 7 incoming link(s).
- **[project](entities/project.md):** 1 outgoing link(s), 7 incoming link(s).
- **[read_group](entities/read_group.md):** 1 outgoing link(s), 7 incoming link(s).
- **[follow_up](entities/follow_up.md):** 2 outgoing link(s), 6 incoming link(s).
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** 2 outgoing link(s), 5 incoming link(s).
- **[diagnosis](entities/diagnosis.md):** 2 outgoing link(s), 3 incoming link(s).
- **[copy_number_segment](entities/copy_number_segment.md):** 4 outgoing link(s), 1 incoming link(s).
- **[simple_germline_variation](entities/simple_germline_variation.md):** 5 outgoing link(s), 0 incoming link(s).
- **[somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md):** 2 outgoing link(s), 3 incoming link(s).
- **[copy_number_estimate](entities/copy_number_estimate.md):** 4 outgoing link(s), 0 incoming link(s).
- **[genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md):** 1 outgoing link(s), 3 incoming link(s).

## How to interpret schema relationships

- **Required relationship:** the schema marks the link as required for the source entity.
- **Multiplicity:** values such as `many_to_one` or `one_to_one` are copied from the schema and describe the source-to-target relationship.
- **Back-reference:** the target-side collection/name declared by the source schema.
- **Link field:** the source property used to reference the target entity, generally represented by a submitter identifier or UUID object according to the shared definitions.

## Shared identifier conventions

- `id` uses the shared UUID definition where present.
- `submitter_id` is a project- or submitter-specific identifier where present.
- `project_id` identifies project membership/context where present.
- Relationship properties commonly resolve through the shared `to_one` / `to_many` foreign-key structures, which support `id` and/or `submitter_id` references.

## Recommended retrieval strategy

For questions about a concept or variable, search the [variable index](variable_index.md). For questions about where information lives or how records connect, use the [relationship map](database_relationships.md). For exact definitions, restrictions, and allowed values, use the relevant entity page.
