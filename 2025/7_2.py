from collections import defaultdict

filename = "data/7.txt"

with open(filename, 'r') as fd:
	content = fd.read()


iterations = {}
for irow, row in enumerate(content.split("\n")):

	if irow == 0:
		start = row.find("S")
		iterations[0] = {start: 1}
		continue
	if irow % 2 == 1:
		continue

	temp_iter = defaultdict(int)

	for element, nb_occurences in iterations[irow/2 - 1].items():
		if row[element] == ".":
			temp_iter[element] += nb_occurences
		elif row[element] == "^":
			temp_iter[element - 1] += nb_occurences
			temp_iter[element + 1] += nb_occurences

	iterations[int(irow/2)] = temp_iter

for k, v in iterations.items():
	print(k, sum(v1 for v1 in v.values()))