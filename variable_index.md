# Variable Index

This index contains **492 unique field names** across **54 schema entities**. A field can appear in more than one entity with the same or different definitions.

## Alphabetical index

### `$ref`

- **[aligned_reads](entities/aligned_reads.md):** `type not stated`; optional/not marked required
- **[aligned_reads_index](entities/aligned_reads_index.md):** `type not stated`; optional/not marked required
- **[alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md):** `type not stated`; optional/not marked required
- **[alignment_workflow](entities/alignment_workflow.md):** `type not stated`; optional/not marked required
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `type not stated`; optional/not marked required
- **[copy_number_estimate](entities/copy_number_estimate.md):** `type not stated`; optional/not marked required
- **[copy_number_liftover_workflow](entities/copy_number_liftover_workflow.md):** `type not stated`; optional/not marked required
- **[copy_number_segment](entities/copy_number_segment.md):** `type not stated`; optional/not marked required
- **[copy_number_variation_workflow](entities/copy_number_variation_workflow.md):** `type not stated`; optional/not marked required
- **[core_metadata_collection](entities/core_metadata_collection.md):** `type not stated`; optional/not marked required
- **[experimental_metadata](entities/experimental_metadata.md):** `type not stated`; optional/not marked required
- **[gene_expression](entities/gene_expression.md):** `type not stated`; optional/not marked required
- **[genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md):** `type not stated`; optional/not marked required
- **[germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md):** `type not stated`; optional/not marked required
- **[mirna_expression](entities/mirna_expression.md):** `type not stated`; optional/not marked required
- **[mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md):** `type not stated`; optional/not marked required
- **[read_group_qc](entities/read_group_qc.md):** `type not stated`; optional/not marked required
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `type not stated`; optional/not marked required
- **[simple_germline_variation](entities/simple_germline_variation.md):** `type not stated`; optional/not marked required
- **[slide_image](entities/slide_image.md):** `type not stated`; optional/not marked required
- **[somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md):** `type not stated`; optional/not marked required
- **[structural_variant_calling_workflow](entities/structural_variant_calling_workflow.md):** `type not stated`; optional/not marked required
- **[structural_variation](entities/structural_variation.md):** `type not stated`; optional/not marked required
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `type not stated`; optional/not marked required
- **[submitted_copy_number](entities/submitted_copy_number.md):** `type not stated`; optional/not marked required
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `type not stated`; optional/not marked required
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `type not stated`; optional/not marked required
- **[submitted_methylation](entities/submitted_methylation.md):** `type not stated`; optional/not marked required
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `type not stated`; optional/not marked required
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `type not stated`; optional/not marked required
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `type not stated`; optional/not marked required

### `acknowledgee`

- **[acknowledgement](entities/acknowledgement.md):** `string`; optional/not marked required. The indvidiual or group being acknowledged by the project.

### `actarm`

- **[case](entities/case.md):** `enum`; optional/not marked required. Description of actual Arm. When an Arm is not planned, ACTARM will be “Unplanned Treatment”. Randomized subjects who were not treated will be given a value of “Not Treated”. Values should be “Screen Failure” for screen failures and “Not Assigned” for subjects not assigned to treatment. Restricted to values in Trial Arms in all other cases. Allowed values: Prednisone; Anakinra + Zinc; Not Treated.

### `adapter_content`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `adapter_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of the sequencing adapter.

### `adapter_sequence`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Base sequence of the sequencing adapter.

### `address`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Address.

### `admission_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of admission for patients who were hospitalized at time of enrollment. In (YYYY-MM-DD) format.

### `adt0101`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0101 Allowed values: 2 to 3 times a week; 2 to 4 times a month; 4 or more times a week; Monthly or less; Never; Not Done/Missing; … (+1 more).

### `adt0102`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0102 Allowed values: 1 or 2; 3 or 4; 5 or 6; 7 to 9; 10 or more; Not Done/Missing; … (+1 more).

### `adt0103`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0103 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0104`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0104 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0105`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0105 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0106`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0106 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0107`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0107 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0108`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0108 Allowed values: Never; Weekly; Less than monthly; Daily or almost daily; Monthly; Not Done/Missing; … (+1 more).

### `adt0109`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0109 Allowed values: No; Yes, during the last year; Yes, but not in the last year; Not Done/Missing; null.

### `adt0110`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. adt0110 Allowed values: No; Yes, during the last year; Yes, but not in the last year; Not Done/Missing; null.

### `adtcomploth`

- **[audit](entities/audit.md):** `string / null`; optional/not marked required. adtcomploth

### `age_at_diagnosis`

- **[diagnosis](entities/diagnosis.md):** `number / null`; required. Age at the time of diagnosis expressed in number of days since birth.

### `age_at_index`

- **[demographic](entities/demographic.md):** `number / null`; optional/not marked required. The patient's age (in years) on the reference or anchor date date used during date obfuscation.

### `ah_hosp`

- **[case](entities/case.md):** `enum`; optional/not marked required. Boolean variable that describes in the last year, were you hospitalized due to Alcoholic Hepatitis? Allowed values: Yes; No.

### `ah_hosp_num`

- **[case](entities/case.md):** `number`; optional/not marked required. Numeric term used to desceibe how many times that patient was hospitalized for alcoholic hepatitis?

### `ajcc_clinical_m`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment. Allowed values: M0; M1; M1a; M1b; M1c; MX; … (+4 more).

### `ajcc_clinical_n`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment. Allowed values: N0; N0 (i+); N0 (i-); N0 (mol+); N0 (mol-); N1; … (+21 more).

### `ajcc_clinical_stage`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis for cancer. Allowed values: Stage 0; Stage 0a; Stage 0is; Stage I; Stage IA; Stage IA1; … (+25 more).

### `ajcc_clinical_t`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment. Allowed values: T0; T1; T1a; T1a1; T1a2; T1b; … (+31 more).

### `ajcc_pathologic_m`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC). Allowed values: M0; M1; M1a; M1b; M1c; M2; … (+5 more).

### `ajcc_pathologic_n`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual. Allowed values: N0; N0 (i+); N0 (i-); N0 (mol+); N0 (mol-); N1; … (+21 more).

### `ajcc_pathologic_stage`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria. Allowed values: Stage 0; Stage 0a; Stage 0is; Stage I; Stage IA; Stage IA1; … (+21 more).

### `ajcc_pathologic_t`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC). Allowed values: T0; T1; T1a; T1a1; T1a2; T1b; … (+31 more).

### `aki_status`

- **[case](entities/case.md):** `enum`; optional/not marked required. Aki status of the patient. Allowed values: Yes; No; Unknown.

### `alcohol_history`

- **[exposure](entities/exposure.md):** `string`; optional/not marked required. A response to a question that asks whether the participant has consumed at least 12 drinks of any kind of alcoholic beverage in their lifetime.

### `alcohol_intensity`

- **[exposure](entities/exposure.md):** `string`; optional/not marked required. Category to describe the patient's current level of alcohol use as self-reported by the patient.

### `aligned_reads_files`

- **[germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md):** `to_many`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)
- **[mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md):** `to_many`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `to_one`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)
- **[simple_germline_variation](entities/simple_germline_variation.md):** `to_many`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)
- **[somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md):** `to_many`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)
- **[structural_variant_calling_workflow](entities/structural_variant_calling_workflow.md):** `to_many`; optional/not marked required; relationship target [aligned_reads](entities/aligned_reads.md)

### `alignment_cocleaning_workflows`

- **[aligned_reads](entities/aligned_reads.md):** `to_one`; optional/not marked required; relationship target [alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md)

### `alignment_workflows`

- **[aligned_reads](entities/aligned_reads.md):** `to_one`; optional/not marked required; relationship target [alignment_workflow](entities/alignment_workflow.md)

### `aliquot_amount`

- **[aliquot](entities/aliquot.md):** `number`; optional/not marked required. Aliquot quantity, (weight in grams or volume in ml and other units).

### `aliquot_collection_unit`

- **[aliquot](entities/aliquot.md):** `enum`; optional/not marked required. Unit of the aliquot sample ( example: grams, ml, etc). Allowed values: gram; ml; Collection Kit.

### `aliquots`

- **[molecular_test](entities/molecular_test.md):** `to_one`; optional/not marked required; relationship target [aliquot](entities/aliquot.md)
- **[read_group](entities/read_group.md):** `to_one`; required; relationship target [aliquot](entities/aliquot.md)
- **[submitted_copy_number](entities/submitted_copy_number.md):** `to_one`; optional/not marked required; relationship target [aliquot](entities/aliquot.md)
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `to_one`; optional/not marked required; relationship target [aliquot](entities/aliquot.md)
- **[submitted_methylation](entities/submitted_methylation.md):** `to_one`; optional/not marked required; relationship target [aliquot](entities/aliquot.md)
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `to_one`; optional/not marked required; relationship target [aliquot](entities/aliquot.md)

### `ann_arbor_b_symptoms`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to signify whether lymphoma B-symptoms are present as noted in the patient's medical record. Allowed values: Yes; No; Unknown; Not Reported; Not Allowed To Collect.

### `ann_arbor_clinical_stage`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The classification of the clinically confirmed anatomic disease extent of lymphoma (Hodgkin's and Non-Hodgkins) based on the Ann Arbor Staging System. Allowed values: Stage I; Stage II; Stage III; Stage IV.

### `ann_arbor_extranodal_involvement`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Indicator that identifies whether a patient with malignant lymphoma has lymphomatous involvement of an extranodal site. Allowed values: Yes; No; Unknown; Not Reported; Not Allowed To Collect.

### `ann_arbor_pathologic_stage`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The classification of the pathologically confirmed anatomic disease extent of lymphoma (Hodgkin's and Non-Hodgkins) based on the Ann Arbor Staging System. Allowed values: Stage I; Stage II; Stage III; Stage IV.

### `apoptotic_concentration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. The concentration, in cells/mL, of apoptotic cells in the slide blood.

### `ascites_culture`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator to describe the state of ascites presence at a particular time. Allowed values: Yes; No; Not Reported; Not Done; Missing.

### `ascites_culture_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text used to describe the results of the ascites culture test. Allowed values: Positive; Negative; Missing.

### `ascites_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of ascites culture test. In (YYYY-MM-DD) format.

### `ascites_diagnosis_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of most recent ascites diagnosis. In (YYYY-MM-DD) format.

### `ascites_organism`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The text term used to describe the organism growth found ascites culture.

### `assay_instrument`

- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; optional/not marked required Allowed values: Illumina.

### `assay_instrument_model`

- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; optional/not marked required Allowed values: Illumina Infinium HumanMethylation450; Illumina Infinium HumanMethylation450K.

### `assay_method`

- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; optional/not marked required Allowed values: Methylation Array.

### `associated_experiment`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. The submitter_id for any experiment with which this experiment is associated, paired, or matched.

### `auditnd`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. auditnd Allowed values: No; Yes; null.

### `availability_mechanism`

- **[project](entities/project.md):** `string`; optional/not marked required. Mechanism by which the project will be made avilable.

### `availability_type`

- **[project](entities/project.md):** `enum`; optional/not marked required. Is the project open or restricted? Allowed values: Open; Restricted.

### `barcoding_applied`

- **[read_group](entities/read_group.md):** `boolean`; optional/not marked required. True/False: was barcoding applied?

### `bari_surgery`

- **[case](entities/case.md):** `enum`; optional/not marked required. Boolean variable that describes whether the patient ever had any type of Bariatric Surgery? Allowed values: Yes; No.

### `bariatric_surgery`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the patient has ever had any type of bariatric surgery. Allowed values: Yes; No; Not Reported.

### `base_caller_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of the base caller.

### `base_caller_version`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Version of the base caller.

### `basic_statistics`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `biomarker_name`

- **[clinical_test](entities/clinical_test.md):** `string`; required. The name of the biomarker being tested for this specimen and set of test results.

### `biomarker_result`

- **[clinical_test](entities/clinical_test.md):** `enum`; required. Text term to define the results of genetic testing. Allowed values: Amplification; Gain; Loss; Normal; Other; Translocation; … (+3 more).

### `biomarker_signal`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. Numeric quantification of the biomarker signal.

### `biomarker_test_method`

- **[clinical_test](entities/clinical_test.md):** `enum`; required. Text descriptor of a molecular analysis method used for an individual. Allowed values: Cytogenetics; FISH; IHC; Karyotype; NGS; Nuclear Staining; … (+6 more).

### `blood_culture`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if a blood culture was done. Allowed values: Yes; No.

### `blood_culture_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of blood culture. In (YYYY-MM-DD) format.

### `blood_culture_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the results of the blood culture test. Allowed values: Positive; Negative.

### `blood_organism`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Text used to describe the organism growth found during blood culture.

### `blood_test_normal_range_lower`

- **[molecular_test](entities/molecular_test.md):** `number`; optional/not marked required. Numeric value used to describe the lower limit of the normal range used to describe a healthy individual at the institution where the test was completed.

### `blood_test_normal_range_upper`

- **[molecular_test](entities/molecular_test.md):** `number`; optional/not marked required. Numeric value used to describe the upper limit of the normal range used to describe a healthy individual at the institution where the test was completed.

### `bmi`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. The body mass divided by the square of the body height expressed in units of kg/m^2.
- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. A calculated numerical quantity that represents an individual's weight to height ratio.

### `burkitt_lymphoma_clinical_variant`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Burkitt's lymphoma categorization based on clinical features that differ from other forms of the same disease. Allowed values: Endemic; Immunodeficiency-associated, adult; Immunodeficiency-associated, pediatric; Sporadic, adult; Sporadic, pediatric; Unknown; … (+2 more).

### `cases`

- **[audit](entities/audit.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)
- **[clinical_test](entities/clinical_test.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)
- **[demographic](entities/demographic.md):** `to_one`; required; relationship target [case](entities/case.md)
- **[diagnosis](entities/diagnosis.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)
- **[exposure](entities/exposure.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)
- **[family_history](entities/family_history.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)
- **[follow_up](entities/follow_up.md):** `to_one`; optional/not marked required; relationship target [case](entities/case.md)

### `cause_of_death`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to identify the cause of death for a patient. Allowed values: Cancer Related; Not Cancer Related; Unknown.

### `cause_of_death_primary`

- **[demographic](entities/demographic.md):** `string`; optional/not marked required. Text term to identify the primary cause of death for a patient.

### `cause_of_death_secondary`

- **[demographic](entities/demographic.md):** `string`; optional/not marked required. Text term to identify the secondary cause of death for a patient.

### `cdc_hiv_risk_factors`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe a risk factor for human immunodeficiency virus, as described by the Center for Disease Control. Allowed values: Hemophiliac; Heterosexual Contact; Homosexual Contact; Intravenous Drug User; None; Not Reported; … (+2 more).

### `cea_level_preoperative`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. Numeric value of the Carcinoembryonic antigen or CEA at the time before surgery. [Manually- curated]

### `cell_count`

- **[slide_count](entities/slide_count.md):** `integer`; optional/not marked required. Raw count of a particular cell type.
- **[slide_image](entities/slide_image.md):** `integer`; optional/not marked required. Count of the cell type being imaged or otherwise analysed.

### `cell_identifier`

- **[slide_count](entities/slide_count.md):** `string`; optional/not marked required. An alternative identifier for a given cell type.
- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. An alternative identifier for a given cell type.

### `cell_type`

- **[slide_count](entities/slide_count.md):** `string`; optional/not marked required. The type of cell being counted or measured.
- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. The type of cell being imaged or otherwised analysed.

### `center_type`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Type classification of the lab (e.g. CGCC).

### `child_pugh_score`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for Child Pugh Score.

### `chipseq_antibody`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. NEW: The antibody used in the ChIP-Seq assay. Allowed values: abcam ab4729 anti-H3K27ac; Unknown; Not Applicable.

### `chipseq_target`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. NEW: The antibody used in the ChIP-Seq assay. Allowed values: H3K4me1; H3K4me3; H3K9me3; H3K27me3; H3K36me3; H3K27ac; … (+2 more).

### `cigarettes_per_day`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. The average number of cigarettes smoked per day.

### `circumferential_resection_margin`

- **[diagnosis](entities/diagnosis.md):** `number`; optional/not marked required. A value in millimeters indicating the measured length between a malignant lesion of the colon or rectum and the nearest radial (or circumferential) border of tissue removed during cancer surgery.

### `ck_signal`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. Numeric quantification of the CK signal.

### `classification_of_tumor`

- **[diagnosis](entities/diagnosis.md):** `enum`; required. Text that describes the kind of disease present in the tumor specimen as related to a specific timepoint. Allowed values: primary; metastasis; recurrence; other; Unknown; not reported; … (+1 more).

### `code`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Numeric code for the lab.
- **[project](entities/project.md):** `string`; required. Unique identifier for the project.

### `cohort`

- **[case](entities/case.md):** `enum`; optional/not marked required. The text term used to describe the study arm of the patient. Allowed values: Heavy Drinker with Alcoholic Hepatits; Heavy Drinker without Alcoholic Hepatits; Healthy Donor.

### `colon_polyps_history`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report (s). Allowed values: Yes; No; Unknown; Not Reported; Not Allowed To Collect.

### `consent_type`

- **[case](entities/case.md):** `enum`; optional/not marked required. The text term used to describe the type of consent obtain from the subject for participation in the study. Allowed values: Consent by Death; Consent Exemption; Consent Waiver; Informed Consent.

### `contact_email`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Contact’s email.

### `contact_name`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Contact’s name.

### `container_type`

- **[aliquot](entities/aliquot.md):** `enum`; optional/not marked required. Term to describe type of container in which Aliquot was collected. Allowed values: 2 ml microtubes; 1.5 ml Fisherbrand Sterile Microcentrifuge Tubes with Screw Caps; 1.8 ml cryovials; 5 ml cryovials; 15 ml cryovials; Collection Cups; … (+1 more).

### `contributor`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. An entity responsible for making contributions to the resource. Examples of a Contributor include a person, an organization, or a service. Typically, the name of a Contributor should be used to indicate the entity.

### `copy_number_liftover_workflows`

- **[copy_number_segment](entities/copy_number_segment.md):** `to_one`; optional/not marked required; relationship target [copy_number_liftover_workflow](entities/copy_number_liftover_workflow.md)

### `copy_number_segments`

- **[copy_number_variation_workflow](entities/copy_number_variation_workflow.md):** `to_many`; optional/not marked required; relationship target [copy_number_segment](entities/copy_number_segment.md)

### `copy_number_variation_workflows`

- **[copy_number_estimate](entities/copy_number_estimate.md):** `to_one`; optional/not marked required; relationship target [copy_number_variation_workflow](entities/copy_number_variation_workflow.md)

### `copy_numbers_identified`

- **[experiment](entities/experiment.md):** `boolean`; optional/not marked required. Are copy number variations identified in this experiment?

### `core_metadata_collections`

- **[aligned_reads](entities/aligned_reads.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[aligned_reads_index](entities/aligned_reads_index.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[copy_number_estimate](entities/copy_number_estimate.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[copy_number_segment](entities/copy_number_segment.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[experimental_metadata](entities/experimental_metadata.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[gene_expression](entities/gene_expression.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[mirna_expression](entities/mirna_expression.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[simple_germline_variation](entities/simple_germline_variation.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[slide_image](entities/slide_image.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[structural_variation](entities/structural_variation.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_copy_number](entities/submitted_copy_number.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_methylation](entities/submitted_methylation.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `to_one`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `to_many`; optional/not marked required; relationship target [core_metadata_collection](entities/core_metadata_collection.md)

### `coverage`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. The spatial or temporal topic of the resource, the spatial applicability of the resource, or the jurisdiction under which the resource is relevant. Spatial topic and spatial applicability may be a named place or a location specified by its geographic coordinates. Temporal topic may be a named period, date, or date range. A jurisdiction may be a named administrative entity or a geographic place to which the resource applies. Recommended best practice is to use a controlled vocabulary such as the Thesaurus of Geographic Names [TGN] (http://www.getty.edu/research/tools/vocabulary/tgn/index.html). Where appropriate, named places or time periods can be used in preference to numeric identifiers such as sets of coordinates or date ranges.

### `created_datetime`

- **[acknowledgement](entities/acknowledgement.md):** `datetime`; optional/not marked required
- **[aliquot](entities/aliquot.md):** `datetime`; optional/not marked required
- **[audit](entities/audit.md):** `datetime`; optional/not marked required
- **[case](entities/case.md):** `datetime`; optional/not marked required
- **[clinical_test](entities/clinical_test.md):** `datetime`; optional/not marked required
- **[demographic](entities/demographic.md):** `datetime`; optional/not marked required
- **[diagnosis](entities/diagnosis.md):** `datetime`; optional/not marked required
- **[experiment](entities/experiment.md):** `datetime`; optional/not marked required
- **[exposure](entities/exposure.md):** `datetime`; optional/not marked required
- **[family_history](entities/family_history.md):** `datetime`; optional/not marked required
- **[follow_up](entities/follow_up.md):** `datetime`; optional/not marked required
- **[keyword](entities/keyword.md):** `datetime`; optional/not marked required
- **[lab](entities/lab.md):** `datetime`; optional/not marked required
- **[molecular_test](entities/molecular_test.md):** `datetime`; optional/not marked required
- **[publication](entities/publication.md):** `datetime`; optional/not marked required
- **[read_group](entities/read_group.md):** `datetime`; optional/not marked required
- **[sample](entities/sample.md):** `datetime`; optional/not marked required
- **[slide](entities/slide.md):** `datetime`; optional/not marked required
- **[slide_count](entities/slide_count.md):** `datetime`; optional/not marked required
- **[study](entities/study.md):** `datetime`; optional/not marked required
- **[treatment](entities/treatment.md):** `datetime`; optional/not marked required

### `creator`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. An entity primarily responsible for making the resource. Examples of a Creator include a person, an organization, or a service. Typically, the name of a Creator should be used to indicate the entity.

### `ct_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of CT. In (YYYY-MM-DD) format.

### `ct_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the results of the ultrasound. Allowed values: Normal; Abnormal; Missing.

### `ct_result_finding`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Description of the overall findings/impressions of the CT.

### `ct_result_sig`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the CT results are clinically significant. Allowed values: Yes; No; Missing.

### `ctc_concentration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. The concentration, in cells/mL, of traditional CTC cells (intact and enlarged cell and nucleus, cytokeratin positive, and CD45 negative) in the slide blood.

### `ctc_low_concentration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. The concentration, in cells/mL, of CTC-low cells (those with low cytokeratin levels compared to traditional CTCs) in the slide blood.

### `ctc_small_concentration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. The concentration, in cells/mL, of CTC-small cells (those with a small nuclear and cellular size relative to traditional CTCs) in the slide blood.

### `cur_employ_stat`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. The indicator to ask if the patient is currently employed. Allowed values: No; Not sure; Missing; Yes.

### `data_category`

- **[aligned_reads](entities/aligned_reads.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Sequencing Data; Sequencing Reads; Raw Sequencing Data.
- **[aligned_reads_index](entities/aligned_reads_index.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Sequencing Data; Sequencing Reads; Raw Sequencing Data.
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Copy Number Variation.
- **[copy_number_estimate](entities/copy_number_estimate.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Copy Number Variation.
- **[copy_number_segment](entities/copy_number_segment.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Copy Number Variation.
- **[experimental_metadata](entities/experimental_metadata.md):** `string`; required. Broad categorization of the contents of the data file.
- **[gene_expression](entities/gene_expression.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Transcriptome Profiling.
- **[mirna_expression](entities/mirna_expression.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Transcriptome Profiling.
- **[simple_germline_variation](entities/simple_germline_variation.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Simple Nucleotide Variation.
- **[slide_image](entities/slide_image.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Biospecimen; Slide Image; Mass Cytometry.
- **[structural_variation](entities/structural_variation.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Somatic Structural Variation; Structural Variation.
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Sequencing Data; Sequencing Reads; Raw Sequencing Data.
- **[submitted_copy_number](entities/submitted_copy_number.md):** `string`; required. Broad categorization of the contents of the data file.
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Combined Nucleotide Variation; Genomic Profiling.
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Copy Number Variation.
- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Methylation Data.
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `string`; required. Broad categorization of the contents of the data file.
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Copy Number Variation.
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; required. Broad categorization of the contents of the data file. Allowed values: Sequencing Data; Sequencing Reads; Raw Sequencing Data.

### `data_description`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. Brief description of the data being provided for this experiment.
- **[study](entities/study.md):** `string`; optional/not marked required. Brief description of the data being provided for this study. Free text.

### `data_format`

- **[aligned_reads](entities/aligned_reads.md):** `enum`; required. Format of the data files. Allowed values: BAM; CRAM.
- **[aligned_reads_index](entities/aligned_reads_index.md):** `enum`; required. UPDATED: Format of the data files. Allowed values: BAI; CRAI.
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `enum`; required. Format of the data files. Allowed values: TAR.
- **[copy_number_estimate](entities/copy_number_estimate.md):** `enum`; required. Format of the data files. Allowed values: TSV; TXT.
- **[copy_number_segment](entities/copy_number_segment.md):** `enum`; required. Format of the data files. Allowed values: TXT.
- **[experimental_metadata](entities/experimental_metadata.md):** `string`; required. Format of the data files.
- **[gene_expression](entities/gene_expression.md):** `enum`; required. Format of the data files. Allowed values: CSV; HDF5; MEX; TSV; TXT.
- **[mirna_expression](entities/mirna_expression.md):** `enum`; required. Format of the data files. Allowed values: CSV; TSV; TXT.
- **[simple_germline_variation](entities/simple_germline_variation.md):** `enum`; required. Format of the data files. Allowed values: VCF.
- **[slide_image](entities/slide_image.md):** `string`; required. Format of the data files.
- **[structural_variation](entities/structural_variation.md):** `enum`; required. Format of the data files. Allowed values: BAM; BEDPE; CSV; FASTA; GVF; JSON; … (+3 more).
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; required. Format of the data files. Allowed values: BAM; BED; CRAM.
- **[submitted_copy_number](entities/submitted_copy_number.md):** `string`; required. Format of the data files.
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `enum`; required. Format of the data files. Allowed values: MAF; TSV; VCF; XML.
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `enum`; required. Format of the data files. Allowed values: CEL.
- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; required. Format of the data files. Allowed values: IDAT.
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `string`; required. Format of the data files.
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `enum`; required. Format of the data files. Allowed values: TXT.
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; required. Format of the data files. Allowed values: BAM; FASTQ.

### `data_type`

- **[aligned_reads](entities/aligned_reads.md):** `enum`; required. Specific content type of the data file. Allowed values: Aligned Reads.
- **[aligned_reads_index](entities/aligned_reads_index.md):** `enum`; required. Specific content type of the data file. Allowed values: Aligned Reads Index.
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `enum`; required. Specific content type of the data file. Allowed values: Intermediate Analysis Archive.
- **[copy_number_estimate](entities/copy_number_estimate.md):** `enum`; required. Specific content type of the data file. Allowed values: Gene Level Copy Number; Gene Level Copy Number Scores; Cohort Level Copy Number Scores.
- **[copy_number_segment](entities/copy_number_segment.md):** `enum`; required. Specific content type of the data file. Allowed values: Allele-specific Copy Number Segment; Copy Number Segment; Masked Copy Number Segment.
- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. The nature or genre of the resource. Recommended best practice is to use a controlled vocabulary such as the DCMI Type Vocabulary [DCMITYPE]. To describe the file format, physical medium, or dimensions of the resource, use the Format element.
- **[experimental_metadata](entities/experimental_metadata.md):** `enum`; required. Specific content type of the data file. Allowed values: Experimental Metadata.
- **[gene_expression](entities/gene_expression.md):** `enum`; required. Specific content type of the data file. Allowed values: Exon Expression Quantification; Gene Expression Quantification; Isoform Expression Quantification; Splice Junction Quantification.
- **[mirna_expression](entities/mirna_expression.md):** `enum`; required. Specific content type of the data file. Allowed values: Isoform Expression Quantification; miRNA Expression Quantification; Supplementary Files.
- **[simple_germline_variation](entities/simple_germline_variation.md):** `enum`; required. Specific content type of the data file. Allowed values: Simple Germline Variation.
- **[slide_image](entities/slide_image.md):** `enum`; required. Specific content type of the data file. Allowed values: image; Single Cell Image; Raw IMC Data; Single Channel IMC Image; Antibody Panel Added.
- **[structural_variation](entities/structural_variation.md):** `enum`; required. Specific content type of the data file. Allowed values: Structural Alteration; Structural Rearrangement; Transcript Fusion.
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; required. Specific content type of the data file. Allowed values: Aligned Reads; Alignment Coordinates.
- **[submitted_copy_number](entities/submitted_copy_number.md):** `string`; required. Specific content type of the data file.
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `enum`; required. Specific content type of the data file. Allowed values: FoundationOne Report; GENIE Report; Raw CGI Variant.
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `enum`; required. Specific content type of the data file. Allowed values: Raw Intensities.
- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; required. Specific content type of the data file. Allowed values: Methylation Intensity Values.
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `string`; required. Specific content type of the data file.
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `enum`; required. Specific content type of the data file. Allowed values: Copy Number Estimate.
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; required. Specific content type of the data file. Allowed values: Unaligned Reads.

### `date`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `datetime`; optional/not marked required

### `date_collected`

- **[project](entities/project.md):** `string`; optional/not marked required. The date or date range in which the project data was collected.

### `days_180_aki`

- **[case](entities/case.md):** `enum`; optional/not marked required. 180 days aki. Allowed values: Yes; No; Unknown.

### `days_180_survival`

- **[case](entities/case.md):** `enum`; optional/not marked required. 180 days survival. Allowed values: alive; dead; Unknown.

### `days_90_aki`

- **[case](entities/case.md):** `enum`; optional/not marked required. 90 days aki. Allowed values: Yes; No; Unknown.

### `days_90_survival`

- **[case](entities/case.md):** `enum`; optional/not marked required. 90 days survival. Allowed values: alive; dead; Unknown.

### `days_to_aki`

- **[case](entities/case.md):** `number`; optional/not marked required. How many days from index date to aki.

### `days_to_birth`

- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated negative number of days.

### `days_to_collection`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. The number of days from the index date to the date a sample was collected for a specific study or project

### `days_to_consent`

- **[case](entities/case.md):** `number`; optional/not marked required. Number of days between the date used for index and the date the subject consent was obtained for participation in the study.

### `days_to_death`

- **[case](entities/case.md):** `number`; optional/not marked required. How many days from index date to death.
- **[demographic](entities/demographic.md):** `number`; optional/not marked required. Number of days between the date used for index and the date from a person's date of death represented as a calculated number of days.
- **[diagnosis](entities/diagnosis.md):** `number`; optional/not marked required. Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days.

### `days_to_follow_up`

- **[follow_up](entities/follow_up.md):** `number / null`; required. Number of days between the date used for index and the date of the patient's last follow-up appointment or contact.

### `days_to_hiv_diagnosis`

- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. Time interval from the date of the initial pathologic diagnosis to the date of human immunodeficiency diagnosis, represented as a calculated number of days.

### `days_to_last_follow_up`

- **[diagnosis](entities/diagnosis.md):** `number / null`; required. Time interval from the date of last follow up to the date of initial pathologic diagnosis, represented as a calculated number of days.

### `days_to_last_known_disease_status`

- **[diagnosis](entities/diagnosis.md):** `number / null`; required. Time interval from the date of last follow up to the date of initial pathologic diagnosis, represented as a calculated number of days.

### `days_to_new_event`

- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. Time interval from the date of new tumor event including progression, recurrence and new primary malignacies to the date of initial pathologic diagnosis, represented as a calculated number of days.

### `days_to_receive_sample`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. The number of days from the index date to the date a sample was received by the site

### `days_to_recurrence`

- **[diagnosis](entities/diagnosis.md):** `number / null`; required. Time interval from the date of new tumor event including progression, recurrence and new primary malignancies to the date of initial pathologic diagnosis, represented as a calculated number of days.

### `days_to_sequencing`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. NEW: Number of days between the date used for index and the date the read group was sequenced.

### `days_to_test`

- **[audit](entities/audit.md):** `number / null`; optional/not marked required. Number of days between the date used for index and the date of the laboratory test.
- **[molecular_test](entities/molecular_test.md):** `number`; optional/not marked required. Number of days between the date used for index and the date of the laboratory test.

### `days_to_treatment`

- **[treatment](entities/treatment.md):** `number`; optional/not marked required. Number of days from date of initial pathologic diagnosis that treatment began.

### `days_to_treatment_end`

- **[treatment](entities/treatment.md):** `number`; optional/not marked required. Time interval from the date of the initial pathologic diagnosis to the date of treatment end, represented as a calculated number of days.

### `days_to_treatment_start`

- **[treatment](entities/treatment.md):** `number`; optional/not marked required. Time interval from the date of the initial pathologic diagnosis to the start of treatment, represented as a calculated number of days.

### `dbgap_accession_number`

- **[program](entities/program.md):** `string`; required. The dbgap accession number provided for the program.
- **[project](entities/project.md):** `string`; required. The dbgap accession number provided for the project.

### `death_related_to`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. Text term to identify common conditions to which the death is related. Allowed values: Spontaneous Bacterial Peritonitis; Sepsis; Esophageal Variceal Bleed; Gastric Variceal Bleeding; Liver Disease - Other; Unknown; … (+1 more).

### `demographics`

- **[follow_up](entities/follow_up.md):** `to_one`; optional/not marked required; relationship target [demographic](entities/demographic.md)

### `description`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. An account of the resource. Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.

### `description_of_lab`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Description of the lab.

### `diagnoses`

- **[clinical_test](entities/clinical_test.md):** `to_many`; optional/not marked required; relationship target [diagnosis](entities/diagnosis.md)
- **[sample](entities/sample.md):** `to_one`; optional/not marked required; relationship target [diagnosis](entities/diagnosis.md)
- **[treatment](entities/treatment.md):** `to_one`; optional/not marked required; relationship target [diagnosis](entities/diagnosis.md)

### `dlco_ref_predictive_percent`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. The value, as a percentage of predicted lung volume, measuring the amount of carbon monoxide detected in a patient's lungs.

### `doi`

- **[publication](entities/publication.md):** `string`; optional/not marked required

### `duodenum_ulcer_bleed`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there were signs of recent bleeding from the duodenal ulcer or erosion. Allowed values: Yes; No; Not Reported; Missing.

### `duodenum_ulcer_size`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the duodenal ulcer or erosion size. Allowed values: Small; Medium; Large; Not Reported; Missing.

### `education`

- **[demographic](entities/demographic.md):** `string`; optional/not marked required. Text term to identify the highest level of education complete for the patient.

### `encoding`

- **[read_group_qc](entities/read_group_qc.md):** `string`; required. Version of ASCII encoding of quality values found in the file.

### `endoscopy`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if an endoscopy was done as a standard of care procedure. Allowed values: Yes; No.

### `endoscopy_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of endoscopy done as a standard of care procedure. In (YYYY-MM-DD) format.

### `endoscopy_ulcer_present`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe ulcers or erosions present on endoscopy. Allowed values: Esophageal; Stomach; Duodenum; Esophageal and Stomach; Esophageal and Duodenum; Stomach and Duodenum; … (+2 more).

### `endoscopy_varices_present`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe if varices were present on endoscopy. Allowed values: Esophageal; Gastric; Esophageal and Gastric; None Present.

### `er_localization`

- **[slide_count](entities/slide_count.md):** `enum`; optional/not marked required. Cellular localization of the endoplasmic reticulum as determined by staining. Allowed values: Nuclear; Cytoplasmic; Both; None; Not Determined.

### `esophageal_ulcer_bleed`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there were signs of recent bleeding from the esophageal ulcer or erosion. Allowed values: Yes; No; Not Reported; Missing.

### `esophageal_ulcer_size`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the esophageal ulcer or erosion size. Allowed values: Small; Medium; Large; Not Reported; Missing.

### `esophageal_varices_bleed`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there were signs of recent bleeding from the esophageal varices. Allowed values: Yes; No; Not Reported; Missing.

### `esophageal_varices_size`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the size of esophageal varices found during endoscopy. Allowed values: Small; Medium; Large; Not Reported; Missing.

### `estrogen_receptor_percent_positive_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Classification to represent ER Positive results expressed as a percentage value. Allowed values: <1%; 1-10%; 11-20%; 21-30%; 31-40%; 41-50%; … (+5 more).

### `estrogen_receptor_result_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Text term to represent the overall result of Estrogen Receptor (ER) testing. Allowed values: Negative; Not Performed; Positive; Unknown.

### `ethnicity`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau. Allowed values: hispanic or latino; not hispanic or latino; Unknown; not reported; not allowed to collect; None.

### `event_type`

- **[follow_up](entities/follow_up.md):** `string / null`; optional/not marked required. Event type for a follow up visit.

### `experiment_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Submitter-defined name for the experiment.

### `experimental_description`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. A brief description of the experiment being performed.

### `experimental_intent`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. Summary of the goals the experiment is designed to discover.

### `experimental_strategy`

- **[aligned_reads](entities/aligned_reads.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: WGS; WXS; Low Pass WGS; Validation; RNA-Seq; miRNA-Seq; … (+1 more).
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: WGS.
- **[copy_number_estimate](entities/copy_number_estimate.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: Genotyping Array; Targeted Sequencing; WGS; WXS.
- **[copy_number_segment](entities/copy_number_segment.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: Genotyping Array; Targeted Sequencing; WGS; WXS.
- **[gene_expression](entities/gene_expression.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: m6A MeRIP-Seq; RNA-Seq; scRNA-Seq; Total RNA-Seq.
- **[mirna_expression](entities/mirna_expression.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: miRNA-Seq.
- **[simple_germline_variation](entities/simple_germline_variation.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: WGS; WXS; Low Pass WGS; Validation.
- **[slide_image](entities/slide_image.md):** `enum`; optional/not marked required. Classification of the slide type with respect to its experimental use. Allowed values: Diagnostic Slide; Tissue Slide.
- **[structural_variation](entities/structural_variation.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: WGS; WXS; Low Pass WGS; Validation; RNA-Seq; miRNA-Seq; … (+3 more).
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: WGS; WXS; Low Pass WGS; Validation; RNA-Seq; miRNA-Seq; … (+10 more).
- **[submitted_copy_number](entities/submitted_copy_number.md):** `string`; required. The sequencing strategy used to generate the data file.
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: ATAC-Seq; Bisulfite-Seq; ChIP-Seq; miRNA-Seq; RNA-Seq; Targeted Sequencing; … (+2 more).
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: Genotyping Array.
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `string`; required. The sequencing strategy used to generate the data file.
- **[submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md):** `enum`; required. The sequencing strategy used to generate the data file. Allowed values: Genotyping Array.
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; required. UPDATED: The sequencing strategy used to generate the data file. Allowed values: WGS; WXS; Low Pass WGS; Validation; RNA-Seq; miRNA-Seq; … (+10 more).

### `experiments`

- **[experimental_metadata](entities/experimental_metadata.md):** `to_one`; optional/not marked required; relationship target [experiment](entities/experiment.md)

### `fastq_name`

- **[read_group_qc](entities/read_group_qc.md):** `string`; optional/not marked required. The name (or part of a name) of a file (of any type).

### `fev1_fvc_post_bronch_percent`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. Percentage value to represent result of Forced Expiratory Volume in 1 second (FEV1) divided by the Forced Vital Capacity (FVC) post-bronchodilator.

### `fev1_fvc_pre_bronch_percent`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. Percentage value to represent result of Forced Expiratory Volume in 1 second (FEV1) divided by the Forced Vital Capacity (FVC) pre-bronchodilator.

### `fev1_ref_post_bronch_percent`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. The percentage comparison to a normal value reference range of the volume of air that a patient can forcibly exhale from the lungs in one second post-bronchodilator.

### `fev1_ref_pre_bronch_percent`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. The percentage comparison to a normal value reference range of the volume of air that a patient can forcibly exhale from the lungs in one second pre-bronchodilator.

### `fibro_capmed`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Fibroscan median CAP score in decibels per meter (dB/m).

### `fibro_e`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Fibroscan fibrosis result in kilopascals (kPa).

### `fibro_iqr`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Fibroscan CAP interquartile range.

### `fibro_probe`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the probe used during the fibroscan. Allowed values: M; XL; Not Reported.

### `fibro_total_number`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Number describing the total measurements used in the fibroscan.

### `fibroscan`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if a fibroscan was done as a standard care of procedure. Allowed values: Yes; No.

### `fibroscan_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of fibroscan done as a standard of care procedure. In (YYYY-MM-DD) format.

### `figo_stage`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The extent of a cervical or endometrial cancer within the body, especially whether the disease has spread from the original site to other parts of the body, as described by the International Federation of Gynecology and Obstetrics (FIGO) stages. Allowed values: Stage 0; Stage I; Stage IA; Stage IA1; Stage IA2; Stage IB; … (+20 more).

### `firbro_e_iqr`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Fibroscan fibrosis interquartile range.

### `firbro_valid_number`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Number of valid measurements in the fibroscan.

### `flow_cell_barcode`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Flow cell barcode. Wrong or missing information may affect analysis results.

### `follow_ups`

- **[aliquot](entities/aliquot.md):** `to_one`; required; relationship target [follow_up](entities/follow_up.md)
- **[clinical_test](entities/clinical_test.md):** `to_one`; optional/not marked required; relationship target [follow_up](entities/follow_up.md)
- **[diagnosis](entities/diagnosis.md):** `to_one`; optional/not marked required; relationship target [follow_up](entities/follow_up.md)
- **[molecular_test](entities/molecular_test.md):** `to_one`; required; relationship target [follow_up](entities/follow_up.md)
- **[sample](entities/sample.md):** `to_one`; required; relationship target [follow_up](entities/follow_up.md)
- **[treatment](entities/treatment.md):** `to_one`; optional/not marked required; relationship target [follow_up](entities/follow_up.md)

### `format`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. The file format, physical medium, or dimensions of the resource. Examples of dimensions include size and duration. Recommended best practice is to use a controlled vocabulary such as the list of Internet Media Types [MIME] (http://www.iana.org/assignments/media-types/).

### `fragment_maximum_length`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. NEW: Maximum length of the sequenced fragments (e.g., as predicted by Agilent Bioanalyzer).

### `fragment_mean_length`

- **[read_group](entities/read_group.md):** `number`; optional/not marked required. NEW: Mean length of the sequenced fragments (e.g., as predicted by Agilent Bioanalyzer).

### `fragment_minimum_length`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. NEW: Minimum length of the sequenced fragments (e.g., as predicted by Agilent Bioanalyzer).

### `fragment_standard_deviation_length`

- **[read_group](entities/read_group.md):** `number`; optional/not marked required. NEW: Standard deviation of the sequenced fragments length (e.g., as predicted by Agilent Bioanalyzer).

### `fragmentation_enzyme`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. NEW: The restriction enzyme used for nucleotide fragmentation. Allowed values: MboI; Unknown; Not Applicable.

### `frame_identifier`

- **[slide_count](entities/slide_count.md):** `string`; optional/not marked required. Name, number, or other identifier given to the frame of the slide from which this image was taken.
- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. Name, number, or other identifier given to the frame of the slide from which this image was taken.

### `gastric_ulcer_bleed`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there were signs of recent bleeding from the gastric ulcer or erosion. Allowed values: Yes; No; Not Reported; Missing.

### `gastric_ulcer_size`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the gastric ulcer or erosion size. Allowed values: Small; Medium; Large; Not Reported; Missing.

### `gastric_varices_bleed`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there were signs of recent bleeding from the gastric varices. Allowed values: Yes; No; Not Reported; Missing.

### `gastric_varices_size`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the size of gastric varices found during endoscopy. Allowed values: Small; Medium; Large; Not Reported; Missing.

### `gender`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. Text designations that identify gender. Gender is described as the assemblage of properties that distinguish people on the basis of their societal roles. [Explanatory Comment 1: Identification of gender is based upon self-report and may come from a form, questionnaire, interview, etc.] Allowed values: female; male; unknown; unspecified; not reported; None.

### `gene_symbol`

- **[molecular_test](entities/molecular_test.md):** `enum`; optional/not marked required. The text term used to describe a gene targeted or included in molecular analysis. For rearrangements, this is shold be used to represent the reference gene. Allowed values: A1CF; ABI1; ABL1; ABL2; ACKR3; ACSL3; … (+716 more).

### `genomic_profile_harmonization_workflows`

- **[copy_number_estimate](entities/copy_number_estimate.md):** `to_one`; optional/not marked required; relationship target [genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md)
- **[copy_number_segment](entities/copy_number_segment.md):** `to_one`; optional/not marked required; relationship target [genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md)
- **[structural_variation](entities/structural_variation.md):** `to_one`; optional/not marked required; relationship target [genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md)

### `germline_mutation_calling_workflows`

- **[simple_germline_variation](entities/simple_germline_variation.md):** `to_one`; optional/not marked required; relationship target [germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md)

### `height`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. The height of the patient in centimeters.
- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. The height of the patient in centimeters.

### `hep_carcinoma`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if subject has been diagnosed with Hepatocellular Carcinoma (HCC). Allowed values: Yes; No; Not Reported; Missing.

### `hep_enceph`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if subject has been diagnosed with Spontaneous Hepatic Encephalopathy (grade 2 or higher). Allowed values: Yes; No; Not Reported; Missing.

### `hep_enceph_diagnosis_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of most recent Spontaneous Hepatic Encephalopathy diagnosis (grade 2 or higher). In (YYYY-MM-DD) format.

### `hepcar_diagnosis_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of most recent diagnosis of Hepatocellular Carcinoma (HCC). In (YYYY-MM-DD) format.

### `her2_erbb2_percent_positive_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Classification to represent the number of positive HER2/ERBB2 cells in a specimen or sample. Allowed values: <1%; 1-10%; 11-20%; 21-30%; 31-40%; 41-50%; … (+5 more).

### `her2_erbb2_result_fish`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. the type of outcome for HER2 as determined by an in situ hybridization (ISH) assay. Allowed values: Negative; Not Performed; Positive; Unknown.

### `her2_erbb2_result_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Text term to signify the result of the medical procedure that involves testing a sample of blood or tissue for HER2 by histochemical localization of immunoreactive substances using labeled antibodies as reagents. Allowed values: Negative; Not Performed; Positive; Unknown.

### `hiv_positive`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to signify whether a physician has diagnosed HIV infection in a patient. Allowed values: Yes; No; Unknown.

### `hospitalized_alc_hep`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the patient was hospitalized due to alcoholic hepatitis in the past year. Allowed values: Yes; No; Not Reported.

### `hospitalized_alc_hep_times`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. The number of times the patient was hospitalized during the past year due to alcoholic hepatitis.

### `hospitalized_at_enrollment`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the patient was hospitalized at the time of enrollment. Allowed values: Yes; No; Not Reported.

### `hpv_positive_type`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text classification to represent the strain or type of human papillomavirus identified in an individual. Allowed values: HPV 16; HPV 18; Other HPV type(s); Unknown.

### `hpv_status`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The findings of the oncogenic HPV. Allowed values: Negative; Positive; Unknown.

### `id`

- **[acknowledgement](entities/acknowledgement.md):** `UUID`; optional/not marked required
- **[aliquot](entities/aliquot.md):** `UUID`; optional/not marked required
- **[audit](entities/audit.md):** `UUID`; optional/not marked required
- **[case](entities/case.md):** `UUID`; optional/not marked required
- **[clinical_test](entities/clinical_test.md):** `UUID`; optional/not marked required
- **[demographic](entities/demographic.md):** `UUID`; optional/not marked required
- **[diagnosis](entities/diagnosis.md):** `UUID`; optional/not marked required
- **[experiment](entities/experiment.md):** `UUID`; optional/not marked required
- **[exposure](entities/exposure.md):** `UUID`; optional/not marked required
- **[family_history](entities/family_history.md):** `UUID`; optional/not marked required
- **[follow_up](entities/follow_up.md):** `UUID`; optional/not marked required
- **[keyword](entities/keyword.md):** `UUID`; optional/not marked required
- **[lab](entities/lab.md):** `UUID`; optional/not marked required
- **[molecular_test](entities/molecular_test.md):** `UUID`; optional/not marked required
- **[program](entities/program.md):** `UUID`; optional/not marked required
- **[project](entities/project.md):** `UUID`; optional/not marked required. UUID for the project.
- **[publication](entities/publication.md):** `UUID`; optional/not marked required
- **[read_group](entities/read_group.md):** `UUID`; optional/not marked required
- **[sample](entities/sample.md):** `UUID`; optional/not marked required
- **[slide](entities/slide.md):** `UUID`; optional/not marked required
- **[slide_count](entities/slide_count.md):** `UUID`; optional/not marked required
- **[study](entities/study.md):** `UUID`; optional/not marked required
- **[treatment](entities/treatment.md):** `UUID`; optional/not marked required

### `includes_spike_ins`

- **[read_group](entities/read_group.md):** `boolean`; optional/not marked required. Spike-in

### `indels_identified`

- **[experiment](entities/experiment.md):** `boolean`; optional/not marked required. Are indels identified in this experiment?

### `index_date`

- **[case](entities/case.md):** `enum`; optional/not marked required. The text term used to describe the reference or anchor date used when for date obfuscation, where a single date is obscurred by creating one or more date ranges in relation to this date. Allowed values: Diagnosis; First Patient Visit; First Treatment; Intitial Genomic Sequencing; Recurrence; Sample Procurement; … (+1 more).

### `inf_cnst_sign_dt`

- **[case](entities/case.md):** `string`; optional/not marked required. The date the informed consent was signed.

### `infection_screen_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of the infection screen. In (YYYY-MM-DD) format.

### `infection_screen_done`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if an infection screen was done. Allowed values: Yes; No.

### `instrument_model`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. Specific model of sequencing instrument used. Allowed values: 454 GS FLX Titanium; AB SOLiD 4; AB SOLiD 2; AB SOLiD 3; Complete Genomics; Illumina HiSeq X Ten; … (+17 more).

### `intended_release_date`

- **[project](entities/project.md):** `string`; optional/not marked required. Tracks a Project's intended release date.

### `investigator_affiliation`

- **[project](entities/project.md):** `string`; optional/not marked required. The investigator's affiliation with respect to a research institution.

### `investigator_name`

- **[project](entities/project.md):** `string`; optional/not marked required. Name of the principal investigator for the project.

### `is_paired_end`

- **[read_group](entities/read_group.md):** `boolean`; optional/not marked required. Are the reads paired end?

### `keyword_name`

- **[keyword](entities/keyword.md):** `string`; optional/not marked required. The name of the keyword.
- **[lab](entities/lab.md):** `string`; optional/not marked required. The name of the keyword.

### `kmer_content`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `laboratory_test`

- **[molecular_test](entities/molecular_test.md):** `enum`; optional/not marked required. The text term used to describe the medical testing used to diagnose, treat or further understand a patient's disease. Allowed values: 5-Hydroxyindoleacetic Acid; Absolute Neutrophil; Albumin; Alkaline Phosphatase; Alpha Fetoprotein; ALT; … (+89 more).

### `labs`

- **[aliquot](entities/aliquot.md):** `to_one`; optional/not marked required; relationship target [lab](entities/lab.md)
- **[molecular_test](entities/molecular_test.md):** `to_one`; optional/not marked required; relationship target [lab](entities/lab.md)

### `lane_number`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. NEW: The basic machine unit for sequencing. For Illumina machines, this reflects the physical lane number. Wrong or missing information may affect analysis results.

### `language`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. A language of the resource. Recommended best practice is to use a controlled vocabulary such as RFC 4646 (http://www.ietf.org/rfc/rfc4646.txt).

### `last_known_disease_status`

- **[diagnosis](entities/diagnosis.md):** `enum`; required. Text term that describes the last known state or condition of an individual's neoplasm. Allowed values: Distant met recurrence/progression; Loco-regional recurrence/progression; Biochemical evidence of disease without structural correlate; Tumor free; Unknown tumor status; With tumor; … (+2 more).

### `laterality`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. For tumors in paired organs, designates the side on which the cancer originates. Allowed values: Bilateral; Left; Right; Unknown.

### `ldh_level_at_diagnosis`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. The 2 decimal place numeric laboratory value measured, assigned or computed related to the assessment of lactate dehydrogenase in a specimen.
- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. The 2 decimal place numeric laboratory value measured, assigned or computed related to the assessment of lactate dehydrogenase in a specimen.

### `ldh_normal_range_upper`

- **[clinical_test](entities/clinical_test.md):** `number`; optional/not marked required. The top value of the range of statistical characteristics that are supposed to represent accepted standard, non-pathological pattern for lactate dehydrogenase (units not specified).
- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. The top value of the range of statistical characteristics that are supposed to represent accepted standard, non-pathological pattern for lactate dehydrogenase (units not specified).

### `library_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of the library.

### `library_preparation_kit_catalog_number`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Catalog of library preparation kit.

### `library_preparation_kit_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of library preparation kit.

### `library_preparation_kit_vendor`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Vendor of library preparation kit.

### `library_preparation_kit_version`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Version of library preparation kit.

### `library_selection`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. Library selection method. Allowed values: Hybrid_Selection; PCR; Affinity_Enrichment; Poly-T_Enrichment; RNA_Depletion; Other; … (+3 more).

### `library_strand`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. Library stranded-ness. Allowed values: Unstranded; First_Stranded; Second_Stranded; Not Applicable.

### `library_strategy`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. Library strategy. Allowed values: WGS; WXS; RNA-Seq; ChIP-Seq; miRNA-Seq; Bisulfite-Seq; … (+9 more).

### `lille_score`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for Lille score.

### `liver_abdomen_imaging`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator use to describe if there were any other imaging test done on the liver or abdomen. Allowed values: Yes; No.

### `liver_imaging_type`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the other type of image done to the liver or abdomen. Allowed values: Ultrasound; CT; MRI; Other type.

### `liver_score_collected`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if liver disease scores were collected. Allowed values: Yes; No.

### `liver_score_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date liver disease scores were obtained. In (YYYY-MM-DD) format.

### `liver_transplant`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if a liver transplant was performed for patient. Allowed values: Yes; No; Not Reported; Missing.

### `liver_transplant_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of liver transplant. In (YYYY-MM-DD) format.

### `lymph_nodes_positive`

- **[diagnosis](entities/diagnosis.md):** `integer`; optional/not marked required. The number of lymph nodes involved with disease as determined by pathologic examination.

### `lymphatic_invasion_present`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. A yes/no indicator to ask if small or thin-walled vessel invasion is present, indicating lymphatic involvement Allowed values: Yes; No; Unknown.

### `maddreys_score`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for Maddrey's Discriminant Function Score.

### `marital`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. What is your current marital status? Allowed values: Divorced; Domestic Partnership; Married; Never Married; Separated; Widowed; … (+3 more).

### `marker_panel_description`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. Brief description of the marker panel used in this experiment.

### `medical_info_collected`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if medical information was collected at a visit. Allowed values: Yes; No.

### `meld_score`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for MELD score.

### `methanol_added`

- **[slide](entities/slide.md):** `boolean`; optional/not marked required. True/False indicator for if methanol was used in the slide preparation process.

### `method_of_diagnosis`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The method used to initially the patient's diagnosis. Allowed values: Autopsy; Biopsy; Blood Draw; Bone Marrow Aspirate; Core Biopsy; Cytology; … (+13 more).

### `microsatellite_instability_abnormal`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. The yes/no indicator to signify the status of a tumor for microsatellite instability. Allowed values: Yes; No; Unknown.

### `mirna_expression_calling_workflows`

- **[mirna_expression](entities/mirna_expression.md):** `to_one`; optional/not marked required; relationship target [mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md)

### `molecular_analysis_method`

- **[molecular_test](entities/molecular_test.md):** `enum`; optional/not marked required. The text term used to describe the method used for molecular analysis. Allowed values: Comparative Genomic Hybridization; Cytogenetics, NOS; FISH; Flow Cytometry; IHC; Immunofluorescence; … (+16 more).

### `morphology`

- **[diagnosis](entities/diagnosis.md):** `string`; required. The third edition of the International Classification of Diseases for Oncology, published in 2000 used principally in tumor and cancer registries for coding the site (topography) and the histology (morphology) of neoplasms. The study of the structure of the cells and their arrangement to constitute tissues and, finally, the association among these to form organs. In pathology, the microscopic process of identifying normal and abnormal morphologic characteristics in tissues, by employing various cytochemical and immunocytochemical stains. A system of numbered categories for representation of data.

### `mri_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of MRI. In (YYYY-MM-DD) format.

### `mri_finding`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Description of the overall findings/impressions of the MRI.

### `mri_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the results of the CT. Allowed values: Normal; Abnormal; Missing.

### `mri_sig`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the MRI results are clinically significant. Allowed values: Yes; No; Missing.

### `multiplex_barcode`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. NEW: The barcode/index sequence used. Wrong or missing information may affect analysis results.

### `name`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Name of the lab (e.g. IU).
- **[program](entities/program.md):** `string`; required. Full name/title of the program.
- **[project](entities/project.md):** `string`; required. Display name/brief description for the project.

### `name_of_institute`

- **[lab](entities/lab.md):** `string / null`; required. Name of institute.

### `namespace`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Domain name of the lab (e.g. iu.edu).

### `new_event_anatomic_site`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to specify the anatomic location of the return of tumor after treatment. Allowed values: Abdomen; Adrenal; Anus; Appendix; Ascites/Peritoneum; Axillary lymph nodes; … (+96 more).

### `new_event_type`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to identify a new tumor event. Allowed values: Biochemical Evidence of Disease; Both Locoregional and Distant Metastasis; Distant Metastasis; Extrahepatic Recurrence; Intrahepatic Recurrence; Intrapleural Progression; … (+15 more).

### `note`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Note.

### `number_expect_cells`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. NEW: Expected number of recovered cells in droplet-based single-cell libraries.

### `number_experimental_group`

- **[experiment](entities/experiment.md):** `integer`; optional/not marked required. The number denoting this experiment's place within the group within the whole.

### `number_nucleated_cells`

- **[slide](entities/slide.md):** `integer`; optional/not marked required. The total number of nucleated cells identified on the slide.

### `number_proliferating_cells`

- **[slide](entities/slide.md):** `integer`; optional/not marked required. Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s).

### `number_samples_per_experimental_group`

- **[experiment](entities/experiment.md):** `integer`; optional/not marked required. The number of samples contained within this experimental group.

### `other_imaging_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of other imaging. In (YYYY-MM-DD) format.

### `other_imaging_finding`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Description of the overall findings/impressions of the other type of image.

### `other_imaging_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the other type of imaging result. Allowed values: Normal; Abnormal; Missing.

### `other_imaging_sig`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the other type of imaging result is clinically significant. Allowed values: Yes; No; Missing.

### `other_imaging_type`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The text used to describe the other type of imaging.

### `overrepresented_sequences`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `pack_years_smoked`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20.

### `panel_used`

- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. Name or other identifier given to the panel used during an IMC run.

### `per_base_n_content`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `per_base_sequence_content`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `per_base_sequence_quality`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `per_sequence_gc_content`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `per_sequence_quality_score`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `per_tile_sequence_quality`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `percent_aligned`

- **[read_group_qc](entities/read_group_qc.md):** `integer`; optional/not marked required. The percent of reads with at least one reported alignment.

### `percent_eosinophil_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of infiltration by eosinophils in a tumor sample or specimen.

### `percent_gc_content`

- **[read_group_qc](entities/read_group_qc.md):** `integer`; required. The overall %GC of all bases in all sequences.

### `percent_granulocyte_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of infiltration by granulocytes in a tumor sample or specimen.

### `percent_inflam_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent local response to cellular injury, marked by capillary dilatation, edema and leukocyte infiltration; clinically, inflammation is manifest by reddness, heat, pain, swelling and loss of function, with the need to heal damaged tissue.

### `percent_lymphocyte_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of infiltration by lymphocytes in a solid tissue normal sample or specimen.

### `percent_monocyte_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of monocyte infiltration in a sample or specimen.

### `percent_necrosis`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of cell death in a malignant tumor sample or specimen.

### `percent_neutrophil_infiltration`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of infiltration by neutrophils in a tumor sample or specimen.

### `percent_normal_cells`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of normal cell content in a malignant tumor sample or specimen.

### `percent_stromal_cells`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of reactive cells that are present in a malignant tumor sample or specimen but are not malignant such as fibroblasts, vascular structures, etc.

### `percent_tumor_cells`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value that represents the percentage of infiltration by granulocytes in a sample.

### `percent_tumor_nuclei`

- **[slide](entities/slide.md):** `number`; optional/not marked required. Numeric value to represent the percentage of tumor nuclei in a malignant neoplasm sample or specimen.

### `perineural_invasion_present`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. a yes/no indicator to ask if perineural invasion or infiltration of tumor or cancer is present. Allowed values: Yes; No; Unknown.

### `PI_email`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. PI' email.

### `PI_name`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. PI’s name.

### `platform`

- **[aligned_reads](entities/aligned_reads.md):** `properties/platform`; required
- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `enum`; required. Name of the platform used to obtain data. Allowed values: Illumina.
- **[copy_number_estimate](entities/copy_number_estimate.md):** `enum`; required. Name of the platform used to obtain data. Allowed values: Affymetrix SNP 6.0; Illumina; Ion Torrent.
- **[copy_number_segment](entities/copy_number_segment.md):** `enum`; required. Name of the platform used to obtain data. Allowed values: Affymetrix SNP 6.0; Illumina.
- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. Name of the platform used to obtain data. Allowed values: Illumina; SOLiD; LS454; Ion Torrent; Complete Genomics; PacBio; … (+1 more).
- **[submitted_genotyping_array](entities/submitted_genotyping_array.md):** `enum`; required. Name of the platform used to obtain data. Allowed values: Affymetrix SNP 6.0.

### `pmid`

- **[publication](entities/publication.md):** `string`; optional/not marked required

### `portal_hypertensive_gastropathy`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe portal hypertensive gastropathy found on endoscopy. Allowed values: Yes, Mild; Yes, Moderate; Yes, Severe; Yes, Unknown severity; None; Not Reported; … (+1 more).

### `preservation_method`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents the method used to preserve the sample Allowed values: Frozen; Unknown; Not Reported.

### `primary_diagnosis`

- **[diagnosis](entities/diagnosis.md):** `string`; required. Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.

### `prior_malignancy`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence. Allowed values: yes; no; unknown; not reported; Not Allowed To Collect.

### `prior_treatment`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. A yes/no/unknown/not applicable indicator related to the administration of therapeutic agents received before the body specimen was collected. Allowed values: Yes; No; Unknown; Not Reported; Not Allowed To Collect.

### `proc_internal`

- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; optional/not marked required. NEW: Internal data processing flag. Allowed values: dna-seq skip.

### `progesterone_receptor_percent_positive_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Classification to represent Progesterone Receptor Positive results expressed as a percentage value. Allowed values: <1%; 1-10%; 11-20%; 21-30%; 31-40%; 41-50%; … (+5 more).

### `progesterone_receptor_result_ihc`

- **[clinical_test](entities/clinical_test.md):** `enum`; optional/not marked required. Text term to represent the overall result of Progresterone Receptor (PR) testing. Allowed values: Negative; Not Performed; Positive; Unknown.

### `programs`

- **[project](entities/project.md):** `to_one`; required; relationship target [program](entities/program.md). Indicates that the project is logically part of the indicated project.

### `progression_or_recurrence`

- **[diagnosis](entities/diagnosis.md):** `enum`; required. Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment. Allowed values: yes; no; unknown; not reported; Not Allowed To Collect.

### `project_id`

- **[acknowledgement](entities/acknowledgement.md):** `string`; optional/not marked required
- **[aliquot](entities/aliquot.md):** `project_id`; optional/not marked required
- **[audit](entities/audit.md):** `project_id`; optional/not marked required
- **[case](entities/case.md):** `project_id`; optional/not marked required
- **[clinical_test](entities/clinical_test.md):** `project_id`; optional/not marked required
- **[demographic](entities/demographic.md):** `project_id`; optional/not marked required
- **[diagnosis](entities/diagnosis.md):** `project_id`; optional/not marked required
- **[experiment](entities/experiment.md):** `project_id`; optional/not marked required
- **[exposure](entities/exposure.md):** `project_id`; optional/not marked required
- **[family_history](entities/family_history.md):** `project_id`; optional/not marked required
- **[follow_up](entities/follow_up.md):** `project_id`; optional/not marked required
- **[keyword](entities/keyword.md):** `string`; optional/not marked required
- **[lab](entities/lab.md):** `string`; optional/not marked required
- **[molecular_test](entities/molecular_test.md):** `project_id`; optional/not marked required
- **[publication](entities/publication.md):** `string`; optional/not marked required
- **[read_group](entities/read_group.md):** `project_id`; optional/not marked required
- **[sample](entities/sample.md):** `string`; optional/not marked required
- **[slide](entities/slide.md):** `project_id`; optional/not marked required
- **[slide_count](entities/slide_count.md):** `string`; optional/not marked required
- **[study](entities/study.md):** `project_id`; optional/not marked required
- **[treatment](entities/treatment.md):** `project_id`; optional/not marked required

### `projects`

- **[acknowledgement](entities/acknowledgement.md):** `to_many_project`; required; relationship target [project](entities/project.md)
- **[core_metadata_collection](entities/core_metadata_collection.md):** `to_one_project`; required; relationship target [project](entities/project.md)
- **[experiment](entities/experiment.md):** `to_one_project`; required; relationship target [project](entities/project.md)
- **[keyword](entities/keyword.md):** `to_many_project`; required; relationship target [project](entities/project.md)
- **[lab](entities/lab.md):** `to_many_project`; required; relationship target [project](entities/project.md)
- **[publication](entities/publication.md):** `to_many_project`; required; relationship target [project](entities/project.md)
- **[study](entities/study.md):** `to_one_project`; required; relationship target [project](entities/project.md)

### `protocol_used`

- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. Name or other identifier given to the protocol used during an IMC run.

### `publisher`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. An entity responsible for making the resource available. Examples of a Publisher include a person, an organization, or a service. Typically, the name of a Publisher should be used to indicate the entity.

### `race`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau. Allowed values: white; american indian or alaska native; black or african american; asian; native hawaiian or other pacific islander; other; … (+5 more).

### `rct_meld_strata`

- **[case](entities/case.md):** `enum`; optional/not marked required. The text term used to describe the MELD strata of the patient. Allowed values: Low(<=25); High(>25).

### `read_group_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Read group name.

### `read_groups`

- **[read_group_qc](entities/read_group_qc.md):** `to_one`; required; relationship target [read_group](entities/read_group.md)
- **[simple_germline_variation](entities/simple_germline_variation.md):** `to_many`; optional/not marked required; relationship target [read_group](entities/read_group.md)
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `to_many`; optional/not marked required; relationship target [read_group](entities/read_group.md)
- **[submitted_copy_number](entities/submitted_copy_number.md):** `to_many`; optional/not marked required; relationship target [read_group](entities/read_group.md)
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `to_many`; required; relationship target [read_group](entities/read_group.md)
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `to_many`; optional/not marked required; relationship target [read_group](entities/read_group.md)
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `to_one`; optional/not marked required; relationship target [read_group](entities/read_group.md)

### `read_length`

- **[read_group](entities/read_group.md):** `integer`; optional/not marked required. The length of the reads.

### `read_pair_number`

- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; optional/not marked required. NEW: Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. Allowed values: R1; R2; R3; Not Applicable.

### `relation`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. A related resource. Recommended best practice is to identify the related resource by means of a string conforming to a formal identification system.�

### `relationship_age_at_diagnosis`

- **[family_history](entities/family_history.md):** `number`; optional/not marked required. The age (in years) when the patient's relative was first diagnosed.

### `relationship_gender`

- **[family_history](entities/family_history.md):** `enum`; optional/not marked required. Text designations that identify gender. Gender is described as the assemblage of properties that distinguish people on the basis of their societal roles. [Explanatory Comment 1: Identification of gender is based upon self-report and may come from a form, questionnaire, interview, etc.] Allowed values: female; male; unknown; unspecified; not reported.

### `relationship_primary_diagnosis`

- **[family_history](entities/family_history.md):** `string`; optional/not marked required. Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.

### `relationship_type`

- **[family_history](entities/family_history.md):** `string`; optional/not marked required. The subgroup that describes the state of connectedness between members of the unit of society organized around kinship ties.

### `relative_cytokeratin_intensity`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. The ratio of the single cell's cytokeratin staining intensity to the average of the surrounding cells.

### `relative_er_intensity`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. The ratio of the single cell's endoplasmic reticulum staining intensity to the average of the surrounding cells.

### `relative_nuclear_intensity`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. The ratio of the single cell's nuclear staining intensity to the average of the surrounding cells.

### `relative_nuclear_size`

- **[slide_count](entities/slide_count.md):** `number`; optional/not marked required. The ratio of the single cell's nucleus size to the average of the surrounding cells.

### `relative_with_cancer_history`

- **[family_history](entities/family_history.md):** `enum`; optional/not marked required. Indicator to signify whether or not an individual's biological relative has been diagnosed with another type of cancer. Allowed values: yes; no; unknown; not reported.

### `releasable`

- **[project](entities/project.md):** `boolean`; optional/not marked required. A project can only be released by the user when `releasable` is true.

### `released`

- **[project](entities/project.md):** `boolean`; optional/not marked required. To release a project is to tell the GDC to include all submitted entities in the next GDC index.

### `residual_disease`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. Text terms to describe the status of a tissue margin following surgical resection. Allowed values: R0; R1; R2; RX.

### `rights`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. Information about rights held in and over the resource. Typically, rights information includes a statement about various property rights associated with the resource, including intellectual property rights.

### `RIN`

- **[read_group](entities/read_group.md):** `number`; optional/not marked required. A numerical assessment of the integrity of RNA based on the entire electrophoretic trace of the RNA sample including the presence or absence of degradation products.

### `rna_expression_calling_workflows`

- **[gene_expression](entities/gene_expression.md):** `to_one`; optional/not marked required; relationship target [rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md)

### `run_datetime`

- **[slide](entities/slide.md):** `datetime`; optional/not marked required

### `run_name`

- **[slide](entities/slide.md):** `string`; optional/not marked required. Name, number, or other identifier given to this slide's run.
- **[slide_count](entities/slide_count.md):** `string`; optional/not marked required. The name or identifier given to the run that was used to generate this slide count.
- **[slide_image](entities/slide_image.md):** `string`; optional/not marked required. Name, number, or other identifier given to the run that generated this slide image.

### `sample_collection`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term to describe if any sample collection was done during the visit Allowed values: Yes; No.

### `sample_date_time`

- **[sample](entities/sample.md):** `datetime`; optional/not marked required

### `sample_exception`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term represents exceptions during sample collection Allowed values: Yes; No.

### `sample_exception_clotted`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to clotting Allowed values: Yes; No; N/A.

### `sample_exception_contaminated`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to contamination Allowed values: Yes; No; N/A.

### `sample_exception_damaged`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to damage Allowed values: Yes; No; N/A.

### `sample_exception_hemolyzed`

- **[sample](entities/sample.md):** `enum`; optional/not marked required Allowed values: Yes; No; N/A.

### `sample_exception_hemorrhagic`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to hemorrhage Allowed values: Yes; No; N/A.

### `sample_exception_insufficient_quantity`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to insufficient quantity Allowed values: Yes; No; N/A.

### `sample_exception_late_processing_24H`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to late processing by 24 hours Allowed values: Yes; No; N/A.

### `sample_exception_late_processing_8H`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to late processing by 8 hours Allowed values: Yes; No; N/A.

### `sample_exception_lipemic`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to lipemia Allowed values: Yes; No; N/A.

### `sample_exception_necrotic`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to necrosis Allowed values: Yes; No; N/A.

### `sample_exception_thawed`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that represents if the sample exception was applied due to thawing Allowed values: Yes; No; N/A.

### `sample_fast`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term to describe if the patient fasted before sample collection Allowed values: Yes; No.

### `sample_fast_hours`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. Number representing the total hours fasted before collecting the sample

### `sample_home_collection_kit`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term to describe if the sample was collected using a home collection kit Allowed values: Yes; No.

### `sample_number_of_tubes`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. Number representing the number of tubes collected

### `sample_transportation_method_ice`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term that describes if the sample was transported to study site on ice Allowed values: Yes; No.

### `sample_type`

- **[sample](entities/sample.md):** `enum`; optional/not marked required. Text term to describe the source of a biospecimen used for a laboratory test. Allowed values: Blood Derived Normal; Blood Derived Normal - Serum; Blood Derived Normal - Whole blood; Blood Derived Normal - Platelet Poor Plasma; Blood Derived Normal - HCl/Neat Plasma; Peripheral Blood Mononuclear Cells; … (+4 more).

### `samples`

- **[slide](entities/slide.md):** `to_many`; required; relationship target [sample](entities/sample.md)

### `section_location`

- **[slide](entities/slide.md):** `string`; optional/not marked required. Tissue source of the slide.

### `sequence_duplication_levels`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `sequence_length_distribution`

- **[read_group_qc](entities/read_group_qc.md):** `qc_metrics_state`; required

### `sequencing_center`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of the center that provided the sequence files.

### `sequencing_date`

- **[read_group](entities/read_group.md):** `datetime`; optional/not marked required

### `sex`

- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. Sex of patient at birth. Allowed values: male; female; unknown; unspecified.

### `short_name`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Shortened name of the lab (e.g. ARDaC).

### `single_cell_library`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. NEW: Library preparation strategy that distinguishes different single-cell assays. Allowed values: Chromium 3' Gene Expression v2 Library; Chromium 3' Gene Expression v3 Library; Chromium scATAC v1 Library; Smart-Seq2.

### `site_of_resection_or_biopsy`

- **[diagnosis](entities/diagnosis.md):** `string`; required. The third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries for coding the site (topography) and the histology (morphology) of neoplasms. The description of an anatomical region or of a body part. Named locations of, or within, the body. A system of numbered categories for representation of data.

### `size_selection_range`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Range of size selection.

### `slide_identifier`

- **[slide](entities/slide.md):** `string`; optional/not marked required. Unique identifier given to the this slide.

### `slides`

- **[slide_count](entities/slide_count.md):** `to_many`; required; relationship target [slide](entities/slide.md)
- **[slide_image](entities/slide_image.md):** `to_one`; optional/not marked required; relationship target [slide](entities/slide.md)

### `soc_collected`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if standard of care procedure information collected. Allowed values: Yes; No.

### `somatic_copy_number_workflows`

- **[copy_number_auxiliary_file](entities/copy_number_auxiliary_file.md):** `to_one`; optional/not marked required; relationship target [somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md)
- **[copy_number_estimate](entities/copy_number_estimate.md):** `to_one`; optional/not marked required; relationship target [somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md)
- **[copy_number_segment](entities/copy_number_segment.md):** `to_one`; optional/not marked required; relationship target [somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md)

### `somatic_mutations_identified`

- **[experiment](entities/experiment.md):** `boolean`; optional/not marked required. Are somatic mutations identified for this experiment?

### `source`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. A related resource from which the described resource is derived. The described resource may be derived from the related resource in whole or in part. Recommended best practice is to identify the related resource by means of a string conforming to a formal identification system.

### `specimen_type`

- **[aliquot](entities/aliquot.md):** `enum`; optional/not marked required. Term to describe type of sample collection. Allowed values: Platelet Poor Plasma; HCl Acidified Plasma; HCl Sodium Citrate Plasma; CPT Plasma; PBMC; Serum; … (+11 more).

### `spike_ins_concentration`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Spike in concentration.

### `spike_ins_fasta`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of the FASTA file that contains the spike-in sequences.

### `state`

- **[acknowledgement](entities/acknowledgement.md):** `state`; optional/not marked required
- **[aliquot](entities/aliquot.md):** `state`; optional/not marked required
- **[audit](entities/audit.md):** `state`; optional/not marked required
- **[case](entities/case.md):** `state`; optional/not marked required
- **[clinical_test](entities/clinical_test.md):** `state`; optional/not marked required
- **[demographic](entities/demographic.md):** `state`; optional/not marked required
- **[diagnosis](entities/diagnosis.md):** `state`; optional/not marked required
- **[experiment](entities/experiment.md):** `state`; optional/not marked required
- **[exposure](entities/exposure.md):** `state`; optional/not marked required
- **[family_history](entities/family_history.md):** `state`; optional/not marked required
- **[follow_up](entities/follow_up.md):** `state`; optional/not marked required
- **[keyword](entities/keyword.md):** `state`; optional/not marked required
- **[lab](entities/lab.md):** `state`; optional/not marked required
- **[molecular_test](entities/molecular_test.md):** `state`; optional/not marked required
- **[project](entities/project.md):** `enum`; optional/not marked required. The possible states a project can be in. All but `open` are equivalent to some type of locked state. Allowed values: open; review; submitted; processing; closed; legacy.
- **[publication](entities/publication.md):** `state`; optional/not marked required
- **[read_group](entities/read_group.md):** `state`; optional/not marked required
- **[sample](entities/sample.md):** `state`; optional/not marked required
- **[slide](entities/slide.md):** `state`; optional/not marked required
- **[slide_count](entities/slide_count.md):** `state`; optional/not marked required
- **[study](entities/study.md):** `state`; optional/not marked required
- **[treatment](entities/treatment.md):** `state`; optional/not marked required

### `stool_test`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe if a stool test was performed. Allowed values: Yes; WBCs present; Yes; C. diff present; Yes; both WBCs and C. diff present; Yes; neither WBCs or C diff present; Not Done.

### `stool_test_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of stool test. In (YYYY-MM-DD) format.

### `stool_test_finding`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Text used to describe other stool findings if present.

### `structural_variant_calling_workflows`

- **[structural_variation](entities/structural_variation.md):** `to_one`; optional/not marked required; relationship target [structural_variant_calling_workflow](entities/structural_variant_calling_workflow.md)

### `studies`

- **[case](entities/case.md):** `to_one`; required; relationship target [study](entities/study.md)

### `study_description`

- **[study](entities/study.md):** `string`; optional/not marked required. A brief description of the study being performed. Free text.

### `study_name`

- **[study](entities/study.md):** `string`; required

### `study_site`

- **[case](entities/case.md):** `enum`; optional/not marked required. The text term used to describe the study site location of the patient. Allowed values: Cleveland Clinic; Indiana University; University of Louisville; University of Massachusetts; Beth Israel Deaconess Medical Center; Virginia Commonwealth University; … (+10 more).

### `subject`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. The topic of the resource. Typically, the subject will be represented using keywords, key phrases, or classification codes. Recommended best practice is to use a controlled vocabulary.

### `submitted_aligned_reads_files`

- **[aligned_reads](entities/aligned_reads.md):** `to_one`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[aligned_reads_index](entities/aligned_reads_index.md):** `to_one`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[alignment_workflow](entities/alignment_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[read_group_qc](entities/read_group_qc.md):** `to_one`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `to_one`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)
- **[simple_germline_variation](entities/simple_germline_variation.md):** `to_many`; optional/not marked required; relationship target [submitted_aligned_reads](entities/submitted_aligned_reads.md)

### `submitted_genomic_profiles`

- **[genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md):** `to_one`; optional/not marked required; relationship target [submitted_genomic_profile](entities/submitted_genomic_profile.md)

### `submitted_genotyping_arrays`

- **[somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_genotyping_array](entities/submitted_genotyping_array.md)

### `submitted_tangent_copy_numbers`

- **[copy_number_liftover_workflow](entities/copy_number_liftover_workflow.md):** `to_one`; optional/not marked required; relationship target [submitted_tangent_copy_number](entities/submitted_tangent_copy_number.md)

### `submitted_unaligned_reads_files`

- **[aligned_reads](entities/aligned_reads.md):** `to_many`; optional/not marked required; relationship target [submitted_unaligned_reads](entities/submitted_unaligned_reads.md)
- **[alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_unaligned_reads](entities/submitted_unaligned_reads.md)
- **[alignment_workflow](entities/alignment_workflow.md):** `to_many`; optional/not marked required; relationship target [submitted_unaligned_reads](entities/submitted_unaligned_reads.md)
- **[read_group_qc](entities/read_group_qc.md):** `to_many`; optional/not marked required; relationship target [submitted_unaligned_reads](entities/submitted_unaligned_reads.md)
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `to_one`; optional/not marked required; relationship target [submitted_unaligned_reads](entities/submitted_unaligned_reads.md)

### `submitter_id`

- **[acknowledgement](entities/acknowledgement.md):** `string / null`; required
- **[aliquot](entities/aliquot.md):** `string / null`; required. The legacy barcode used before prior to the use UUIDs. For TCGA this is bcraliquotbarcode.
- **[audit](entities/audit.md):** `string / null`; required
- **[case](entities/case.md):** `string / null`; required
- **[clinical_test](entities/clinical_test.md):** `string / null`; required
- **[demographic](entities/demographic.md):** `string / null`; required
- **[diagnosis](entities/diagnosis.md):** `string / null`; required
- **[experiment](entities/experiment.md):** `string / null`; required
- **[exposure](entities/exposure.md):** `string / null`; required
- **[family_history](entities/family_history.md):** `string / null`; required
- **[follow_up](entities/follow_up.md):** `string / null`; required
- **[keyword](entities/keyword.md):** `string / null`; required
- **[lab](entities/lab.md):** `string / null`; required
- **[molecular_test](entities/molecular_test.md):** `string / null`; required
- **[publication](entities/publication.md):** `string / null`; required
- **[read_group](entities/read_group.md):** `string`; required
- **[sample](entities/sample.md):** `string / null`; required. The legacy barcode used before prior to the use UUIDs, varies by project. For TCGA this is bcrsamplebarcode.
- **[slide](entities/slide.md):** `string / null`; required
- **[slide_count](entities/slide_count.md):** `string / null`; required
- **[study](entities/study.md):** `string / null`; required
- **[treatment](entities/treatment.md):** `string / null`; required

### `support_id`

- **[project](entities/project.md):** `string`; optional/not marked required. The ID of the source providing support/grant resources.

### `support_source`

- **[project](entities/project.md):** `string`; optional/not marked required. The name of source providing support/grant resources.

### `target_capture_kit`

- **[read_group](entities/read_group.md):** `enum`; optional/not marked required. NEW: Description that can uniquely identify a target capture kit. Suggested value is a combination of vendor, kit name, and kit version. Allowed values: Custom AmpliSeq Cancer Hotspot GENIE-MDA Augmented Panel v1 - 46 Genes; Custom GENIE-DFCI OncoPanel - 275 Genes; Custom GENIE-DFCI Oncopanel - 300 Genes; Custom GENIE-DFCI Oncopanel - 447 Genes; Custom HaloPlex DLBCL Panel - 370 Genes; Custom Ion AmpliSeq Hotspot GENIE-MOSC3 Augmented Panel - 74 Genes; … (+43 more).

### `target_capture_kit_catalog_number`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Catalog of Target Capture Kit.

### `target_capture_kit_name`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Name of Target Capture Kit.

### `target_capture_kit_target_region`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Target Capture Kit BED file.

### `target_capture_kit_vendor`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Vendor of Target Capture Kit.

### `target_capture_kit_version`

- **[read_group](entities/read_group.md):** `string`; optional/not marked required. Version of Target Capture Kit.

### `test_result`

- **[molecular_test](entities/molecular_test.md):** `enum`; optional/not marked required. The text term used to describe the result of the molecular test. If the test result was a numeric value see test_value. Allowed values: Abnormal; Copy Number Reported; Equivocal; High; Intermediate; Loss of Expression; … (+8 more).

### `test_unit`

- **[molecular_test](entities/molecular_test.md):** `string / null`; optional/not marked required. The unit for the test

### `test_value`

- **[molecular_test](entities/molecular_test.md):** `string / null`; optional/not marked required. The text term or numeric value used to describe a sepcific result of a molecular test.

### `therapeutic_agents`

- **[treatment](entities/treatment.md):** `string`; optional/not marked required. Text identification of the individual agent(s) used as part of a prior treatment regimen.

### `time_between_collection_and_freezing`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. Numeric representation of the elapsed time between the sample collection and freezing, measured in minutes

### `tissue_or_organ_of_origin`

- **[diagnosis](entities/diagnosis.md):** `string`; required. Text term that describes the anatomic site of the tumor or disease.

### `title`

- **[core_metadata_collection](entities/core_metadata_collection.md):** `string`; optional/not marked required. A name given to the resource. Typically, a Title will be a name by which the resource is formally known.

### `tlfb_collected`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe of the Timeline Followback (TLFB) questionnaire was completed. Allowed values: Yes; No.

### `tlfb_drinking_days`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for the total number of drinking days out of the 30 days prior to the visit as reported in the TLFB.

### `tlfb_number_drinks`

- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. Numerical value for the total number of drinks in the 30 days prior to the visit as reported in the TLFB.

### `to_trim_adapter_sequence`

- **[read_group](entities/read_group.md):** `boolean`; optional/not marked required. Does the user suggest adapter trimming?

### `tobacco_smoking_onset_year`

- **[exposure](entities/exposure.md):** `integer`; optional/not marked required. The year in which the participant began smoking.

### `tobacco_smoking_quit_year`

- **[exposure](entities/exposure.md):** `integer`; optional/not marked required. The year in which the participant quit smoking.

### `tobacco_smoking_status`

- **[exposure](entities/exposure.md):** `enum`; optional/not marked required. Category describing current smoking status and smoking history as self-reported by a patient. Allowed values: 1; 2; 3; 4; 5; 6; … (+4 more).

### `total_aligned_reads`

- **[read_group_qc](entities/read_group_qc.md):** `integer`; optional/not marked required. The total number of reads with at least one reported alignment.

### `total_cell_count`

- **[sample](entities/sample.md):** `integer`; optional/not marked required. Number representing the total cell count in the sample (in million)

### `total_sequences`

- **[read_group_qc](entities/read_group_qc.md):** `integer`; required. A count of the total number of sequences processed.

### `total_variants`

- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `integer`; optional/not marked required. The total number of variants detected carrying a base change difference from the reference genome.

### `translational_projects_title`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. Title of the translational projects.

### `treatment_anatomic_site`

- **[treatment](entities/treatment.md):** `enum`; optional/not marked required. The anatomic site or field targeted by a treatment regimen or single agent therapy. Allowed values: Abdomen, total; Arm; Ascites; Axillary; Body, total; Bone; … (+71 more).

### `treatment_intent_type`

- **[treatment](entities/treatment.md):** `string`; optional/not marked required. Text term to identify the reason for the administration of a treatment regimen. [Manually-curated]

### `treatment_or_therapy`

- **[treatment](entities/treatment.md):** `enum`; optional/not marked required. A yes/no/unknown/not applicable indicator related to the administration of therapeutic agents received before the body specimen was collected. Allowed values: yes; no; unknown; not reported.

### `treatment_outcome`

- **[treatment](entities/treatment.md):** `enum`; optional/not marked required. Text term that describes the patient�s final outcome after the treatment was administered. Allowed values: Complete Response; Partial Response; Treatment Ongoing; Treatment Stopped Due to Toxicity; Unknown.

### `treatment_type`

- **[treatment](entities/treatment.md):** `enum`; optional/not marked required. Text term that describes the kind of treatment administered. Allowed values: Ablation; Chemotherapy; Concurrent Chemoradiation; Cryoablation; Embolization; Hormone Therapy; … (+11 more).

### `tumor_grade`

- **[diagnosis](entities/diagnosis.md):** `string`; required. Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.

### `tumor_stage`

- **[diagnosis](entities/diagnosis.md):** `string`; required. The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body. The accepted values for tumor_stage depend on the tumor site, type, and accepted staging system. These items should accompany the tumor_stage value as associated metadata.

### `type`

- **[acknowledgement](entities/acknowledgement.md):** `enum`; required Allowed values: acknowledgement.
- **[aligned_reads_index](entities/aligned_reads_index.md):** `enum`; required Allowed values: aligned_reads_index.
- **[alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md):** `enum`; required Allowed values: alignment_cocleaning_workflow.
- **[alignment_workflow](entities/alignment_workflow.md):** `enum`; required Allowed values: alignment_workflow.
- **[aliquot](entities/aliquot.md):** `string`; required
- **[audit](entities/audit.md):** `string`; required
- **[case](entities/case.md):** `string`; required
- **[clinical_test](entities/clinical_test.md):** `enum`; required Allowed values: clinical_test.
- **[demographic](entities/demographic.md):** `string`; required
- **[diagnosis](entities/diagnosis.md):** `string`; required
- **[experiment](entities/experiment.md):** `enum`; required Allowed values: experiment.
- **[experimental_metadata](entities/experimental_metadata.md):** `enum`; required Allowed values: experimental_metadata.
- **[exposure](entities/exposure.md):** `enum`; required Allowed values: exposure.
- **[family_history](entities/family_history.md):** `enum`; required Allowed values: family_history.
- **[follow_up](entities/follow_up.md):** `enum`; required Allowed values: follow_up.
- **[germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md):** `enum`; required Allowed values: germline_mutation_calling_workflow.
- **[keyword](entities/keyword.md):** `enum`; required Allowed values: keyword.
- **[lab](entities/lab.md):** `string`; required
- **[mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md):** `enum`; required Allowed values: germline_mutation_calling_workflow.
- **[molecular_test](entities/molecular_test.md):** `string`; required
- **[program](entities/program.md):** `string`; optional/not marked required
- **[project](entities/project.md):** `string`; optional/not marked required
- **[publication](entities/publication.md):** `enum`; required Allowed values: publication.
- **[read_group](entities/read_group.md):** `enum`; required Allowed values: read_group.
- **[read_group_qc](entities/read_group_qc.md):** `enum`; required Allowed values: read_group_qc.
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `enum`; required Allowed values: rna_expression_calling_workflow.
- **[sample](entities/sample.md):** `string`; required
- **[slide](entities/slide.md):** `string`; required
- **[slide_count](entities/slide_count.md):** `enum`; required Allowed values: slide_count.
- **[slide_image](entities/slide_image.md):** `enum`; required Allowed values: slide_image.
- **[structural_variation](entities/structural_variation.md):** `enum`; required Allowed values: aligned_reads.
- **[study](entities/study.md):** `string`; required
- **[submitted_aligned_reads](entities/submitted_aligned_reads.md):** `enum`; required Allowed values: submitted_aligned_reads.
- **[submitted_copy_number](entities/submitted_copy_number.md):** `enum`; required Allowed values: submitted_copy_number.
- **[submitted_genomic_profile](entities/submitted_genomic_profile.md):** `enum`; required Allowed values: submitted_genomic_profile.
- **[submitted_methylation](entities/submitted_methylation.md):** `enum`; required Allowed values: submitted_methylation.
- **[submitted_somatic_mutation](entities/submitted_somatic_mutation.md):** `enum`; required Allowed values: submitted_somatic_mutation.
- **[submitted_unaligned_reads](entities/submitted_unaligned_reads.md):** `enum`; required Allowed values: submitted_unaligned_reads.
- **[treatment](entities/treatment.md):** `enum`; required Allowed values: treatment.

### `type_of_data`

- **[experiment](entities/experiment.md):** `enum`; optional/not marked required. Is the data raw or processed? Allowed values: Raw; Processed.
- **[study](entities/study.md):** `enum`; optional/not marked required. Is the data raw or processed? Allowed values: Raw; Processed; Raw/ Processed.

### `type_of_sample`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. String indicator identifying the types of samples as contrived or clinical.

### `type_of_specimen`

- **[experiment](entities/experiment.md):** `string`; optional/not marked required. Broad description of the specimens used in the experiment.

### `ultrasound_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The date of ultrasound. In (YYYY-MM-DD) format.

### `ultrasound_finding`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Description of the overall findings/impressions from the ultrasound.

### `ultrasound_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the results of the ultrasound. Allowed values: Normal; Abnormal; Missing.

### `ultrasound_result_sig`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the ultrasound results are clinically significant. Allowed values: Yes; No; Missing.

### `updated_datetime`

- **[acknowledgement](entities/acknowledgement.md):** `datetime`; optional/not marked required
- **[aliquot](entities/aliquot.md):** `datetime`; optional/not marked required
- **[audit](entities/audit.md):** `datetime`; optional/not marked required
- **[case](entities/case.md):** `datetime`; optional/not marked required
- **[clinical_test](entities/clinical_test.md):** `datetime`; optional/not marked required
- **[demographic](entities/demographic.md):** `datetime`; optional/not marked required
- **[diagnosis](entities/diagnosis.md):** `datetime`; optional/not marked required
- **[experiment](entities/experiment.md):** `datetime`; optional/not marked required
- **[exposure](entities/exposure.md):** `datetime`; optional/not marked required
- **[family_history](entities/family_history.md):** `datetime`; optional/not marked required
- **[follow_up](entities/follow_up.md):** `datetime`; optional/not marked required
- **[keyword](entities/keyword.md):** `datetime`; optional/not marked required
- **[lab](entities/lab.md):** `datetime`; optional/not marked required
- **[molecular_test](entities/molecular_test.md):** `datetime`; optional/not marked required
- **[publication](entities/publication.md):** `datetime`; optional/not marked required
- **[read_group](entities/read_group.md):** `datetime`; optional/not marked required
- **[sample](entities/sample.md):** `datetime`; optional/not marked required
- **[slide](entities/slide.md):** `datetime`; optional/not marked required
- **[slide_count](entities/slide_count.md):** `datetime`; optional/not marked required
- **[study](entities/study.md):** `datetime`; optional/not marked required
- **[treatment](entities/treatment.md):** `datetime`; optional/not marked required

### `urine_culture`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if a urine culture test was done. Allowed values: Yes; No; Missing; Not Done.

### `urine_culture_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of urine culture. In (YYYY-MM-DD) format.

### `urine_culture_fungal_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe if the urine culture was positive for a fungal culture with >50,000 colonies/mL? Allowed values: Yes; No; Positive fungal culture ≤50,000 colonies/mL; No; Positive for other organisms only; Missing.

### `urine_culture_organism`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Text used to describe the organism growth found during urine culture test.

### `urine_culture_result`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The text term used to describe the results of the urine culture test. Allowed values: Positive; Negative; Missing.

### `url_of_lab_website`

- **[lab](entities/lab.md):** `string / null`; optional/not marked required. URL to the lab’s website.

### `usaudit_collected`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. The yes/no indicator to describe if the AUDIT was collected at this visit. Allowed values: Yes; No.

### `usaudit_completed_by`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. The text term used to describe the person who completed the AUDIT. Allowed values: Patient/Study Participant; Relative of Patient/Study Participant; Friend of Patient/Study Participant; Other.

### `usaudit_q1`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often do you have a drink containing alcohol? Allowed values: Never; Less than monthly; Monthly; Weekly; 2 to 3 times a week; 4 to 6 times a week; … (+1 more).

### `usaudit_q10`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, has a relative, friend, doctor, or other health care worker been concerned about your drinking and suggested you cut down? Allowed values: No; Yes, but not in the past year; Yes, during the past year.

### `usaudit_q2`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how many drinks containing alcohol do you have on a typical day you are drinking? Allowed values: 1 drink; 2 drinks; 3 drinks; 4 drinks; 5 to 6 drinks; 7 to 9 drinks; … (+1 more).

### `usaudit_q3`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often do you have X (5 for men; 4 for women and men over age 65) or more drinks on one occasion? Allowed values: Never; Less than monthly; Monthly; Weekly; 2 to 3 times a week; 4 to 6 times a week; … (+1 more).

### `usaudit_q4`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often have you found that you were not able to stop drinking once you had started? Allowed values: Never; Less than monthly; Monthly; Weekly; Daily or almost daily.

### `usaudit_q5`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often have you failed to do what was expected of you because of drinking? Allowed values: Never; Less than monthly; Monthly; Weekly; Daily or almost daily.

### `usaudit_q6`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often have you needed a drink first thing in the morning to get yourself going after a heavy drinking session? Allowed values: Never; Less than monthly; Monthly; Weekly; Daily or almost daily.

### `usaudit_q7`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often have you had a feeling of guilt or remorse after drinking? Allowed values: Never; Less than monthly; Monthly; Weekly; Daily or almost daily.

### `usaudit_q8`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, how often have you been unable to remember what happened the night before because you had been drinking? Allowed values: Never; Less than monthly; Monthly; Weekly; Daily or almost daily.

### `usaudit_q9`

- **[audit](entities/audit.md):** `enum`; optional/not marked required. Thinking about your drinking in the past year, have you or someone else been injured because of your drinking? Allowed values: No; Yes, but not in the past year; Yes, during the past year.

### `varices`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if subject has been diagnosed with moderate/large varices or bleeding from varices. Allowed values: Yes; No; Not Reported; Missing.

### `varices_diagnosis_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of most recent diagnosis of moderate/large varices or bleeding from varices. In (YYYY-MM-DD) format.

### `vascular_invasion_present`

- **[diagnosis](entities/diagnosis.md):** `enum`; optional/not marked required. The yes/no indicator to ask if large vessel or venous invasion was detected by surgery or presence in a tumor specimen. Allowed values: Yes; No; Unknown; Not Reported; Not Allowed To Collect.

### `visit_date`

- **[sample](entities/sample.md):** `datetime`; optional/not marked required

### `visit_day`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. Number of days between the baseline and when the visit is scheduled according to the protocol. Equivalent to the visit. Allowed values: 0; 3; 7; 14; 28; 60; … (+4 more).

### `vital_status`

- **[case](entities/case.md):** `enum`; optional/not marked required. Vital status of the patient. Allowed values: alive; dead; Unknown.
- **[demographic](entities/demographic.md):** `enum`; optional/not marked required. The survival state of the person registered on the protocol. Allowed values: Alive; Dead; Unknown; Not Reported; None.
- **[diagnosis](entities/diagnosis.md):** `enum`; required. The survival state of the person registered on the protocol. Allowed values: alive; dead; lost to follow-up; unknown; not reported; Not Allowed To Collect; … (+1 more).

### `weight`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. The weight of the patient measured in kilograms.
- **[follow_up](entities/follow_up.md):** `number`; optional/not marked required. The weight of the patient measured in kilograms.

### `workflow_type`

- **[alignment_cocleaning_workflow](entities/alignment_cocleaning_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: BWA with Mark Duplicates and Cocleaning.
- **[alignment_workflow](entities/alignment_workflow.md):** `enum`; required Allowed values: STAR; BWA-aln; BWA-mem; spinnaker.
- **[copy_number_liftover_workflow](entities/copy_number_liftover_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: DNAcopy.
- **[copy_number_variation_workflow](entities/copy_number_variation_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: GISTIC - Copy Number Score; GISTIC - Arm Level Copy Number; GISTIC - Focal Deletion; GISTIC - Focal Amplification.
- **[genomic_profile_harmonization_workflow](entities/genomic_profile_harmonization_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: FM Copy Number Variation; FM Simple Somatic Mutation; FM Structural Variation; GENIE Copy Number Variation; GENIE Simple Somatic Mutation; GENIE Structural Variation; … (+2 more).
- **[germline_mutation_calling_workflow](entities/germline_mutation_calling_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: HaplotypeCaller.
- **[mirna_expression_calling_workflow](entities/mirna_expression_calling_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: HaplotypeCaller.
- **[read_group_qc](entities/read_group_qc.md):** `enum`; optional/not marked required. Generic name for the workflow used to analyze a data set. Allowed values: Read Group Quality Control.
- **[rna_expression_calling_workflow](entities/rna_expression_calling_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: CellRanger - 10x Filtered Counts; CellRanger - 10x Raw Counts; Cufflinks; DEXSeq; HTSeq - Counts; HTSeq - FPKM; … (+11 more).
- **[somatic_copy_number_workflow](entities/somatic_copy_number_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: ABSOLUTE LiftOver; ASCAT3; ASCAT2; AscatNGS; GATK4 CNV.
- **[structural_variant_calling_workflow](entities/structural_variant_calling_workflow.md):** `enum`; required. Generic name for the workflow used to analyze a data set. Allowed values: Arriba; BRASS; Fusion Catcher; Pizzly; STAR-Fusion; SvABA.

### `xray`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if a x-ray was done as a standard of care procedure. Allowed values: Yes; No.

### `xray_date`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. Date of X-ray. In (YYYY-MM-DD) format.

### `xray_findings`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The text describing any additional findings from the x-ray.

### `xray_impression`

- **[follow_up](entities/follow_up.md):** `string`; optional/not marked required. The text describing a list of impression ( if any) found during the x-ray.

### `xray_infiltrates`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if there are infiltrates noted. Allowed values: Yes; No; Not Reported.

### `xray_last_4_weeks`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the patient received a chest X-ray in the last 4 weeks. Allowed values: Yes; No; Not Reported.

### `xray_normal`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if the x-ray scan was normal. Allowed values: Yes; No; Missing.

### `xray_pleural_effusion`

- **[follow_up](entities/follow_up.md):** `enum`; optional/not marked required. The yes/no indicator used to describe if pleural effusion was found during the x-ray. Allowed values: Yes; No; Missing.

### `year_of_birth`

- **[demographic](entities/demographic.md):** `number / null`; optional/not marked required. Numeric value to represent the calendar year in which an individual was born.

### `year_of_death`

- **[demographic](entities/demographic.md):** `number`; optional/not marked required. Numeric value to represent the year of the death of an individual.

### `year_of_diagnosis`

- **[diagnosis](entities/diagnosis.md):** `number / null`; optional/not marked required. Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer.

### `years_smoked`

- **[exposure](entities/exposure.md):** `number`; optional/not marked required. Numeric value (or unknown) to represent the number of years a person has been smoking.
