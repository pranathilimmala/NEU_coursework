# "To understand the concepts of loops, decisions and python script refactoring by programming"
## Overview
This module3 assignment helps us to understand the work flow of identifying nucleic acids and amino acids and thereby refactoring their scripts and performing different tests by importing functions in the refactored files. Basically giving us an overview of how loops and decision making in python programming actually occurs. In that order, we also can identify the length of kmers and their total kmer count in a given .fastq file or nucleic acid sequence.

## Author
Pranathi Limmala

# Date created
10/14/2022

## Running the assignment03_file.py as:
identify_sequence.py

identify_sequence_refactored.py

test_identify_sequence_refactored.py

count_aip_kmers.py
### Running the additional files as:
aip_kmers.txt

### Running the program by the following additional data files:
sequence1.txt
sequence2.txt
sequence3.txt

### Running the program by the following .fastq files:
Sample.R1.fastq

### Tests
### Test 1 
This test is run to identify whether the given sequence is a nucleicacid or an aminoacid.

Code: 

    for letter in sequence:
        if letter not in nucleic_acids:
            nt_check = False
    if nt_check == True:
        print("nucleicacid")
    else:
        print("aminoacid")


### Test 2

This test is run to avoid errors on the subject of case sensitivity.

    sequence = sequence3.readline().upper()

### Test 3
This is a negative test and throws an error in case of an invalid letter which is not in the list.

        if letter in noncoding_letters:
            print("Not an amino acid or a nucleic acid")
            sys.exit() # to exit the program
