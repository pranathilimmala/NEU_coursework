#!/usr/bin/env bash
# analyzeTrinity.sh
# Usage: bash scripts/analyzeTrinity.sh 1>results/trinity_de_novo_stats.txt 2>results/logs/analyzeTrinity.err

TrinityStats.pl results/trinity_de_novo/Trinity.fasta
