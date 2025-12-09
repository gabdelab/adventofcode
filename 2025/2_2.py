file = "data/2.txt"

with open(file, 'r') as fd:
	content = fd.read()


total = 0

def is_splittable(some_string, divisor):
	"""Returns true if the string is splittable in "divisor" times the same pattern"""
	index = int(len(some_string)/divisor)
	if divisor == 0:
		return False
	if len(some_string) % divisor != 0:
		return False
	if some_string == "":
		return True
	if some_string[0:index] == some_string[index:]:
		return True
	if some_string[0:index] == some_string[index:2*index]:
		return is_splittable(some_string[index:], divisor-1)


for i in content.split(","):
	start, end = i.split("-")
	istart, iend = int(start), int(end)

	for j in range(istart, iend+1):
		strj = str(j)

		divisor = 2

		while divisor <= len(strj):
			if is_splittable(strj, divisor):
				total += int(strj)
				break
			divisor += 1

print(total)