"""To determine the first orf of the given RNA sequence and to find the protein of the input file sequence
"""

import argparse
import re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="TODO: say what the script does.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\d{1}\D*$')  # default works for Drosophila chromosomes

    return(parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    try:
        orf_first = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
        orf = Seq(orf_first)

    except AttributeError:
        orf = ""

    return Seq(orf)

def translate_first_orf(dna):
    """It translates RNA to Protein

    Assumes input sequences is a Bio.Seq object.
    """
    # Transcribe the DNA, find the first ORF, translate said ORF
    rna = Seq(dna).transcribe()
    orf = find_first_orf(rna)
    translate_first_orf = orf.translate()

    return translate_first_orf


if __name__ == "__main__":
    args = get_args()

    for record in SeqIO.parse(args.filename, "fasta"):
        if re.match("^\d{1}\D*$", record.id):
            print(f"{record.id}: \t{translate_first_orf(record.seq)}")

    # use SeqIO to get the records in the fasta file provided by the command-line input
    # if the FASTA record's ID matches the regex pattern,
    #   then print out its record ID then a tab space then the translated first ORF
   