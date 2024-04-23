#FASTARandomSampler
#grabs 100 random sequences from the aligned file
#Does this random sampling 1000 times and writes each one to a file

from Bio import SeqIO
import os
from random import sample

os.chdir(os.path.dirname(os.path.abspath(__file__)))


fastaFile = list(SeqIO.parse("full_data/ha/haAlignedGuide.fasta", "fasta"))

for loop in range(1,1001):
    with open("full_data/ha/subsample/randSeqs%s.fasta" %loop, "w") as writeTo:
       samples = sample(fastaFile, 100)
       for samp in samples:
        writeTo.write(">%s\n%s\n" %(samp.name, samp.seq))
"""
with open("paths.txt", "w", newline='') as writeTo:
    for loop in range(1,1001):
        writeTo.write("randoSeqs%s.fasta\n" %loop)
"""