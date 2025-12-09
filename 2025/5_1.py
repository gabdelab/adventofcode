file = "data/5.txt"


with open(file, 'r') as filereader:
	content = filereader.read()

a = content.split("\n\n")
boundaries = a[0]
items = a[1]

bounds = []
for i in boundaries.split("\n"):
	a, b = i.split("-")
	bounds.append((int(a), int(b)))

print(bounds)

total = 0
for i in items.split("\n"):
	for j in bounds:
		if int(i) >= j[0] and int(i)<=j[1]:
			total += 1
			break

print(total)