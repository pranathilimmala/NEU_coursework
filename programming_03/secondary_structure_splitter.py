"""secondary_structure_splitter"""

import argparse
import sys


def main():
    """To print output files"""
    args = get_cli_args()
    infile = args.infile

# output_files hardcoded
    outfile_1 = "pdb_protein.fasta"
    outfile_2 = "pdb_ss.fasta"

    # using get_filehandle() for one output file, two output files
    fh_in = get_filehandle(infile, "r")
    fh_out1 = get_filehandle(outfile_1, mode="w")
    fh_out2 = get_filehandle(outfile_2, mode="w")
    header, seqs = get_fasta_lists(fh_in)
    # print out the results
    num_proteins, num_ss = output_results_to_files(header, seqs)
    if num_proteins != num_ss:
        sys.stderr.write("Header and Sequence lists "
                         "size are different in size\n")
        sys.stderr.write("Did you provide a FASTA formatted file?")
    else:
        # writing this to STDERR
        sys.stderr.write("found {} protein sequences\n".format(num_proteins))
        sys.stderr.write("found {} ss sequences\n".format(num_ss))

    fh_in.close()
    fh_out1.close()
    fh_out2.close()


def get_filehandle(infile, mode):
    """To get the filehandle"""
    try:
        get_filehandle = open(infile, mode)
        return get_filehandle
    except OSError as error:
        print('file cannot be opened', infile)
        raise error
    except ValueError as error:
        print("wrong argument was passed for opening mode")
        raise error


def get_fasta_lists(fh_in):
    """To get fasta lists"""
    header_list = []
    seqs_list = []
    lines = fh_in.readlines()
    res = ''.join([str(elem) for elem in lines])
    line_list = res.split('>')
    for i in range(1, len(line_list)):
        if i % 2 == 0:
            seqs_list.append('>' + line_list[i])
        else:
            header_list.append('>' + line_list[i])

    return header_list, seqs_list


def _verify_lists(header_list, seqs_list):
    """Gives us the header list and sequence list"""
    if len(header_list) != len(seqs_list):
        sys.exit()
    else:
        return True


def output_results_to_files(num_proteins, num_ss):
    """To print output results for files"""
    return len(num_proteins), len(num_ss)


def get_cli_args():
    """ Just get the command line options using argparse
        @return: Instance of argparse arguments """

    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform splitting '
                    'on sequence and secondary structure')

    parser.add_argument('-i', '--infile',
                        dest='infile',
                        type=str,
                        help='file to parse in the fh_in to open',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
