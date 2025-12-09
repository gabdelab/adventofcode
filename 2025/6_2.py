import math
from collections import defaultdict
import re

filename = "data/6.txt"

with open(filename, 'r') as fd:
	content = fd.read()

puzzles = defaultdict(str)
total = 0

for i in content.split("\n"):
	last_index = 0
	if i[0] in ["+", "*"]:
		for index, j in enumerate(i):
			if j == " ":
				continue
			next_plus = i[index+1:].find("+")
			next_times = i[index+1:].find("*")
			if next_plus == -1 and next_times == -1:
				next_char = 100000
			elif next_plus == -1:
				next_char = next_times
			elif next_times == -1:
				next_char = next_plus
			else:
				next_char = min(next_plus, next_times)
			if j == "+":
				subtotal = sum([int(v) for k, v in puzzles.items() if v and k >= index and k < index + next_char])
			else:
				subtotal = math.prod([int(v) for k, v in puzzles.items() if v and k >= index and k < index + next_char])
			total += subtotal
	else:
		for index, j in enumerate(i):
			puzzles[index] += j


print(total)