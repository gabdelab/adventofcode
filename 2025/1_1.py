file = "data/1.txt"


with open(file, 'r') as filereader:
	content = filereader.read()


start = 50
total = 0

for i in content.split("\n"):
	if not i:
		continue

	direction = i[0]
	steps = int(i[1:])


	if direction == "R":
		start = (start + steps) % 100
	else:
		start = (start - steps) % 100

	if start == 0:
		total += 1

print(total)