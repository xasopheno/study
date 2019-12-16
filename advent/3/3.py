import numpy as np


def get_data():
    with open("data.txt", "r") as f:
        datas = []
        for l in f:
            datas.append(l.split(","))

        return datas[0], datas[1]


data1, data2 = get_data()
# data1, data2 = ["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]

size = 18000
start = (size // 2, size // 2)


def make_path(data, start):
    x = start[0]
    y = start[1]
    p = np.zeros((size, size))
    for v in data:
        # print(v[0], v[1:], y, x)
        if v[0] == "R":
            d = int(v[1:])
            for i in range(d):
                p[y][x + i] = 1
            x += d
        elif v[0] == "L":
            d = int(v[1:])
            for i in range(d):
                p[y][x - i] = 1
            x -= d
        elif v[0] == "U":
            d = int(v[1:])
            for i in range(d):
                p[y - i][x] = 1
            y -= d
        elif v[0] == "D":
            d = int(v[1:])
            for i in range(d):
                p[y + i][x] = 1
            y += d

        else:
            print("?")

    return p


path1 = make_path(data1, start)
path2 = make_path(data2, start)
# print(path2)

intersections = []
for j in range(size):
    if j % 100 == 0:
        print(j / size * 100)
    for i in range(size):
        if path1[j][i] == 1 and path1[j][i] == path2[j][i]:
            if (i, j) != start:
                intersections += ((i, j),)

print(intersections)
result = []
for i in intersections:
    x = abs(start[0] - i[0])
    y = abs(start[1] - i[1])
    result.append(x + y)

print("answer: " + str(min(result)))

