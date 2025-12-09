file = "data/9.txt"


with open(file, 'r') as filereader:
	content = filereader.read()

points = []

for row in content.split("\n"):
	splitrow = row.split(",")
	points.append((int(splitrow[0]), int(splitrow[1])))

distances = []
for i in points:
	for j in points:
		distances.append((j[1] - i[1] + 1)*(j[0] - i[0] + 1))

print(sorted(distances, reverse=True)[0])