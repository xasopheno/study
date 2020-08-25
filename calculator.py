from typing import List
import operator

#  [0, 1, 2]
values = ["1", "2", "3", "4", "5", "6"]
ops = ["+", "-", "*", "/"]


def expressions(values: List[int]):
    if len(values) == 1:
        yield values

    for i in range(len(values)):
        copy_values = values[:]  # [1, 2, 3]
        val = copy_values.pop(i)  # [2, 3]
        # copy_values = [2, 3]

        for op in ops:
            for rest in expressions(copy_values):
                yield [val] + [op] + rest


print(list(expressions(values)))


#  def parse(s: str) -> (List[int], List[str]):
#  operations = set("+=*/")
#  nums = []
#  ops = []
#  state = []
#  for val in list(s):
#  if val in operations:
#  ops.append(val)
#  nums.append("".join(state))
#  state = []
#  else:
#  state.append(val)

#  nums.append("".join(state))
#  return nums, ops


#  print(parse("11/2+3"))

