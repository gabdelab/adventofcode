file = "data/2.txt"

with open(file, 'r') as fd:
	content = fd.read()


total = 0

for i in content.split(","):
	start, end = i.split("-")
	istart, iend = int(start), int(end)

	for j in range(istart, iend+1):
		strj = str(j)
		if len(strj) % 2 == 1:
			continue
		if strj[0:int(len(strj)/2)] == strj[int(len(strj)/2):]:
			total += j

print(total)