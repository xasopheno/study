import numpy as np


def get_intersections():
    result = []
    with open("intersections.txt", "r") as f:
        l = next(f)
        data = l.strip()
        data = data.replace("[]", "")
        # data = data.replace("]", "")
        data = data.split(")")
        for d in data:
            try:
                d = str(d[3:])
                d = d.split(",")
                d = {"x": int(d[0]), "y": int(d[1])}
                result.append(d)
            except:
                pass

    return result


def get_data():
    with open("data.txt", "r") as f:
        datas = []
        for l in f:
            datas.append(l.split(","))

        return datas[0], datas[1]


data1, data2 = get_data()
# data1, data2 = ["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]
data_t = [
    "R75",
    "D30",
    "R83",
    "U83",
    "L12",
    "D49",
    "R71",
    "U7",
    "L72",
    "U62",
    "R66",
    "U55",
    "R34",
    "D71",
    "R55",
    "D58",
    "R83",
]

size = 18000
start = (size // 2, size // 2)


def make_path(data, start, intersections):
    x = start[0]
    y = start[1]
    p = np.zeros((size, size))
    total_distance = 0
    result = []

    def test(x, y):
        for intersection in intersections:
            if x == intersection["x"] and y == intersection["y"]:
                result.append({"x": x, "y": y, "d": total_distance})

    for v in data:
        # print(v[0], v[1:], y, x)
        d = int(v[1:])
        if v[0] == "R":
            for i in range(d):
                p[y][x + i] = 1
                total_distance += 1
                test(x + i, y)
            x += d
        elif v[0] == "L":
            for i in range(d):
                p[y][x - i] = 1
                total_distance += 1
                test(x - i, y)
            x -= d
        elif v[0] == "U":
            for i in range(d):
                p[y - i][x] = 1
                total_distance += 1
                test(x, y - i)
            y -= d
        elif v[0] == "D":
            for i in range(d):
                p[y + i][x] = 1
                total_distance += 1
                test(x, y + i)
            y += d
        else:
            print("?")
        print(v, total_distance)

        # print(total_distance)
    return result


ints = get_intersections()
for i in range(5):
    print(ints[i])

# path1 = make_path(data1, start, ints[:])
# path2 = make_path(data2, start, ints[:])
t = make_path(data_t, start, ints[:])

# print(path1[0])
# print(path2[0])
# print(len(path1))
# print(len(path2))

# result = []
# for i in range(len(path1)):
# result.append(path1[i]["d"] + path2[i]["d"])

# print(min(result))
x = [{"a": 1, "b": 2}, {"a": 1, "b": 3}]
r = x.index({"a": 1, "b": 3})
print(r)
