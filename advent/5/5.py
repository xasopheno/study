from enum import Enum

data = []
with open("data_new.txt") as f:
    for line in f:
        data = line.split(",")
        data = [int(v) for v in data]

# data[0] = 1

position = 0

ops = {
    1: {"length": 4},
    2: {"length": 4},
    3: {"length": 2},
    4: {"length": 2},
    99: {"length": 1},
}


def normalize_instruction(instruction: int) -> str:
    instruction = str(instruction)
    instruction = (4 - len(instruction)) * "0" + instruction
    return instruction


def clean_parameters(params: int) -> str:
    result = ""
    for v in str(params):
        if v != "1":
            result += "0"
        else:
            result += "1"
    return result


def parse_instruction(instruction: int) -> (int, int):
    i = normalize_instruction(instruction)
    opcode = i[-2:]
    parameters = clean_parameters(i[:-2])
    return (opcode, parameters)


while True:
    operation = data[position]
    opcode, parameters = parse_instruction(operation)
    opcode = int(opcode)
    op_length = ops[int(opcode)]["length"]
    print(opcode, parameters, "length", op_length)

    if opcode == 99:
        break

    elif opcode in [1, 2]:
        index1 = data[position + 1]
        index2 = data[position + 2]
        index3 = data[position + 3]
        if opcode == 1:
            data[index3] = data[index1] + data[index2]

        elif opcode == 2:
            data[index3] = data[index1] * data[index2]
        else:
            print("error:", position, data[position])
            break

    position += op_length


assert parse_instruction(21301) == ("01", "010")
assert parse_instruction(101) == ("01", "001")
