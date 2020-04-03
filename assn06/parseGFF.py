#! /usr/bin/env python3
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('gff')
parser.add_argument('fsa')
args = parser.parse_args()
with open(args.gff) as input:
    GeneList = []
    for line in input:
        line = line.rstrip("\n")
        fields = line.split("\t")
        attributes = fields[8].split(";")
        gene_fields = attributes[0].split("Gene ")
        GeneList.append(gene_fields[1])
        for gene in sorted(GeneList): print(gene)
