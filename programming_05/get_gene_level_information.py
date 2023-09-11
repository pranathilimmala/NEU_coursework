# get_gene_level_information

"""
query the tissue expression for a given gene and species
"""

import argparse
import sys
import re
from assignment5 import config
from assignment5 import io_utils


def get_cli_args():
    """
    set up parser for command line, two argument are added
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')

    parser.add_argument('--host',
                        dest='HOST',
                        type=str,
                        help='Name of Host',
                        default='Human')

    parser.add_argument('-g', '--gene',
                        dest='GENE',
                        type=str,
                        help='Name of Gene',
                        default='TGM1')

    return parser.parse_args()


def _print_scientific_name():
    """
    print scientific names when the file cannot be opened
    """
    keyword_dict = config.get_host_keywords()
    scientific_name = keyword_dict.values()
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name\n")
    list_scientific = tuple(enumerate(set(scientific_name), 1))
    for index, name in list_scientific:
        print("{:>2}. {}".format(index, name.capitalize()))


def _print_common_name():
    """
    print common names when the file cannot be opened
    """
    keyword_dict = config.get_host_keywords()
    common_name = keyword_dict.keys()
    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")
    list_common = tuple(enumerate(sorted(set(common_name)), 1))
    for index, name in list_common:
        print("{:>2}. {}".format(index, name.capitalize()))


def _print_directories_for_hosts():
    """
    print statement when the file cannot be opened
    """
    print('\nEither the Host Name you are searching '
          'for is not in the database\n\n\
or If you are trying to use the scientific name '
          'please put the name in double quotes:\n\n\
"Scientific name"')
    _print_scientific_name()
    _print_common_name()


def update_host_name(temp_host_name):
    """
    modify input common name to scientific name
    """
    keyword_dict = config.get_host_keywords()
    if temp_host_name is None:
        temp_host_name = "Homo sapiens"

    if '_' in temp_host_name:
        temp_host_name = temp_host_name.split("_")[0].lower() + " " \
                         + temp_host_name.split("_")[1].lower()
        if temp_host_name in keyword_dict.keys():
            return keyword_dict.get(temp_host_name)
    if '_' not in temp_host_name:
        temp_host_name = temp_host_name.lower()
        if temp_host_name in keyword_dict.keys():
            return keyword_dict.get(temp_host_name)
    else:
        _print_directories_for_hosts()
        sys.exit()


def get_data_for_gene_file(gene_name):
    """
    extract expressed tissues list given by the gene name
    """
    args = get_cli_args()
    temp_host_name = args.HOST
    temp_gene_name = args.GENE
    if temp_host_name is None:
        host_name = "Homo_sapiens"
        gene_name = "TGM1"
    else:
        host_name = update_host_name(temp_host_name)
        gene_name = temp_gene_name
    file = "/".join((config.get_directory_for_unigene(),
                     host_name, gene_name + "." +
                     config.get_extension_for_unigene()))
    if io_utils.is_gene_file_valid(file):
        # using f-strings
        message = f"\nFound Gene {gene_name} for {host_name}"
    else:
        print(f"Not found\n\
        Gene {gene_name} does not exist for {host_name}. exiting now...")
        sys.exit()
    fh_in = io_utils.get_fh(file, "r")
    for line in fh_in:
        match = re.search(r'^EXPRESS\s+(\D+)', line)
        if match:
            tissue_string = match.group(1)
            temp_tissue_list = list(tissue_string.split(sep='|'))
            tissue_list = sorted([tissue.strip() for tissue in temp_tissue_list])
            return message, tissue_list


def print_host_to_gene_name_output(host_name="Homo_sapiens",
                                   gene_name="TGM1",
                                   tissue_list=get_data_for_gene_file("TGM1")):
    """
    print expressed tissues with index, define the default values
    """
    tissues_number = len(tissue_list)
    print(f"In {host_name}, There are {tissues_number} tissues that {gene_name} is expressed in:\n")
    for index, tissue in sorted(enumerate(tissue_list, 1)):
        print(f"{index:>2}. {tissue.capitalize()} ")


def main():
    """
    Business logic
    """
    args = get_cli_args()
    temp_host_name = args.HOST
    temp_gene_name = args.GENE
    host_name = update_host_name(temp_host_name)
    message, tissue_list = get_data_for_gene_file(temp_gene_name)
    print(message)
    print_host_to_gene_name_output(host_name, temp_gene_name, tissue_list)


if __name__ == '__main__':
    main()
