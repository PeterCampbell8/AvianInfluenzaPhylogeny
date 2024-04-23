from Bio import SeqIO
import timeit

start = timeit.default_timer()
#alignment file
alignment_file = "pb1/pb1AlignedGuide2.fasta"


#gap alignment file
#gaps_file = input("File path to gaps analysis file: ")
gaps_file = "pb1/pb1AlignedGuide2.gaps.txt"

#cutoff = input("provide a cutoff ")
cutoff = 1
'''
#Make a list of lines
#Lines = [sequenceID, % gaps]
def getGoodSeq():
    with open(gaps_file, 'r', newline = "") as gaps:
        gap_lines = gaps.readlines()
        gap_lines = [x.strip().split()[1:3] for x in gap_lines]
        gap_lines = [[x[0], float(x[1][:-1])] for x in gap_lines]
        
        goodLines = [x[0] for x in gap_lines if x[1] < cutoff]
        return goodLines

#getGoodSeq()

def pullAligns():
    with open (alignment_file, 'r', newline="") as aligned:
        goodLines = getGoodSeq()
        goodSeq = [x for x in SeqIO.FastaIO.SimpleFastaParser(aligned) if x[0] in goodLines]
        return goodSeq

outFileName = input("Provide the output file name: ")
with open (outFileName, 'x', newline="") as writeTo:
    for seq in pullAligns():
        writeTo.write(">%s\n%s\n" %(seq[0], seq[1]))
'''

def getGoodSeq():
    with open(gaps_file, 'r', newline = "") as gaps:
        
        gap_lines = gaps.readlines()
        
        stripper = lambda x: x.strip().split()
        
        gap_lines = list(map(stripper, gap_lines))
        
        floater = lambda x: [x[1], float(x[2][:-1])]
        gap_lines = list(map(floater, gap_lines))
        
        goodLines = [x[0] for x in gap_lines if x[1] < cutoff]
        
        return goodLines

#getGoodSeq()

def pullAligns():
    goodLines = getGoodSeq()
    with open (alignment_file, 'r', newline="") as aligned:
        goodSeq = [x for x in SeqIO.FastaIO.SimpleFastaParser(aligned) if x[0] in goodLines]
        return goodSeq

outFileName = input("Provide the output file name: ")
with open (outFileName, 'w', newline="") as writeTo:
    seqs = pullAligns()
    for seq in seqs:
        writeTo.write(">%s\n%s\n" %(seq[0], seq[1]))


print("runtime: ", timeit.default_timer() - start)
