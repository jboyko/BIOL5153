#! /usr/bin/env python3
import argparse
import csv
import re

# inputs
parser = argparse.ArgumentParser()
parser.add_argument('txt', help="the txt file")
args = parser.parse_args()

# operations
with open(args.txt) as input:
    sentence = " ".join(input)
    for m in re.finditer("[KC]ath.{0,1}r[yi]ne*", sentence):
        print(m.group(0), m.start(), m.end(), m.end() - m.start())
