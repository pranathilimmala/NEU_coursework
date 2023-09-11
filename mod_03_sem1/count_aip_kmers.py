# !/usr/bin/env python
# read_by_line_using_for_v2.py
# Open a sample fastq file for reading.

# Import re to support regular expressions in this program.
import re

# Open a sample fastq file for reading
filename = "C:\\Users\\Lenovo\\PycharmProjects\\" \
           "pythonProject\\pranathi_limmala\\6308\\assignment_03\\Sample.R1.fastq"

with open(filename, 'r') as read_sample:
    for line in read_sample:
        # get rid the hidden new line character
        line = line.rstrip()

        if re.match('^[ATGCN]+$', line):
            # Print the line
            print(line)
# get_one_kmer.py
            seq = 'GCCGGCCCTCAGACAGGAGTGGTCCTGGATG'
            kmer = seq[0:7]
            print(kmer)
            # count kmers
            kmer_length = 6

            # Initialize a k-mer dictionary
            kmer_dictionary = {}

            stop = len(seq) - kmer_length + 1
            # Iterate over the positions
            for start in range(0, stop):
                # Get the substring at a specific start and end position
                kmer = seq[start:start + kmer_length]

                # See if it's in the dictionary
                if kmer in kmer_dictionary:
                    # Add one to the count
                    kmer_dictionary[kmer] += 1
                else:
                    # It's not in the dictionary so add with a count of 1
                    kmer_dictionary[kmer] = 1

            # Print the number of keys in the dictionary
            print(len(kmer_dictionary))

# get_all_kmers2.py
seq = 'GCCGGCCCTCAGACAGGAGTGGTCCTGGATG'
kmer_length = 6
# Calculate the stop before the loop to improve efficiency.
stop = len(seq) - kmer_length + 1
for start in range(0, stop):
    kmer = seq[start:start + kmer_length]
    print(kmer)
