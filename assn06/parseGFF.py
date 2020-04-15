#! /usr/bin/env python3
import argparse
import csv

#functions
def gc(subseq):
    return subseq.upper().count("G") + subseq.upper().count("C"))/len(subseq)

# inputs
parser = argparse.ArgumentParser()
parser.add_argument('gff', help="the gff file")
parser.add_argument('fsa', help="the fasta file")
args = parser.parse_args()
genome = SeqIO.read(args.fsa, "fasta")
fullseq = genome.seq

# operations
with open(args.gff) as input:
    input.read = csv.reader(input, delimiter = "\t")
    for line in input.read:
        if(line[2] == "CDS"):
            start = int(line[3])
            end = int(line[4])
            subseq = fullseq[(start-1):(end)]
            GC = gc(subseq)
            print(round(GC, 2))
