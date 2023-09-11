#!/usr/bin/env python
""" The following code identifies the presence of nucleic acids
or amino acids in the given sequence file """

import argparse


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="identifies the presence of nucleic acids or amino acids)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get a list of text files to process
    parser.add_argument('file_list',  # variable to access this data later: args.file_list
                        metavar='FILE', # shorthand to represent the input value
                        help='Provide file name to process.'
                             'For multiple files, '
                             'separate their names with spaces.',
                        # message to the user, it goes into the help menu
                        type=str,
                        nargs="+" # will combine multiple textfile inputs into a list
                        )

    return parser.parse_args()
def identify_sequence(sequence3):
    """identifies the presence of nucleic acids or amino acids in sequence"""
    sequence = sequence3.readline().upper()
    # stores nucleic acid or amino acid in the variable sequence3
    # create a list of nucleicacids
    nucleic_acids = ['A', 'T', 'G', 'C', 'U']
    nt_check = True

    # Iterate over the txt file to check if not in list
    for letter in sequence:
        # The alphabets in the list below are not nucleic acids or amino acid
        noncoding_letters = ['B', 'J', 'O', 'X', 'Z']
        if letter in noncoding_letters:
            print("Not an amino acid or a nucleic acid")
            #sys.exit()
        if letter not in nucleic_acids:
            nt_check = False

    if nt_check is True:
        result = "nucleic acid"
    else:
        result = "amino acid"
    return result

if __name__ == "__main__":
    print(get_args())

# Open each file
for file in get_args().file_list: # Identify the sequence within the file
    print("\n", file, ":") # Print the filename, and its identity to the Terminal
    f = open(file)
    print(identify_sequence(f))
