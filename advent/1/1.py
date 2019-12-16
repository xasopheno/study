# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

data = []
with open("data.txt", "r") as f:
    for line in f:
        data.append(int(line))


def fuel(mass: int):
    f = (mass // 3) - 2
    if f <= 0:
        return 0
    else:
        return f


def fuel_recursive(mass):
    f = fuel(mass)
    total = f
    while f > 0:
        f = fuel(f)
        total += f
    return total


result = sum([fuel_recursive(d) for d in data])
print(result)

