import random


file = "data/9.txt"


with open(file, 'r') as filereader:
    content = filereader.read()

points = []
red_points = []

for row in content.split("\n"):
    splitrow = row.split(",")
    red_points.append((int(splitrow[0]), int(splitrow[1])))

green_points = []
previous_point = red_points[-1]
for index, i in enumerate(red_points):
    # print(i, previous_point, -1**(i[1] > previous_point[1]), i[1] > previous_point[1])

    direction = ""

    if i[0] == previous_point[0]:
        if abs(i[1] - previous_point[1]) == 1:
            print("ABORT")
        if i[1] > previous_point[1]:
            pointrange = range(previous_point[1] + 1, i[1])
            direction = ""
        else:
            pointrange = range(i[1] + 1, previous_point[1])
        for k in pointrange:
            green_points.append((i[0], k))
    else:
        if abs(i[0] - previous_point[0]) == 1:
            print("ABORT")
        if i[0] > previous_point[0]:
            pointrange = range(previous_point[0] + 1, i[0])
        else:
            pointrange = range(i[0] + 1, previous_point[0])
        for k in pointrange:
            green_points.append((k, i[1]))

    previous_point = i

points = set(["%s-%s" % (i[0], i[1]) for i in red_points]
             ).union(set(["%s-%s" % (i[0], i[1]) for i in green_points]))


def check_if_correct(i0, i1, j0, j1):
    # Check if there's any green point inside
    for k in green_points:
        k0, k1 = k[0], k[1]
        if k0 > i0 and k0 < j0 and k1 > i1 and k1 < j1:
            return False
    return True


max_area = 1571016172
distances = []
random.shuffle(red_points)
red_points_copy = red_points.copy()
for index, i in enumerate(red_points):
    print(index)
    random.shuffle(red_points_copy)
    for indexj, j in enumerate(red_points_copy):
        if i[0] == j[0] or i[1] == j[1]:
            continue
        i0, i1, j0, j1 = min(i[0], j[0]), min(i[1], j[1]), max(i[0], j[0]), max(i[1], j[1])

        if (j1 - i1 + 1) * (j0 - i0 + 1) < max_area:
            continue
        if check_if_correct(i0, i1, j0, j1):
            max_area = max(max_area, (j1 - i1 + 1) * (j0 - i0 + 1))
            print(max_area)

print(max_area)
