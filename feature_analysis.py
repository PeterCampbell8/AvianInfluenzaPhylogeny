#REGEX to find lines with non-standard characters:  ^[AGCT]{1}.*(?<=[^ACGT]).*$

#Set cd to a protein's folder

from Bio import SeqIO
import os
import glob

#os.chdir(os.path.dirname(os.path.abspath(__file__)))
'''
#-----------Take GB files and pull nucleotide fasta---------------
def makeFASTA():
    with open("../Nucleotides.fasta", "w") as writeTo:
#        directory = 'records' #Rename to directory with your GB files. GB Files should be isolated from other things, like accession list
        for missing in os.listdir('.'): 
           for filename in os.listdir(f'{missing}/records'):
                records = list(SeqIO.parse(("%s/records/%s" %(missing, filename)),"genbank"))
                for record in records:
                    writeTo.write(">%s\n%s\n" %(record.name, record.seq))
    return

makeFASTA()
'''
with open("../typeOfGene.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            for item in record.features:
                if item.type == 'gene':
                    gene = (item.qualifiers.get("gene"))
                    writeTo.write(">%s\n%s\n" %(record.name, gene))
        