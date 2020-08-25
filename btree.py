from typing import Any, Optional, List


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.value}"


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def depth_first_traversal(self, node, acc=[]) -> List[int]:
        if node:
            acc += [node.value]
            acc = self.depth_first_traversal(node.left, acc)
            acc = self.depth_first_traversal(node.right, acc)
        return acc

    def breadth_first_traversal(self, head, acc=None) -> List[int]:
        if head:
            if not acc:
                acc = [head.value]
            for node in [head.left, head.right]:
                if node:
                    acc += [node.value]
            for node in [head.left, head.right]:
                self.breadth_first_traversal(node, acc)

            return acc
        else:
            return acc


if __name__ == "__main__":
    el1 = Node(1)
    el2 = Node(2)
    el3 = Node(3)
    el4 = Node(4)
    el5 = Node(5)
    el6 = Node(6)

    el1.left = el2
    el1.right = el3
    el1.left.left = el4
    el1.right.left = el5
    el1.right.right = el6

    btree = BinaryTree(el1)

    acc = btree.depth_first_traversal(btree.head)
    print(acc)
    acc = btree.breadth_first_traversal(btree.head)
    print(acc)

