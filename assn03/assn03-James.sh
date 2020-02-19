#! /bin/bash

# assn02 - I had a bag Cheetos and sipped Mountain Dew - 2020.02.17

# assn03-1
for i in {808..8008}; do echo TR-$i; done

# assn03-2
alias enc="echo Keep up the great work!"
alias disc="echo So, is your anole manuscript published?"
alias mot="echo Pragmatism in your personal model."

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
comm -23 fasta_files.txt tre_files.txt | wc -l
445

# assn03-7
for f in *.sched
do
    if grep -q "Program Return Code: 0" $f; then
	echo exists
    else
	echo not found
    fi
done > out.txt
grep "not found" out.txt | wc -l
45
grep "not found" -v out.txt | wc -l
15217

# assn03-8
comm -23 fasta_files.txt tre_files.txt > fasta_only.txt
while read f; do
    echo "write_raxml_job_script.py ${f}_alignment.fasta > ${f}_alignment.pbs"
done < fasta_only.txt
