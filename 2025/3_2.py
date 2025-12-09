file = "data/3.txt"

with open(file, 'r') as filereader:
	content = filereader.read()

total = 0
for row in content.split("\n"):
	if not row:
		continue
	mlist = [int(i) for i in row if i != "\n"]
	# Exclude the last element

	elems = []
	for i in range(1, 13):
		if i == 12:
			elem = max(mlist)
		else:
			elem = max(mlist[:-12+i])
		elems.append(elem)
		imax = mlist.index(elem)
		mlist = mlist[imax+1:]

	subtotal = sum([j*10**(11-i) for i, j in enumerate(elems)])


	total += subtotal

print(total)