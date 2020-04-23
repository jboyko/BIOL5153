#! /usr/bin/env python3

import argparse
import csv
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def get_args():
    # create an argument parser object
    parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

    # add positional arguments
    parser.add_argument("gff",   help="name of the GFF file")
    parser.add_argument("fasta", help="name of the FASTA file")

    # parse the arguments
    return parser.parse_args()


def parse_fasta():
    # read and parse the FASTA file
    return SeqIO.read(args.fasta, 'fasta')


def parse_gff(genome):
    # read GFF file, line by line
    with open(args.gff, 'r') as gff_file:
        
        # create a csv reader object
        reader = csv.reader(gff_file, delimiter="\t")
        
        # gene dic
        gene_dic = dict()
        exon_dic = dict()
        
        for line in reader:
            # skip blank lines
            if not line:
                continue

            else:
                organism     = line[0].replace(" ", "_")
                feature_type = line[2]
                start        = int(line[3])
                end          = int(line[4])
                strand       = line[6]
                attributes   = line[8]

                # test whether this is a CDS feature
                # if it is a CDS feature, then extract the substring/sequence
                if feature_type == 'CDS':
                    # extract this feature from the genome
                    feature_seq = genome[start-1:end]

                    # reverse complement feature_seq if necessary
                    if strand == '-':
                        feature_seq = feature_seq.reverse_complement()

                    # extract the gene name
                    match = re.search("Gene\s+(\S+)\s+", attributes)
                    gene_name = match.group(1)
                    
                    # extract the exon number
       
                    # dictionary called cds where, key = gene name, value = another dictionary (key = exon number, value = sequence of that exon)
                    if re.search("exon\s+[0-9]", attributes):
                        gene_seq = str(feature_seq)
                        exon_match = re.search("exon\s+[0-9]", attributes)
                        exon_number = exon_match.group()
                        gene_dic[gene_name] = {}
                        exon_dic["_".join([gene_name,exon_number])] = gene_seq

                    # print FASTA format
                    
                    #print(">" + organism + "_" + gene_name)
                    #print(feature_seq)
        
        for gene_key in gene_dic.keys():
            tmp_dic = dict()
            for exon_key in exon_dic.keys():
                if gene_key in exon_key:
                    exon_num_key = exon_key.split("_")[1]
                    tmp_dic[exon_num_key] = exon_dic.get(exon_key)
            gene_dic[gene_key] = tmp_dic
        print(gene_dic)
    
def gc(sequence):
    # calculate and print the GC content for that substring (2 decimal places)
    count_of_G = sequence.count('G')
    count_of_C = sequence.count('C')

    return(count_of_G + count_of_C)/len(sequence)

def codon2aa(codon):
    codon_dict = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'O', 'TAC':'Y', 'TAG':'O', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'O', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}

    return(codon_dict.get(codon, '-'))

def main():
    genome_sequence = parse_fasta()
    parse_gff(genome_sequence.seq)


# get the command-line arguments before calling main()
args = get_args()

# execute the program by calling main
if __name__ == "__main__":
    main()
