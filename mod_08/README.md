# "Transcriptome assembly with Trinity

## Overview
Trinity is a technique for rapid and reliable de novo transcriptome reconstruction using RNA-Seq data. Normalization, Inchworm, Chrysalis, and Assembly are the four separate software modules that make up Trinity. Large RNA-Seq datasets can be processed by sequentially implementing each of these modules.

## Author
Pranathi Limmala

## Date created
11/21/2022

## Required bash scripts for Module 08 assignment :
mergeAll.sh

runTrinity.sh

analyzeTrinity.sh

trinityDeNovo.sh

analyzeTrinityDeNovo.sh

sbatch_trinity.sh


## Results
trinity_guided_stats.txt

trinity_de_novo_stats.txt

batch-trinity-32685819.output

## Methods

### Trimmomatic

Trimmomatic is a Java-based quality trimmer that uses a sliding window to determine where quality scores have dropped below a specified threshold. In addition to trimming based on quality scores, Trimmomatic also removes any adapter sequences from the reads. Sometimes during library preparation, extra copies of adapters get attached to the beginning or end of the cDNA fragments. These adapters are what sequencers use to immobilize DNA fragments on the flow cell, but you don't want them treated as actual sequence data. If included in your sequence data, they confuse assemblers and read aligners.
Using this bash script to trim our paired-end FASTQ reads.

Reference:
https://northeastern.instructure.com/courses/122305/pages/module-7-practice-aligning-rnaseq-reads-to-a-reference

### samtools
Large nucleotide sequence alignments can be stored in the SAM (Sequence Alignment/Map) format.

The SAM format intends to be one that:
1)It is adaptable enough to hold all alignment data produced by different alignment programs.
2)Easy to generate using alignment software or to convert from current alignment formats has a small file size.
3)Enables the majority of alignment operations to be performed on a stream without having to load the entire alignment into memory.
4)Allows for rapid retrieval of all reads aligning to a locus by allowing the file to be indexed by genomic location.

Sorting, merging, indexing, and producing alignments in a per-position format are just a few of the tools offered by SAM Tools for handling alignments in the SAM format.

The initial version first appeared online 12 years ago, and since then, it has been updated and improved with numerous new functions.

Reference:
Danecek, P., Bonfield, J. K., Liddle, J., Marshall, J., Ohan, V., Pollard, M. O., Whitwham, A., Keane, T., McCarthy, S. A., Davies, R. M., & Li, H. (2021). Twelve years of SAMtools and BCFtools. Gigascience, 10(2). https://doi.org/10.1093/gigascience/giab008


### GMAP Database and GSNAP alignment

cDNA sequences can be mapped and aligned to a genome using the standalone application GMAP. The program offers quick batch processing of large sequence sets while mapping and aligning a single sequence with a small startup time and memory demand. Without using probabilistic splice site models, the program produces precise gene structures even in the presence of significant polymorphisms and sequence mistakes. The program's methodology includes oligomer chaining for approximate alignment, sandwich DP for splice site detection, microexon identification with statistical significance testing, and minimal sampling for genomic mapping.

Reference:
Wu, T. D., & Watanabe, C. K. (2005). GMAP: a genomic mapping and alignment program for mRNA and EST sequences. BIOINFORMATICS, 21(9), 1859–1875. https://doi.org/10.1093/bioinformatics/bti310

With improvements in biological methods, the programs GMAP and GSNAP—used to align RNA-Seq and DNA-Seq datasets to genomes—have developed to handle longer reads, bigger volumes of data, and novel kinds of biological tests. The genomic representation has been enhanced to support large genomes with more than four billion base pairs, compressed genomic hash tables with fast access using SIMD instructions, and enhanced suffix arrays (ESAs) with novel data structures for fast access. Linear genomes that can compare sequences using SIMD instructions are also now included. A greedy match-and-extend algorithm using suffix arrays, segment chaining using genomic hash tables, diagonalization using segmental hash tables, and nucleotide-level dynamic programming techniques using SIMD instructions and doing away with the need for F-loops are some improvements to the algorithms. Standardization of indel positions, handling of ambiguous splicing, clipping and merging of overlapping paired-end reads, alignments to circular chromosomes, and alternative scaffolds are all improvements to the programs' functionality. By incorporating the programs use into R/Bioconductor packages like gmapR and HTSeqGenie, the programs were modified for use in pipelines, and these pipelines aided in the discovery of a variety of biological phenomena.

The basic steps for running GSNAP are to:
1)Quality trim the reads
2)Build an index of the reference genome using the gmap_build command
3)Build a database of the known introns from the GFF3 file using the iit_store command
4)Run the alignment using the gsnap command.

Reference:
Wu, T. D., Reeder, J., Lawrence, M., Becker, G., & Brauer, M. J. (2016). GMAP and GSNAP for Genomic Sequence Alignment: Enhancements to Speed, Accuracy, and Functionality. Statistical Genomics, 1418, 283–334. https://doi.org/10.1007/978-1-4939-3578-9_15


### Transcriptome assembly
Trinity: Trinity is a technique for rapid and reliable de novo transcriptome reconstruction using RNA-Seq data. Normalization, Inchworm, Chrysalis, and Assembly are the four separate software modules that make up Trinity. Large RNA-Seq datasets can be processed by sequentially implementing each of these modules.
With out a genome sequence, researchers can analyze transcriptomes using de novo assembly of RNA-seq data. This method can be applied, for example, to research on "non-model organisms" with ecological and evolutionary significance, cancer samples, or the microbiome.

Reference: Haas, B., Papanicolaou, A., Yassour, M. et al. De novo transcript sequence reconstruction from RNA-seq using the Trinity platform for reference generation and analysis. Nat Protoc 8, 1494–1512 (2013). https://doi-org.ezproxy.neu.edu/10.1038/nprot.2013.084
