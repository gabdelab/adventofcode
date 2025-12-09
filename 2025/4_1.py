from collections import defaultdict

file = "data/4.txt"

with open(file, 'r') as filereader:
	content = filereader.read()

out = defaultdict(lambda: defaultdict(bool))

for indexrow, i in enumerate(content.split("\n")):
	for indexcol, j in enumerate(i):
		out[indexrow][indexcol] = True if j == "@" else False

total = 0

for indexrow, column in out.items():
	for indexcol, item in column.items():
		print(indexrow, indexcol)
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
			print(indexrow, indexcol)
			total += 1

print(total)
