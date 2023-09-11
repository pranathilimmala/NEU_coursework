'''To calculate the average weight of the protein sequence'''

import sys # to exit the program using sys.exit


def main():
    '''The protein sequence'''
    seq_name = input("Please enter a name for the DNA sequence: ")
    print("Your sequence name is", seq_name)
    len_seq = float(input("Please enter the length of the sequence: "))

    if len_seq % 3 != 0: # to throw an error code
        print("\n\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)
        sys.exit(1)

    print("The length of the DNA sequence is: ", len_seq)
    protein_length = len_seq / 3
    print("The length of the decoded protein is: ", protein_length)
    print("The average weight of the protein sequence is: ", (protein_length * 110)/ 1000)


if __name__ == '__main__':
    main()
