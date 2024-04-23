#----------------Set the working directory to the protein's folder---------------------------
#                

####-------------Subsequent batch download attempts should be structured within the protein folder as:
#### {protein} > missing{#} > auxFiles & records


from Bio import SeqIO
import os


startingPoint = input("Folder with target missing records (eg. missing0): ")

#Make a set of records correctly received from GenBank
def receivedSet(startingPoint):
    received = set()
    directory = '%s/records' %(startingPoint) #The folder with your previous batch download attempt
    for filename in os.listdir(directory):
        records = list(SeqIO.parse(("%s/%s" %(directory, filename)),"genbank"))
        for record in records:
            rec = record.annotations["accessions"]
            received.update(rec)
    return received

#Make a set of the original accession list for comparison
def accessionSet(startingPoint):
    accessions = set()
    with open("%s/auxFiles/accessions.fa" %(startingPoint), 'r') as acc: #the folder with the list you attempted to download
        for line in acc.readlines():
            line = str(line)
            accessions.add(line[:-1])
    return accessions

#Make a set of the records missing from the received list
def missingSet(accessions, received):
    return accessions.difference(received)



missing = missingSet(accessionSet(startingPoint), receivedSet(startingPoint))

#write the missing records to a fasta file
with open("accessions_%s.fa" %(startingPoint), "w") as writeTo:
    for miss in missing:
        writeTo.write("%s\n" %(miss))