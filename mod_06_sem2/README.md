# "To create a genome assembly and thereby assess its quality using different bioinformatic tools"

## Overview
This assignment is all about understanding the genome assembly and performing a quality check accordingly by downloading FASTA sequence of the given organism under study. All of this performed on Northeastern's OnDemand Discovery terminal.

## Author
Pranathi Limmala

## Date created
11/7/2022

## Required bash scripts for Module 06 assignment :
getNGS.sh

trim.sh

runSpades.sh

runQuast.sh

sbatch_assembleGenome.sh

### Additional files:
Spades.py

Quast.py
 
#### quast_results
quast.log

report.pdf

#### spades_test
spades.log

## Methods

### getNGS.sh

From the script, the fasterq-dump tool extracts data in FASTQ- or FASTA-format from SRA-accessions. It is a commandline-tool that is available for Linux, macOS, and Windows. Fasterq-dump is the successor to the older fastq-dump tool, but faster.

### trim.sh

Trimmomatic is a Java-based quality trimmer that uses a sliding window to determine where quality scores have dropped below a specified threshold. In addition to trimming based on quality scores, Trimmomatic also removes any adapter sequences from the reads. Sometimes during library preparation, extra copies of adapters get attached to the beginning or end of the cDNA fragments. These adapters are what sequencers use to immobilize DNA fragments on the flow cell, but you don't want them treated as actual sequence data. If included in your sequence data, they confuse assemblers and read aligners.
Using this bash script to trim our paired-end FASTQ reads.

### runSpades.sh

This bash script is used to assemble the Rhodobacter genome using just the quality-trimmed reads.

### runQuast.sh

To run a basic analysis report for your genome and determine the N50 for our assembly.

### sbatch_assembleGenome.sh

This is for assigning a batch job to perform for crating our genome assembly.


## Analysis of the report_6308.pdf

From the quast_results we can infer that the N50 value is 1000 and to test the quality, Quast is that Bioinformatics tool we have used here. Although larger assembly values are better, other parameters do play an important role for the overall quality check. This is only known later when the genome assembly is actually used in further procedures involving genomics.
Have also tried to resolve this issue but we get the same N50 value somehow. 

