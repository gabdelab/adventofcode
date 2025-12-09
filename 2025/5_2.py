file = "data/5.txt"


with open(file, 'r') as filereader:
	content = filereader.read()

a = content.split("\n\n")
boundaries = a[0]
items = a[1]
existing = set()

# Ordered list of boundaries
bounds = []
boundaries = a[0].split("\n")

int_boundaries = []
for j in boundaries:
	l = j.split("-")
	print(l)
	int_boundaries.append((int(l[0]), int(l[1])))
boundaries = sorted(int_boundaries, key=lambda t: t[0])
print(boundaries)

for index, i in enumerate(boundaries):
	if not bounds:
		bounds = [(i[0], i[1])]
		continue
	for indexj, j in enumerate(bounds):
		# 6 choices
		# - area is fully left to the first element
		# - area is left but eats a bit
		# - area is left and eats fully
		# - area is fully within
		# - area is right but eats a bit
		# - area is fully right

		# can be reduced to 3:
		# - area is fully left
		# - there is any intersection
		# - area is fully right
		minibound, maxibound = j[0], j[1]
		print("here", bounds, minibound, maxibound, i[0], i[1])
		if i[1] < minibound:
			print("case1")
			bounds = bounds[:(indexj+1)] + [(i[0], i[1])] + bounds[(indexj+1):]
		elif i[0] > maxibound:
			if indexj == len(bounds) - 1:
				print("case 2 a")
				bounds.append((i[0], i[1]))
			else:
				print("case 2b")
				pass
		else:
			print("case 3")
			bounds = bounds[:indexj] + [(min(i[0], minibound), max(i[1], maxibound))] + bounds[(indexj+1):]


print(bounds)

total = 0
for k in bounds:
	total += k[1] - k[0] + 1
print(total)