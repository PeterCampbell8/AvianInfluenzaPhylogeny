#Remove all records in a given protein folder whose sequence is shorter than a given length

from Bio import SeqIO
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

protName = str(input("Name of protein to shorten the list of: ")) #name of the protein you're looking at eg. 'ha' or 'pb2'
keep = int(input("Minimum sequence length to keep: ")) #Found using the fastaStats.r script
fullList = list(SeqIO.parse("%s/%sNucleotides.fasta" %(protName,protName), "fasta"))
with open(f"{protName}_Nucleotides_{keep}OrMore.fasta", "w") as writeTo:
    for seq in fullList:
        if len(seq.seq) >= keep:
            writeTo.write(">%s\n%s\n" %(seq.name, seq.seq))