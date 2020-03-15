#! /usr/bin/env python3

# read in the file name
value = input("Please enter a file with a string of A,T,C,Gs:\n")
with open(value) as input_file:
    data = input_file.read().upper()
    print("Sequence:", data)
    # count the total
    print("Sequence length:", len(data))
    seqlen = len(data)
    # count the number of Letters
    print("Percent of As:", round((data.count("A")/seqlen)*100, 2), "%")
    print("Percent of Ts:", round((data.count("T")/seqlen)*100, 2), "%")
    print("Percent of Cs:", round((data.count("C")/seqlen)*100, 2), "%")
    print("Percent of Gs:", round((data.count("G")/seqlen)*100, 2), "%")
