import math
from collections import defaultdict

filename = "data/6.txt"

with open(filename, 'r') as fd:
	content = fd.read()

puzzles = defaultdict(list)
total = 0

for i in content.split("\n"):
	print(i)
	if i[0] in ["+", "*"]:
		print(puzzles)
		for index, j in enumerate(i.strip().split()):
			if j == "+":
				subtotal = sum(puzzles[index])
			else:
				subtotal = math.prod(puzzles[index])
			print("subtotal", index, subtotal)
			total += subtotal
	else:
		numbers = i.strip().split()
		print(numbers)
		for index, j in enumerate(numbers):
			puzzles[index].append(int(j))

print(total)