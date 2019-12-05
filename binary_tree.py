from typing import Any, Optional, List


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def depth_first_traversal(self, node: Optional[Any], acc: List = []) -> List[Node]:
        if node:
            acc += [node.value]
            acc = self.depth_first_traversal(node.left, acc)
            acc = self.depth_first_traversal(node.right, acc)
            return acc
        else:
            return acc

    def breadth_first_traversal(
        self, node: Optional[Any], acc: List = []
    ) -> List[Node]:
        if node:
            if len(acc) == 0:
                acc += [self.head.value]
            for i in [node.left, node.right]:
                if i:
                    acc += [i.value]
            for j in [node.left, node.right]:
                if j:
                    self.breadth_first_traversal(j, acc)
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

