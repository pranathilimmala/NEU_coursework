# "Adding the KEGG Pathways using Swissprot Database"

## Overview
An Application Programming Interface or API provides a programmatic way to access data from a service like KEGG.
A group of databases known as KEGG (Kyoto Encyclopedia of Genes and Genomes) contains information on genomes, biological pathways, illnesses, medications, and chemical compounds. Data analysis in genomes, metagenomics, metabolomics, and other omics studies, modeling and simulation in systems biology, and translational research in drug development all make use of KEGG. KEGG is also used for bioinformatics research and education.

## Author
Pranathi Limmala

## Date created
12/07 /2022

## Required python script for Module 10 assignment :

addKEGGPathways.py


## Results

alignPredicted.txt (Output file)

## Methods

BLAST: Basic Local Alignment Search Tool (BLAST) searches for optimal local alignments between a query and a sequence database in a speed-optimized fashion. These start with an initial "word" of size "W" that scores above a threshold "T." From there, the alignment is extended in each direction seeking to find an alignment of the score "S" or greater. In some ways, these Words are similar to the k-mers we discussed previously. We simplify the initial search when we divide the query into smaller words. Adjusting the values for W, T, and S can change the sensitivity and speed of our search.

Reference: https://northeastern.instructure.com/courses/122305/pages/module-9-practice-blast-and-transdecoder

KEGG Pathway (API Method):Protein-protein interactions (PPIs) are the outcomes of two proteins coming into close physical contact and are typically responsible for particular biological functions or regulatory processes. The exploration of PPIs' pattern and principle for characterization and study has remained an open subject in biological studies. PPI research have been conducted using a variety of experimental and computational methodologies, although the majority of them are based on sequence similarity with current validated PPI participants or cellular localization patterns. The fact that PPIs are defined by their unique biological roles is overlooked by the majority of approaches. In this study, employing gene ontology and KEGG pathway annotation of PPI participants, we developed a unique rule-based computational technique that corresponds to the complex biological consequences of PPIs.
Our recently developed computational method discovered a collection of biological processes that are closely related to PPIs and offered a brand-new function-based tool for PPI studies in a rule-based fashion. •A machine learning model of protein-protein interaction that can be understood by rules was created. •A binary GO and KEGG annotation vector served as a representation for each protein. •To depict a protein-protein pair, we employed the sum and absolute difference of two protein vectors. •Using the feature selection method, the essential GO and KEGG function features were found. Using decision trees, it was possible to learn the predictions for protein-protein interactions.
 
 Reference: Zhang, Y.-H., Zeng, T., Chen, L., Huang, T., & Cai, Y.-D. (2021). Determining protein–protein functional associations by functional rules based on gene ontology and KEGG pathway. Biochimica et Biophysica Acta. Proteins and Proteomics, 1869(6), 140621–140621. https://doi.org/10.1016/j.bbapap.2021.140621
 
 Swissprot database: The goal of SWISS-PROT, a curated protein sequence database, is to offer high levels of annotation (such as descriptions of a protein's function, its domain structure, post-translational modifications, variations, etc.), low levels of redundancy, and high levels of database integration. The database has recently undergone upgrades to its format and content, cross-references to other databases, new documentation files, and TrEMBL, a computer-annotated complement to SWISS-PROT. All of the coding sequences (CDSs) in the EMBL Nucleotide Sequence Database were translated into entries in the SWISS-PROT-like format for TrEMBL, with the exception of the CDSs that were previously included in SWISS-PROT. We also discuss the Human Proteomics Initiative (HPI), a significant endeavor to annotate all existing human sequences in accordance with SWISS-quality PROT's requirements.
 
Reference: Bairoch, A., & Apweiler, R. (2000). The SWISS-PROT protein sequence database and its supplement TrEMBL in 2000. Nucleic acids research, 28(1), 45–48. https://doi.org/10.1093/nar/28.1.45
