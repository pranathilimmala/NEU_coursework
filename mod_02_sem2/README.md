# To identify the presence of nucleic acids or amino acids

## Overview 
This program helps us to identify if the sequence given contains nucleic acids or amino acids.

## Author
Pranathi Limmala

## Date created
10/05/2022

## Running the sequence_file.py as:
pranathi_limmala_assignment_module_02.py

## Tests
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
            
    
