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

	if steps >= 100:
		total += steps // 100
		steps = steps % 100

	if direction == "R":
		if start + steps >= 100:
			print("crossed 0 while doing steps %d and direction %s - start = %d; total = (%d)" % (steps, direction, start, (start + steps)%100))
			total += 1
		start = (start + steps) % 100
	else:
		if start - steps <= 0 and start != 0:
			print("crossed 0 while doing steps %d and direction %s - start = %d total = (%d)" % (steps, direction, start, (start - steps)% 100))
			total += 1
		start = (start - steps) % 100

print(total)