"""Business Logic"""

import argparse
import sys


def main():
    args = get_cli_args()
    infile = args.infile

    outfile_1 = "pdb_protein.fasta"
    outfile_2 = "pdb_ss.fasta"
    ntcount_file = "statistic.txt"

    # using get_filehandle() for one output file, two output files
    fh_in = get_filehandle(infile, "r")
    fh_out = get_filehandle(ntcount_file, mode="w")
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
        sys.stderr.write(f'found {num_proteins} protein sequences\n')
        sys.stderr.write(f'found {num_ss} ss sequences\n')

    output_seq_statistics(header, seqs, fh_out)
    fh_in.close()
    fh_out1.close()
    fh_out2.close()
    fh_out.close()


def get_filehandle(infile, mode):
    """To get file handle"""
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
    seq = ""
    for i in lines:
        if '>' in i:
            if seq != "":
                seqs_list.append(seq)
                seq = ""
            header_list.append(i)
            continue
        else:
            seq = seq+i.strip()
    seqs_list.append(seq)

    return header_list, seqs_list


def _verify_lists(header_list, seqs_list):
    """To get header list and seqs list"""
    if len(header_list) != len(seqs_list):
        sys.exit()
    else:
        return True


def output_results_to_files(num_proteins, num_ss):
    """To print output results to files"""
    return len(num_proteins), len(num_ss)


def _get_num_nucleotides(char, seq):
    """To get number of nucleotide bases"""
    a = {'A', 'G', 'C', 'T', 'N'}
    if char not in a:
        sys.exit("Did not code this condition")
    return seq.count(char)


def _get_ncbi_accession(header):
    """To get accession numbers"""
    return header.strip().split(" ")[0]


def output_seq_statistics(header, seq, fh_out):
    """To get output of seq statistics"""
    for i in range(len(header)):
        print("**********"+_get_ncbi_accession(header[i])+"*******")
        print("A: "+str(seq[i].count('A')))
        print("C: " + str(seq[i].count('C')))
        print("T: " + str(seq[i].count('T')))
        print("G: " + str(seq[i].count('G')))
        print("N: " + str(seq[i].count('N')))
        print("Length: " + str(seq[i].count('A') +
                               seq[i].count('C') +
                               seq[i].count('T') +
                               seq[i].count('G')))
        length = (seq[i].count('A') +
                  seq[i].count('C') +
                  seq[i].count('T') +
                  seq[i].count('G'))
        print("GC%: " + str((seq[i].count('C') +
                             seq[i].count('G')) / length * 100))


def get_cli_args():
    """
        Just get the command line options using argparse
        @return: Instance of argparse arguments
        """

    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform '
                    'splitting on sequence and secondary structure')

    parser.add_argument('-i', '--infile',
                        dest='infile',
                        type=str,
                        help='file to parse in the fh_in to open',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()
    args = get_cli_args()
