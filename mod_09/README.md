# "BLAST and TransDecoder"

## Overview
Trinity is a technique for rapid and reliable de novo transcriptome reconstruction using RNA-Seq data. Normalization, Inchworm, Chrysalis, and Assembly are the four separate software modules that make up Trinity. Large RNA-Seq datasets can be processed by sequentially implementing each of these modules.
BLAST (basic local alignment search tool) is an algorithm and program for comparing primary biological sequence information, such as the amino-acid sequences of proteins or the nucleotides of DNA and/or RNA sequences.

## Author
Pranathi Limmala

## Date created
11/30/2022

## Required bash scripts for Module 09 assignment :

scripts/longOrfs_args.sh
scripts/blastPep_args.sh
scripts/pfamScan_args.sh
scripts/predictProteins_args.sh
scripts/alignPredicted_args.sh
sbatch_transdecoder.sh

## Results

alignPredicted_args.err
blastPep_args.err
longOrfs_args.err
longOrfs_args.log
pfamScan_args.err
pfamScan_args.log (too long to be uploaded on the repository)
predictProteins_args.err
predictProteins_args.log

## Methods

### Transcriptome assembly

Trinity: Trinity is a technique for rapid and reliable de novo transcriptome reconstruction using RNA-Seq data. Normalization, Inchworm, Chrysalis, and Assembly are the four separate software modules that make up Trinity. Large RNA-Seq datasets can be processed by sequentially implementing each of these modules.
With out a genome sequence, researchers can analyze transcriptomes using de novo assembly of RNA-seq data. This method can be applied, for example, to research on "non-model organisms" with ecological and evolutionary significance, cancer samples, or the microbiome.

Reference: Haas, B., Papanicolaou, A., Yassour, M. et al. De novo transcript sequence reconstruction from RNA-seq using the Trinity platform for reference generation and analysis. Nat Protoc 8, 1494–1512 (2013). https://doi-org.ezproxy.neu.edu/10.1038/nprot.2013.084

TransDecoder: TransDecoder is a utility developed and included with Trinity Links to an external site.. It assists in the identification of potential coding regions within reconstructed transcripts.
TransDecoder recognizes likely coding sequences based on the following criteria:
1)A minimum length open reading frame (ORF) in a transcript sequence.
2)A log-likelihood score similar to what is computed by the GeneID Links to an external site.software is greater than 0.
3)The above coding score is greatest when the ORF is scored in the first reading frame as compared to scores in the other 2 forward reading frames.
4)If a candidate ORF is found fully encapsulated by the coordinates of another candidate ORF, the longer one is reported. However, a single transcript can report multiple ORFs (allowing for operons, chimeras, etc.).
5)A Position-Specific Scoring Matrix (PSSM) is computed, trained, and used to refine the start codon prediction.

BLAST: Basic Local Alignment Search Tool (BLAST) searches for optimal local alignments between a query and a sequence database in a speed-optimized fashion. These start with an initial "word" of size "W" that scores above a threshold "T." From there, the alignment is extended in each direction seeking to find an alignment of the score "S" or greater. In some ways, these Words are similar to the k-mers we discussed previously. We simplify the initial search when we divide the query into smaller words. Adjusting the values for W, T, and S can change the sensitivity and speed of our search.

Reference: https://northeastern.instructure.com/courses/122305/pages/module-9-practice-blast-and-transdecoder
