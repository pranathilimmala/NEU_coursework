# "To determine the first orf of the given RNA sequence and to find the protein of the input file sequence"

## Overview
This helps us to understand the concept of usage of Biopython and object oriented programming involved for finding orfs and determining the protein sequences.

## Author
Pranathi Limmala

# Date created
10/20/2022

## Running the assignment03_file.py as:
translate_first_orf.py

test_translate_first_orf.py

### Running the additional files as:
("/work/courses/BINF6308/data_BINF6308/Module4/dmel-all-chromosome-r6.17.fasta")


### Tests
### Test 1 
To find the first orf of the input sequence:

    try:
        orf_first = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
        #orf_f = orf_first.group()
        orf = Seq(orf_first)
        print(orf)

    except AttributeError:
        orf = ""

    return Seq(orf)


### Test 2
To find the protein / translated first orf of the input file

    rna = Seq(dna).transcribe()
    orf = find_first_orf(rna)
    translate_first_orf = orf.translate()

    return translate_first_orf

