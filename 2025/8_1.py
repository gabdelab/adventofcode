from collections import defaultdict
import math

test = False
file = "data/8.txt"
nb_iter = 1000
if test:
	file = "data/8_ex.txt"
	nb_iter = 10

class Point:

	def __init__(self, index, x, y, z):
		self.index = index
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "%d,%d,%d" % (self.x, self.y, self.z)

class Distance:

	def __init__(self, pt1, pt2):
		self.pt1 = pt1
		self.pt2 = pt2
		self.distance = self.compute_distance()

	def compute_distance(self):
		if self.pt1.index >= self.pt2.index:
			return 1e10
		return (self.pt1.x - self.pt2.x)**2 + (self.pt1.y - self.pt2.y)**2 + (self.pt1.z - self.pt2.z)**2

	def __repr__(self):
		return str(self.distance)

distances = []
points = []

with open(file, 'r') as filereader:
	content = filereader.read()

for index, row in enumerate(content.split("\n")):
	print(row)
	if not row:
		continue
	coordinates = row.split(",")
	points.append(Point(index, int(coordinates[0]), int(coordinates[1]), int(coordinates[2])))

for indexi, i in enumerate(points):
	for indexj, j in enumerate(points):
		distances.append(Distance(i, j))

distances = sorted(distances, key = lambda x: x.distance)[:nb_iter]

circuits = []
for distance in distances:
	for entry in circuits:
		if distance.pt1 in entry or distance.pt2 in entry:
			entry.add(distance.pt2)
	circuits.append(set([distance.pt1, distance.pt2]))

print(circuits)

to_throw = set()
for i in range(10):
	print(i, len(to_throw))
	# Remove any intersection
	for indexi, i in enumerate(circuits):
		for indexj, j in enumerate(circuits):
			if indexi == indexj:
				continue
			if i.intersection(j):
				circuits[indexi] = i.union(j)
				circuits[indexj] = j.union(i)
				to_throw.add(max(indexj, indexi))

for i in sorted(to_throw, reverse=True):
	circuits.pop(i)

circuits = sorted(circuits, key = lambda t: len(t), reverse=True)[:3]

print(circuits)
print(len(circuits))
print(math.prod([len(i) for i in circuits]))

