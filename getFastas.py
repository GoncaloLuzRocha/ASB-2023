#!/bin/bash/env python3

from Bio import Entrez, SeqIO

Entrez.email = "emailBatata@gmail.com"
P32_Gene_list = ["JN596272","JN596273","JN596274","JN596275","JN602370","NC_004002","AY368684","HQ607368","HM770955","FJ882029","FJ748487","NC_003027","AF409137","AF124516","HM572329","EF522179","EF522176","AY382869","EF522178","NC_004003","AY773088","AY881707","EF514892","EF514889","EF522180","AY159333","EF522181","HM572331","EU625263","EU625262"]
GPCR_Gene_list = ["JQ310666","JQ310668","JQ310675","JQ310672","JQ310667","NC_004002","FJ869389","FJ869387","FJ869385","FJ869381","FJ869378","NC_003027","AF409137","FJ869377","NC_004003","FJ869359","FJ869357","FJ869355","FJ869358","FJ869356"]
ROP30_Gene_list =["JQ310671","JQ310673","JQ310670","JQ310674","JQ310669","NC_004002","GU119916","GU119924","GU119920","GU119929","NC_003027","AF409137","GU119947","NC_004003","GU119933","GU119942","GU119949","GU119936","GU119940"]
accession_lists = [P32_Gene_list,GPCR_Gene_list,ROP30_Gene_list]

for i, accession_numbers in enumerate(accession_lists):
    records = []

    for accession in accession_numbers:
        handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        records.append(record)
        handle.close()

    filename = "sequences_{}.fasta".format(i+1)
    with open(filename, "w") as output_handle:
        SeqIO.write(records, output_handle, "fasta")
