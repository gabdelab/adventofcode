filename = "data/7.txt"

with open(filename, 'r') as fd:
	content = fd.read()


iterations = {}
hit = 0
for irow, row in enumerate(content.split("\n")):
	if irow == 0:
		start = row.find("S")
		iterations[0] = [start]
		continue
	if irow % 2 == 1:
		continue

	temp_iter = []
	for icol in iterations[irow/2 - 1]:
		if row[icol] == ".":
			temp_iter.append(icol)
		elif row[icol] == "^":
			hit += 1
			temp_iter.extend([icol-1, icol+1])
	temp_iter = list(set(temp_iter))

	iterations[irow/2] = temp_iter

print(iterations)
print(hit)