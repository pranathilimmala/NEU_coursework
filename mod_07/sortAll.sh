#!/usr/bin/env bash
# sortAll.sh
# Usage: bash scripts/sortAll.sh 1>results/logs/sortAll.log 2>results/logs/sortAll.err &

#Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="data/trimmed/paired/"

#Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="data/trimmed/paired/"


function sortAll {
	#Loop through all the left-read fastq files in $fastqPath
	for leftInFile in $fastqPath*$leftSuffix
	do
    		#Remove the path from the filename and assign to pathRemoved
	    pathRemoved="${leftInFile/$fastqPath/}"
	    #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
	    sampleName="${pathRemoved/$leftSuffix/}"
	    #Print $sampleName to see what it contains after removing the path
	    echo $sampleName

		samtools sort \
		results/$sampleName.sam \
		-o results/bam/$sampleName.sorted.bam \

	done
}
sortAll
