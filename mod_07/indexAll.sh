#!/usr/bin/env bash
# indexAll.sh
# Usage: bash indexAll.sh 1>results/indexAll.log 2>results/logs/indexAll.err &

#Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="data/trimmed/paired/"

#Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="data/trimmed/paired/"

function indexAll {
	#Loop through all the left-read fastq files in $fastqPath
	for leftInFile in $fastqPath*$leftSuffix
	do
    		#Remove the path from the filename and assign to pathRemoved
	    pathRemoved="${leftInFile/$fastqPath/}"
	    #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
	    sampleName="${pathRemoved/$leftSuffix/}"
	    #Print $sampleName to see what it contains after removing the path
	    echo $sampleName

	    samtools index \
		results/bam/$sampleName.sorted.bam\
		-o results/bai/$sampleName.bai \

	done

}
indexAll
