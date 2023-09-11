#!/usr/bin/env bash

from Bio import SeqIO
import sys


"""Problem: 4
BioPython_seqio.py"""


# Define the reverse complement function
def reverse_complement(sequence):
    complement_map = {'A': 'T', 'C': 'G',
                      'G': 'C', 'T': 'A'}
    return "".join([complement_map[base]
                    for base in sequence[::-1]])

# Read the input FASTA file and output
# the reverse complement FASTA file
def write_reverse_complement(input_file, output_file):
    with open(output_file, "w") as f:
        for record in SeqIO.parse(input_file,
                                  "fasta"):
            reversed_seq = reverse_complement(str(record.seq))
            f.write(">" + record.id + "\n" +
                    reversed_seq + "\n")

# Read the input and output filenames
# from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]

# Call the main function
if __name__ == '__main__':
    write_reverse_complement(input_file, output_file)
