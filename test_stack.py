from nose2.tools import such  # type: ignore
from stack import Stack
from typing import List


def stack_1() -> Stack:
    return Stack([2, 4, 7, 4, 3, 6])


with such.A("Stack") as it:

    @it.should("return maximum value")
    def test_stack_max():
        it.assertEqual(stack_1().max(), 7)

    @it.should("reverse polish")
    def test_reverse_polish():
        input = ["+", 2, 4]
        result = Stack(input).reverse_polish()
        expected = 6
        it.assertEqual(result, expected)

    def test_reverse_polish_long():
        input = ["+", 2, 4, "-", 3]
        result = Stack(input).reverse_polish()
        expected = 6
        # it.assertEqual(result, expected)


it.createTests(globals())
