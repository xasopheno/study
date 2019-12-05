from nose2.tools import such  # type: ignore
from binary_tree import Node, BinaryTree


def btree1():
    el1 = Node(1)
    el2 = Node(2)
    el3 = Node(3)
    el4 = Node(4)
    el5 = Node(5)
    el6 = Node(6)

    el1.left = el2
    el1.right = el3
    el1.left.left = el4
    el1.left.right = el5
    el1.left.left.left = el6

    return BinaryTree(el1)


with such.A("BinaryTree") as it:

    @it.should("depth_first_traversal")
    def test_depth_first():

        btree = btree1()

        acc = btree.depth_first_traversal(btree.head)
        expected = [1, 2, 4, 6, 5, 3]
        it.assertEqual(acc, expected)

    @it.should("breadth_first_traversal")
    def test_breadth_first():

        btree = btree1()

        acc = btree.breadth_first_traversal(btree.head)
        expected = [1, 2, 3, 4, 5, 6]
        it.assertEqual(acc, expected)


it.createTests(globals())

