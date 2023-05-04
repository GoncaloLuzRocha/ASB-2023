#!/bin/bash/env python3

from Bio import SeqIO

alignment_file = "aligned_afterConcat.fasta"

# Load alignment
alignment = SeqIO.parse(alignment_file, "fasta")

# Count occurrences of each sequence name
counts = {}
for record in alignment:
    name = record.id.split()[0]
    counts[name] = counts.get(name, 0) + 1

# Rename duplicate sequence names
new_records = []
for record in SeqIO.parse(alignment_file, "fasta"):
    name = record.id.split()[0]
    if counts[name] > 1:
        new_name = "{}_{}".format(name, counts[name])
        record.id = new_name
        record.name = new_name
        record.description = new_name
        counts[name] -= 1
    new_records.append(record)

# Write out new alignment
SeqIO.write(new_records, "my_alignment_renamed.fasta", "fasta")

