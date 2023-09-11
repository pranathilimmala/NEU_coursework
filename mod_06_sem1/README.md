# "To understand the Multiple Sequence Alignment"

## Overview
Module 06 assignment helps us to understand the basic concepts of MSA

## Author
Pranathi Limmala

# Date created
03/03/2023

## Running the module_06 assignment files as:

1) translate_apoe.py : This python file creates a fasta file named apoe_aa.fasta containing the APOE orthologs as amino acid sequences.

2) clustalAlign.sh : This script uses apoe_aa.fasta as input file and generates apoe_alignment.fasta. The clustalo command from clustal omega tool helps to perform MSA on the input .fasta file.

3) sbatch_clustalAlign.sh : This sbatch script asigns batch job on clustalAlign.sh script and gives apoe_alignment.fasta files as output file after performing MSA.

### Running the program by the following data file:
APOE_refseq_transcript.fasta

### Resulting fasta files
apoe_aa.fasta (Through translate_apoe.py)
apoe_alignment.fasta (sbatch_clustalAlign.sh)

# Version
initial version

# Resources
https://northeastern.instructure.com/courses/135893/pages/binf6309-module-6-practice-multiple-sequence-alignment?module_item_id=8539167
Chowdhury, Biswanath, and Gautam Garai. 2017. “A Review on Multiple Sequence Alignment from the Perspective of Genetic Algorithm.” *Genomics* 109 (5): 419–31...
