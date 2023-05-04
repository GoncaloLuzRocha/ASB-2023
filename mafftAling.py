#!/bin/bash/env python3

from datetime import datetime, timedelta
from Bio.Align.Applications import MafftCommandline
from Bio import AlignIO

# Input file name
input_file = "concatenated.fasta"

# Output file name
output_file = "aligned_afterConcat.fasta"

# Run MAFFT on the input file and save the output to a file
mafft_cline = MafftCommandline(input=input_file)
start_time = datetime.now()
print("Running MAFFT on %s..." % input_file)
stdout, stderr = mafft_cline()
with open(output_file, "w") as output_handle:
    output_handle.write(stdout)
end_time = datetime.now()

# Parse the aligned sequences from the output file
alignment = AlignIO.read(output_file, "fasta")

# Print some summary information about the alignment
print("Aligned %i sequences with %i columns" % (len(alignment), alignment.get_alignment_length()))

# Print the elapsed time and estimated time of arrival
elapsed_time = end_time - start_time
time_per_alignment = elapsed_time / len(alignment)
remaining_time = time_per_alignment * (len(alignment) - 1)
eta = end_time + remaining_time
print("Elapsed time: %s" % str(elapsed_time))
print("ETA: %s" % eta.strftime("%Y-%m-%d %H:%M:%S"))

# Write the alignment to a new file
AlignIO.write(alignment, "aligned.fasta", "fasta")

