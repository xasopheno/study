from typing import List, Any, Optional, Union
from enum import Enum


class Operation(Enum):
    ADD = 1
    SUBTRACT = 2


class Stack:
    def __init__(self, data: List[Any] = []):
        self.data = data

    def __len__(self):
        return len(self.data)

    def push(self, value: int):
        self.data.append(value)

    def pop(self, value: int):
        if len(self) == 0:
            raise IndexError("Stack is empty.")
        else:
            self.data.pop(value)

    def max(self) -> Optional[Any]:
        max = 0
        for value in self.data:
            if value > max:
                max = value
        return max

    def reverse_polish(self):
        operators: List[Operation] = []
        operands = []
        for val in self.data:
            if type(val) == int:
                operands.append(val)
            else:
                token = tokenize(val)
                operators.append(token)

        calculating = True
        result = 0
        i = len(operators)
        while i > 0:
            operand_1 = operands.pop()
            operand_2 = operands.pop()
            operator = operators.pop()
            if operator is Operation.ADD:
                result += operand_1 + operand_2
                operands.append(result)
            if operator is Operation.SUBTRACT:
                result += operand_1 - operand_2
                operands.append(result)
            i -= 1

        return result


def tokenize(val: str) -> Any:
    try:
        token = {"+": Operation.ADD, "-": Operation.SUBTRACT}[val]
        return token
    except:
        return ValueError


