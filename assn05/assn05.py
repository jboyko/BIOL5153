#! /usr/bin/env python3

input = open("watermelon.gbf", "r")
GeneList = []
for line in input:
    if "gene=" in line:
        value = line.split("=", 1)
        value = value[1].rstrip()
        value = value.strip('\"')
        if value in GeneList:
            print(value, "already found.")
        else:
            GeneList.append(value)
            print(value, "added to list.")
input.close()
GeneList.sort()
print(GeneList)
