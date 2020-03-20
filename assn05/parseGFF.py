#! /usr/bin/env python3

input = open("watermelon.gff", "r")
GeneList = []
for line in input:
    line = line.rstrip("\n")
    line = line.split("\t")
    line = line[8].split(" ")
    if(line[1] == "similar"):
        print("similar")
    if(line[1] == "inverted"):
        print("inverted")
    else:
        if line[1] in GeneList:
            print("already found")
        else:
            GeneList.append(line[1])
GeneList.sort()
print(GeneList)
