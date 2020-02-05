#! /bin/bash

# assn01 - I had a couple cheetos - 2020.01.29

# assn01-1
find ~/2020_PracticalProgramming/ -name nad*.fasta

# assn01-2
top -o command

#ID    COMMAND      %CPU TIME     #TH   #WQ  #PORTS MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS          %CPU_ME
#12046  top          4.3  00:00.78 1/1   0    25     5120K+ 0B     0B     12046 11671 running  *0[1]           0.00000
# PhysMem: 8085M used (2921M wired), 106M unused.
# Load Avg: 1.58, 1.62, 1.75  CPU usage: 6.69% user, 6.45% sys, 86.84% idle

# assn01-3
grep misc_feature watermelon.gff | sort -k7gr > IR_regions.gff

# assn01-4
# from IR
grep misc_feature watermelon.gff | grep "chloroplast IR" | wc -l
# from non-IR
grep misc_feature watermelon.gff | grep -v "chloroplast IR" | wc -l

# assn01-5
grep -hB69 GGATCC *.fasta | grep -huB69 GAATTC | less -S

# assn01-6
cat -n shaver_etal.csv | grep -B500 1000 | less -S

# assn01-7
column -t fruit.txt | sort -k2,2r -k3



