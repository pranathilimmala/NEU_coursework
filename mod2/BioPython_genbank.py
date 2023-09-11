#!/usr/bin/env bash

from Bio import Entrez, SeqIO


"""Problem: 3
BioPython_genbank.py"""


# Set the email for Entrez
Entrez.email = "my_email@example.com"

# List to store the Seq objects
seq_list = []

# Retrieve a sequence from GenBank
# by gi (id) for 515056
handle = Entrez.efetch(db="nucleotide", id="515056",
                       rettype="gb", retmode="text")
record = SeqIO.read(handle, "gb")
seq_list.append(record)
handle.close()

# Retrieve a sequence from GenBank by
# accession (id) for J01673.1
handle = Entrez.efetch(db="nucleotide", id="J01673.1",
                       rettype="gb", retmode="text")
record = SeqIO.read(handle, "gb")
seq_list.append(record)
handle.close()

# Print out the sequences
for record in seq_list:
    print(record.seq)

# Print out the type, location, and
# strand of each feature
for record in seq_list:
    for feature in record.features:
        print("Type:", feature.type)
        print("Location:", feature.location)
        print("Strand:", feature.strand)
        print("---")
