#!/bin/bash/env python3

from Bio import SeqIO

# Input file names
file1 = "sequences_1.fasta"
file2 = "sequences_2.fasta"
file3 = "sequences_3.fasta"

# Output file name
output_file = "concatenated.fasta"

# Open the output file for writing
with open(output_file, "w") as out_handle:

    # Iterate over the input files and write each record to the output file
    for file_name in [file1, file2, file3]:
        with open(file_name) as in_handle:
            for record in SeqIO.parse(in_handle, "fasta"):
                SeqIO.write(record, out_handle, "fasta")

