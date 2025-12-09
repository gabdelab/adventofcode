file = "data/3.txt"

with open(file, 'r') as filereader:
	content = filereader.read()

total = 0
for row in content.split("\n"):
	if not row:
		continue
	mlist = [int(i) for i in row if i != "\n"]
	# Exclude the last element
	first = max(mlist[:-1])
	imax = mlist.index(first)
	second = max(mlist[imax+1:])

	total += first*10 + second

print(total)