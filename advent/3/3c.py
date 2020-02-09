import numpy as np


def get_data():
    with open("data.txt", "r") as f:
        datas = []
        for l in f:
            datas.append(l.split(","))

        return datas[0], datas[1]


data1, data2 = get_data()
# data1, data2 = ["R8", "U5", "L5", "D7"], ["U7", "R6", "D4", "L4"]
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
data_t2 = [
    "R98",
    "U47",
    "R26",
    "D63",
    "R33",
    "U87",
    "L62",
    "D20",
    "R33",
    "U53",
    "R51",
    "U98",
    "R91",
    "D20",
    "R16",
    "D67",
    "R40",
    "U7",
    "R15",
    "U6",
    "R7",
]


def traverse_wire(wire):
    wire_info = {}
    x, y, distance = 0, 0, 0
    directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            distance += 1
            wire_info[(x, y)] = distance
    return wire_info


wire_one = traverse_wire(data1)
wire_two = traverse_wire(data2)
crossings = wire_one.keys() & wire_two.keys()

fewest_steps = min(crossings, key=lambda x: wire_one[x] + wire_two[x])
print(fewest_steps)
steps = wire_one[fewest_steps] + wire_two[fewest_steps]
print(steps)

closest = min(
    [intersection for intersection in crossings], key=lambda x: abs(x[0]) + abs(x[1])
)
print(closest)
distance = abs(closest[0]) + abs(closest[1])
print(distance)


