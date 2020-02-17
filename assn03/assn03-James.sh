#! /bin/bash

# assn02 - I had a bag Cheetos and sipped Mountain Dew - 2020.02.17

# assn03-1
for i in {808..8008}; do echo TR-$i; done

# assn03-2
alias enc="echo Keep up the great work!"
alias disc="echo So, is your anole manuscript published?"

# assn03-3
ls -l | grep .fasta | wc -l
15085

# assn03-4
ls -l | grep .tre | wc -l
14640

# assn03-5
ls -l | grep .sched | wc -l
15262

# assn03-6
ls gene_trees/ | grep .fasta | cut -d "_" -f1 > fasta_files.txt
ls gene_trees/ | grep .tre | cut -d "_" -f1 > tre_files.txt
comm -12 fasta_files.txt tre_files.txt | wc -l
14640
cat fasta_files.txt | wc -l
15085
expr 15085 - 14640
445

# assn03-7
for f in *.sched
do
    grep "Program Return Code: 0" f
done


# assn03-8
