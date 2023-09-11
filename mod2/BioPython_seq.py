#!/usr/bin/env bash

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


"""Problem: 2
BioPython_seq.py"""

seq = Seq("aaaatgggggggggggccccgtt")
my_dna_record = SeqRecord(seq,
                          id="#12345",
                          description="example 1",
                          annotations={"molecule_type":
                                           "generic_dna"})

# Write the SeqRecord to a GenBank file
SeqIO.write(my_dna_record, "BioPython_seq.gb", "genbank")
