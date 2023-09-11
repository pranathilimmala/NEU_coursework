#!/usr/bin/env bash
# alignPredicted_args.sh
# Usage: bash scripts/alignPredicted_args.sh 1>results/logs/alignPredicted_args.log 2>results/logs/alignPredicted_args.erro

blastp -query $1 -db $2 -outfmt "6 qseqid sacc qlen slen length nident pident evalue stitle"  -evalue 1e-10 -num_threads 4  

