#REGEX to find lines with non-standard characters:  ^[AGCT]{1}.*(?<=[^ACGT]).*$

#----------------Set cd to a protein's folder-------------------------

from Bio import SeqIO
import os
import glob
import re
import csv
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
'''
with open("../typeOfAnnotation.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            for item in record.features:
                if item.type == 'gene':
                    gene = (item.qualifiers.get("gene"))
                    writeTo.write(">%s\n%s\n" %(record.name, gene))
'''

#for field 1
'''
with open("../typeOfAnnotation_organism_field1.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            try:
                writeTo.write(">%s\n%s\n" %(record.name, record.annotations['organism'].split('/')[1]))
            #----Three forms of 'organism' field seen----
            #>MW097430
            #Influenza A virus
            #>CY074539
            #Influenza A virus (A/California/VRDL311/2009(H1N1))
            #>AB049159
            #Influenza A virus (A/parakeet/Chiba/1/97(H9N2))
            #----------------------------------
            except:
                writeTo.write(">%s\n'None'\n" %(record.name))
'''

#for field 2
'''
with open("../typeOfAnnotation_organism_field2.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            try:
                field2 = record.annotations['organism'].split('/')[2]
                if re.search('[0-9]', field2):              #filter out records with a number in this field. Likely an accession number
                    writeTo.write(">%s\n'Probably not relevant'\n" %(record.name))
                else:
                    writeTo.write(">%s\n%s\n" %(record.name, field2))
            #----Three forms of 'organism' field seen----
            #>MW097430
            #Influenza A virus
            #>CY074539
            #Influenza A virus (A/California/VRDL311/2009(H1N1))
            #>AB049159
            #Influenza A virus (A/parakeet/Chiba/1/97(H9N2))
            #----------------------------------
            except:     #if this record lacks a () of information, output none
                writeTo.write(">%s\n'None'\n" %(record.name))
'''

#Pull both fields 1 and 2, if 2 has a number write 'probably not relevant', if there's no field 1 or 2, write none
'''
csvfile = open('../../worldcitiesASCII.csv',encoding="utf-8")
worldplaces = csv.reader(csvfile)
places = set()
for i in worldplaces:
    for p in i:
        places.add(p)


with open("../typeOfAnnotation_organism_place.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            #try:
            fields = record.annotations['organism'].split('/')
                #except:     #if this record lacks a () of information, output none
            try:
                if fields[2] in places:
                    writeTo.write(">%s\n%s\n" %(record.name, fields[2]))
                elif fields[1] in places:
                    writeTo.write(">%s\n%s\n" %(record.name, fields[1]))
                else:
                    continue
                    #writeTo.write(">%s\n'No match for:%s or %s'\n" %(record.name, fields[2], fields[1]))
            except:
                continue
            #    writeTo.write(">%s\n'No details'\n" %(record.name))
            #----Three forms of 'organism' field seen----
            #>MW097430
            #Influenza A virus
            #>CY074539
            #Influenza A virus (A/California/VRDL311/2009(H1N1))
            #>AB049159
            #Influenza A virus (A/parakeet/Chiba/1/97(H9N2))
            #----------------------------------
'''


#for year/date

with open("../typeOfAnnotation_organism_year.fasta", "w") as writeTo:
    for filename in glob.iglob('missing?/records/*.gb'):
        records = list(SeqIO.parse(filename, format = "genbank"))
        for record in records:
            try:
                writeTo.write(">%s\n%s\n" %(record.name, record.annotations['organism'].split('/')[-1]))
            #----Three forms of 'organism' field seen----
            #>MW097430
            #Influenza A virus
            #>CY074539
            #Influenza A virus (A/California/VRDL311/2009(H1N1))
            #>AB049159
            #Influenza A virus (A/parakeet/Chiba/1/97(H9N2))
            #----------------------------------
            except:
                writeTo.write(">%s\n'None'\n" %(record.name))
