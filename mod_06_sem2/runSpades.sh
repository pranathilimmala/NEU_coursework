#!/usr/bin/env bash
# runSpades.sh

mkdir -p "rhodo/"

function Spades {
    spades.py \
    -1 Paired/SRR522244_1.fastq \
    -2 Paired/SRR522244_2.fastq \
    -o rhodo
}

Spades # runs the function Spades