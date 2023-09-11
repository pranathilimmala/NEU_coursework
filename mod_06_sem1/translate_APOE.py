#!/usr/bin/env bash
# translate_APOE.py

from Bio import SeqIO
from Bio.Seq import Seq

# Load the APOE transcript sequences from the original file
transcript_records = SeqIO.parse("APOE_refseq_transcript.fasta", "fasta")

# Create a new fasta file for the translated amino acid sequences
aa_records = []

# Iterate through each transcript sequence
for record in transcript_records:
    # Translate the nucleotide sequence to amino acids
    aa_seq = Seq(str(record.seq)).translate()
    
    # Create a new SeqRecord object for the translated sequence with the same header as the original
    aa_record = record
    aa_record.seq = aa_seq
    
    # Append the translated sequence to the list of amino acid sequences
    aa_records.append(aa_record)

# Write the amino acid sequences to a new fasta file
SeqIO.write(aa_records, "apoe_aa.fasta", "fasta")
