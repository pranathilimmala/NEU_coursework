"""
File : find_common_cats.py
Program to extract gene, categeories with
their description from the input files provided
"""

import argparse
from assignment4 import io_utils


def main():
    """Business logic"""
    args = get_cli_args()
    infile = args.infile
    fh_in = io_utils.get_fh(infile, "r")
    my_dict3 = dict2(fh_in)
    output = "OUTPUT//categories.txt"
    with open(output, 'w') as file:
        file.write('%s\t:\t%s\n' % ('Category', 'Description'))
        for key, value in my_dict3:
            file.write('%s\t:\t%s\n' % (key, value))


def dict2(fh_in):
    """The function dict2 is for extracting gene,
    categeories with their descriptions
    simultaneously"""
    my_dict2 = {}
    my_dict3 = ''
    lines = fh_in.readlines()[1:]
    i = 0
    for line in lines:
        text = line.strip().split("\t")
        if len(text) == 2:
            continue
        cat = float(text[2])
        description = text[1].lower()
        my_dict2[i] = (cat, description)
        i += 1
        my_dict3 = sorted(my_dict2.values())
    return my_dict3


def get_cli_args():
    """ Just get the command line options using argparse
    @return: Instance of argparse arguments"""

    parser = argparse.ArgumentParser(description='Open '
                                                 'chr21_genes_categories.txt '
                                                 'sort them in '
                                                 'ascending order')
    parser.add_argument('-i1', '--infile', dest='infile',
                        type=str,
                        help='Path to file to open',
                        required=True)
    parser.add_argument('-i2', '--second argument',
                        help='second argument', required=True,
                        default="chr21_genes_categeories.txt")
    return parser.parse_args()


if __name__ == '__main__':
    main()
