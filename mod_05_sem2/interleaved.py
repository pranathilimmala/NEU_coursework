"""Interleave mate-pair sequences into a single file"""

import argparse  # for command-line argument parsing
from datetime import datetime  # for getting current timestamp
from Bio import SeqIO  # for reading/writing FASTQ/A files
import itertools

def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Interleave mate-pair FASTQ sequences into a single FASTA file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # To get the first mate FASTQ file name (or path)

    # T0 add argument to get the second mate FASTQ file name

    # Get output FASTA file name
    parser.add_argument('-o', '--output',  # variable to access this data later: args.output
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide the path for the output FASTA file.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-1', '--firstArgument',
						help='First argument for mate1',required=True,
						default="first3reads_Aip02.R1.fastq")
    parser.add_argument('-2', '--secondArgument',
						help='Second argument for mate2',required=True,
						default="first3reads_Aip02.R2.fastq")

    # extra arguments to help us format our log file output
    parser.add_argument('--logFolder',  # variable to access this data later: args.logFolder
                        help='Provide the folder for log files.', # message to the user, it goes into the help menu
                        type=str,
                        default="C:\\Users\\Lenovo\\PycharmProjects\\pythonProject"
								"\\pranathi_limmala\\6308\\assignment_05\\")
    parser.add_argument('--logBase',  # variable to access this data later: args.logBase
    					help='Provide the base for the log file name',
    					type=str,
    					default=parser.prog)  # get the name of the script

    return(parser.parse_args())


def pathLogFile(logFolder, logBase):
	"""Return a log file path and name using the current time and script name."""
	timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")  # get current time in YYYY-MM-DD-HHMM
	return(f"{logFolder}{timestamp}_{logBase}.log")


def interleave(mate1, mate2):
	"""Return list of interleaved SeqRecords.

	Assumes mate1 and mate2 inputs are SeqIO.parse iterator objects.
	"""
	# The first parameter to SeqIO.parse is the file location
	# The second parameter is the file type
	interleaved = []
	for l, r in zip(mate1, mate2):
		interleaved.append(l)
		interleaved.append(r)
	SeqIO.write(interleaved, "top24_Aip02.interleave", "fasta")

	# interleaved list with interleaved SeqRecord objects
	return interleaved

def logInterleave(args):
	"""Create log of Interleave progress."""
	args = get_args()
	logFile = pathLogFile(args.logFolder, args.logBase)

	with open(logFile, 'w') as log:
		log.write(f"Running interleaved.py on {datetime.now()}\n")

		# TODO log the two mate files and the output file
		log.write("\n**** Summary of arguments ****")
		log.write(f"\nMate1 file: {args.firstArgument}")
		log.write(f"\nMate2 file: {args.secondArgument}")
		log.write(f"\nOutput file: {args.output}")
		log.write("\n\n")  # add some space between argument data and the rest of the log

		# To add log lines and commands to do the following steps.
		#   Log the file
		# Can find my Logfile found in module_05 repository in scripts

		log.write(f"\nPreparing input data - {datetime.now()}")
		log.write(f"\nCalling interleave() to process the data - {datetime.now()}")
		mate1 = SeqIO.parse(args.firstArgument, "fastq")
		mate2 = SeqIO.parse(args.secondArgument, "fastq")
		interleave(list(mate1), list(mate2))

		log.write(f"\nOutputting results to file - {datetime.now()}")
		log.write(f"\nScript has finished at {datetime.now()}")



if __name__ == "__main__":
	logInterleave(get_args())  # pass arguments directly into the primary function
