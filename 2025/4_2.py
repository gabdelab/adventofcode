from collections import defaultdict

file = "data/4.txt"

with open(file, 'r') as filereader:
	content = filereader.read()

out = defaultdict(lambda: defaultdict(bool))

for indexrow, i in enumerate(content.split("\n")):
	for indexcol, j in enumerate(i):
		out[indexrow][indexcol] = True if j == "@" else False

total = 0
total_iteration = 0

while True:
	total_iteration = 0
	found = []
	for indexrow, column in out.items():
		for indexcol, item in column.items():
			if item == False:
				continue
			a = int(out.get(indexrow+1, defaultdict(bool)).get(indexcol-1, False)) \
				+ int(out.get(indexrow, defaultdict(bool)).get(indexcol-1, False)) \
				+ int(out.get(indexrow-1, defaultdict(bool)).get(indexcol-1, False)) \
				+ int(out.get(indexrow+1, defaultdict(bool)).get(indexcol, False)) \
				+ int(out.get(indexrow-1, defaultdict(bool)).get(indexcol, False)) \
				+ int(out.get(indexrow+1, defaultdict(bool)).get(indexcol+1, False)) \
				+ int(out.get(indexrow, defaultdict(bool)).get(indexcol+1, False)) \
				+ int(out.get(indexrow-1, defaultdict(bool)).get(indexcol+1, False))
			if a < 4:
				total_iteration += 1
				found.append((indexrow, indexcol))

	for i in found:
		out[i[0]][i[1]] = False
	total += total_iteration
	print(total_iteration, total)

print(total)
