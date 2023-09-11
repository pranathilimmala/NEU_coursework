#!/usr/bin/env bash
# blastPep_args.sh
# Usage: bash scripts/blastPep_args.sh <SWISSPROT_DB> <result folder> 1>results/blastPep.outfmt6 2>results/logs/blastPep.err

# <SWISSPROT_DB> might be results/trinity_de_novo.transdecoder_dir/longest_orfs.pep
# <result folder> might be /work/courses/BINF6308/inputFiles/blastDB/swissprot

blastp -query  $1 -db $2 -max_target_seqs 1  -outfmt 6  -evalue 1e-5  -num_threads 4
