d = []
with open("data.txt") as f:
    for line in f:
        d = line.split(",")
        d = [int(v) for v in d]


for i in range(0, 100):
    for j in range(0, 100):
        data = d.copy()
        # print(i, j)
        try:
            data[1] = i
            data[2] = j

            # print(data)
            # print("\n")

            position = 0

            while True:
                operation = data[position]

                if operation == 99:
                    break

                index1 = data[position + 1]
                index2 = data[position + 2]
                index3 = data[position + 3]
                if operation == 1:
                    data[index3] = data[index1] + data[index2]

                elif operation == 2:
                    data[index3] = data[index1] * data[index2]
                else:
                    # print("error:", position, data[position])
                    break

                position += 4

            # print(data[0])
            if data[0] == 19690720:
                print(100 * i + j)
        except:
            pass
