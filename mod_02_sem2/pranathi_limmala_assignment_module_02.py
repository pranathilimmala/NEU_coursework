'''To identify the presence of nucleic acids or amino acids'''

import sys # to exit the program using sys.exit


def main():
    '''Set the file path for the sequence3 selected'''
    sequence3 = open("C:\\Users\\Lenovo\\PycharmProjects\\python"
                     "Project\\Pranathi_Limmala\\6308\\Pranathi_Limmala_module_02_6308.txt")
    sequence = sequence3.readline().upper()

    # create a list of nucleicacids
    nucleic_acids = ['A', 'T', 'G', 'C', 'U']

    nt_check = True

    # Iterate over the txt file to check if not in list
    for letter in sequence:
        # The alphabets in the list below are not nucleic acids or amino acid
        noncoding_letters = ['B', 'J', 'O', 'X', 'Z']
        if letter in noncoding_letters:
            print("Not an amino acid or a nucleic acid")
            sys.exit()
        if letter not in nucleic_acids:
            nt_check = False

    if nt_check is True:
        print("nucleicacid")
    else:
        print("aminoacid")



if __name__ == '__main__':
    main()
