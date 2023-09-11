"""
File: gene_names_from_chr21.py
Program to extract Gene Symbols and their
description from input files provided"""


import argparse
from assignment4 import io_utils


def main():
    """Business logic"""
    args = get_cli_args()
    infile = args.infile
    fh_in = io_utils.get_fh(infile, "r")
    my_dict = dict1(fh_in)
    while True:
        gene_symbol = input("Enter gene name of interest. Type quit to exit: ")
        if gene_symbol in my_dict:
            print(f"{gene_symbol} found! Description below:")
            print(f"{my_dict[gene_symbol]}")
        elif gene_symbol == 'quit':
            print(f"Thanks for querying the data.")
            break
        else:
            print("Not a valid gene name")


def dict1(fh_in):
    """Function to extract gene symbols and their descriptions"""
    my_dict = {}
    lines = fh_in.readlines()[1:]
    for line in lines:
        gene_symbol = line.strip().split("\t")[0]
        description = line.strip().split("\t")[1].lower()
        my_dict[gene_symbol] = description
        print(my_dict)
    return my_dict


def get_cli_args():
    """ Just get the command line options using argparse
      @return: Instance of argparse arguments"""
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt '
                                                 'and ask user '
                                                 'for a gene name')
    parser.add_argument('-i', '--infile', dest='infile',
                        type=str,
                        help='Path to file to open',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
