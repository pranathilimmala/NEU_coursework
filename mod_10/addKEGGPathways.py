#!/usr/bin/env python
"""Template script: Duplicate word n times.

Customize the framework below for your particular need.
"""

import argparse
import requests


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Your script description (often top line of script's DocString; eg. Duplicate word n times)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Create a sequential argument (eg. it has to come in the order defined)
    parser.add_argument('word', # name of the argument, we will later use args.word to get this user input
                        metavar='WORD', # shorthand to represent the input value
                        help='Word to duplicate', # message to the user, it goes into the help menu
                        type=str, # type of input expected, could also be int or float
                        default='Hello', # default option if no input is given by the user
                        #required=False # whether this input must be given by the user, could also be True
                        )
    # Create a flagged argument (eg. input comes after a short "-i" or long "--input" form flag)
    parser.add_argument('-n', '--number', # name of the argument, we will later use args.number to get this user input
                        metavar='INT', # shorthand to represent the input value
                        help='Number of times to duplicate', # message to the user, it goes into the help menu
                        type=int, # type of input expected, could also be int or float
                        default=1, # default option if no input is given by the user
                        #required=False # whether this input must be given by the user, could also be True
                        )
    # create new values input file
    parser.add_argument('-new', '--new_value_input_file',  # name of the argument, we will later use args.number to get this user input
                        metavar='INT',  # shorthand to represent the input value
                        help='input_file',  # message to the user, it goes into the help menu
                        type=str,  # type of input expected, could also be int or float
                        default=1,  # default option if no input is given by the user
                        # required=False # whether this input must be given by the user, could also be True
                        )
    # create output file
    parser.add_argument('-o', '--output',  # name of the argument, we will later use args.number to get this user input
                        metavar='INT',  # shorthand to represent the input value
                        help='output_file',  # message to the user, it goes into the help menu
                        type=str,  # type of input expected, could also be int or float
                        default=1,  # default option if no input is given by the user
                        # required=False # whether this input must be given by the user, could also be True
                        )
    # create evalue list
    parser.add_argument('-e', '--eval',  # name of the argument, we will later use args.number to get this user input
                        metavar='INT',  # shorthand to represent the input value
                        help='threshold eval',  # message to the user, it goes into the help menu
                        type=str,  # type of input expected, could also be int or float
                        default=1,  # default option if no input is given by the user
                        # required=False # whether this input must be given by the user, could also be True
                        )

    return(parser.parse_args())


def name_of_function(word, n=1):
    """What the function does (eg. Return duplicated word.)"""

    # Do things with the parameters above
    # to get to defining the "thing" you will return
    duplicated_word = word * n

    return(duplicated_word)


def getUniProtFromBlast(blast_line, threshold):
    """Return UniProt ID from the BLAST line if the evalue is below the threshold.

    Returns False if evalue is above threshold.
    """
    cleaned_line = blast_line.strip()
    blast_fields = cleaned_line.split("\t")
    # print(blast_fields)
    if float(blast_fields[7]) < float(threshold):
        return(blast_fields[1])
    else:
        return(False)


def loadKeggPathways():
    """Return dictionary of key=pathID, value=pathway name from http://rest.kegg.jp/list/pathway/ko

    Example: keggPathways["path:ko00564"] = "Glycerophospholipid metabolism"
    """
    keggPathways = {}
    result = requests.get('https://rest.kegg.jp/list/pathway/ko')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggPathways[fields[0]] = fields[1]
    return(keggPathways)


def getKeggGene(uniprotID):
    """Return a list of KEGG organism:gene pairs for a provided UniProtID."""
    keggGenes = []
    result = requests.get(f'https://rest.kegg.jp/conv/genes/uniprot:{uniprotID}')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            str_entry = entry.decode(result.encoding)  # convert from binary value to plain text
            fields = str_entry.split("\t")
            keggGenes.append(fields[1])  # second field is the keggGene value
    return(keggGenes)


def getKeggOrthology(keggGenes):
    """write yourself to return the
    KEGG Orthology ID (e.g., ko:K01108)
    for a provided KEGG ID (e.g., 'hsa:4534');
    model it on getKeggGenes() function"""
    keggOrthology = []
    result = requests.get(f'https://rest.kegg.jp/link/ko/{keggGenes}')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            str_entry = entry.decode(result.encoding)
            fields = str_entry.split("\t")
            keggOrthology.append(fields[1])
    return(keggOrthology)


def getKeggPathIDs(keggOrthology):
    """write yourself to return the KEGG Path
    IDs (e.g., path:ko01100, path:ko00562)
    for a provided KEGG Orthology ID
    (e.g., ko:K01108); model it on getKeggGenes()
    function"""

    keggPathIDs = []
    result = requests.get(f'https://rest.kegg.jp/link/pathway/{keggOrthology}')
    for entry in result.iter_lines():
        if entry.decode(result.encoding):
            # print("decoded is", entry.decode(result.encoding))
            str_entry = entry.decode(result.encoding)
            fields = str_entry.split("\t")
            # if fields is empty, then stop executing
            if not fields[1].startswith("path:map"):
                keggPathIDs.append(fields[1])
    return(keggPathIDs)


def addKEGGPathways():
    """write yourself to tie all the other
    functions together to accomplish the
    assignment prompt"""
    keggPathways = loadKeggPathways()
    blastFile = open("/scratch/limmala.p/module-10-pranathibinf/data/alignPredicted.txt", "r")
    outputFile = open("/scratch/limmala.p/module-10-pranathibinf/results/alignPredicted.txt", "w")
    count = 0
    for line in blastFile:
        line = line.strip()
        count += 1
        if count % 100 == 0:
            print(f"count is {count}")
        uniprotID = getUniProtFromBlast(line, 1e-50)
        # print("Uniprot id", uniprotID)
        if uniprotID:
            # get the KEGG gene IDs
            keggGenes = getKeggGene(uniprotID)
            if keggGenes:
                # print("kegggenes is", keggGenes[0])
                keggOrthology = getKeggOrthology(keggGenes[0])
                # print("ortho is", keggOrthology)
                if keggOrthology:
                    keggPathIDs = getKeggPathIDs(keggOrthology[0])
                    if keggPathIDs:
                        #print("path is", keggPathIDs)
                        for pathID in keggPathIDs:
                            # print("writing", pathID)
                            f_line = line+"\t"+keggOrthology[0]+"\t"+pathID+"\t"+keggPathways[pathID]+"\n"
                            outputFile.write(f_line)

    blastFile.close()
    outputFile.close()


if __name__ == '__main__':
    args = get_args()
    result = name_of_function(args.word, args.number)
    addKEGGPathways()
    # Output the result
    print(result)

    # or just print the function if this is all we are doing:
    #print(name_of_function(args.word, args.number))
