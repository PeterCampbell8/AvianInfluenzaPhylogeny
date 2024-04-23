import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

protein = input("Protein folder you want: ")
results = []

for file in os.listdir(f'{protein}/treesumm'):
	with open (f"{protein}/treesumm/{file}", "r") as current:
		lines = current.readlines()
		results.append(lines[36])

with open ("treeSummresults.txt", "w") as result:
	for item in results:
		result.write(f"{item}\n")