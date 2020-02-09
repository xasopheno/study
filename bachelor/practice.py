def reverse_string(string: str):
    string_arr = list(string)
    result = [None] * len(string)

    for i, char in enumerate(string_arr):
        result[len(result) - i - 1] = char

    return ("").join(result)


assert reverse_string("hello") == "olleh"
assert reverse_string("") == ""
assert reverse_string("123") == "321"


def is_palendrome(string: str) -> bool:
    for i in range(len(string) // 2):
        if string[i] == string[len(string) - i - 1]:
            continue
        else:
            return False

    return True


assert is_palendrome("123") == False
assert is_palendrome("0l9l0") == True
assert is_palendrome("0rr0") == True


def findSubArrayWithSum(arr, target):
    index = 0
    total = 0
    while index < len(arr):
        for i in range(index, len(arr) - 1):
            total += arr[i]
            if total < target:
                continue
            if total == target:
                return index, i
        index += 1
        total = 0
    return -1, -1


assert findSubArrayWithSum([1, 2, 3, 7, 5], 12) == (1, 3)
assert findSubArrayWithSum([12, 3, 7, 5], 12) == (0, 0)
assert findSubArrayWithSum([1, 11, 7, 5], 12) == (0, 1)
assert findSubArrayWithSum([1, 1], 12) == (-1, -1)


def removeDuplications(string):
    seen = {}
    result = []
    for char in list(string):
        if char in seen:
            continue
        else:
            result += [char]
            seen[char] = True
    return ("").join(result)


assert removeDuplications("geeks for geeks") == "geks for"


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.value)


def BFS(node: Node, acc=[]):
    if len(acc) == 0:
        acc += [node.value]
    if node.left:
        acc += [node.left.value]
    if node.right:
        acc += [node.right.value]
    if node.left:
        acc == BFS(node.left, acc)
    if node.right:
        acc == BFS(node.right, acc)

    return acc


def BTDepth(node):
    if not node:
        return 0

    if node.left or node.right:
        return 1 + max(BTDepth(node.left), BTDepth(node.right))

    return 0


tree = Node(10)
tree.left = Node(7)
tree.left.right = Node(11)
tree.left.right.left = Node(14)
tree.left.right.left.right = Node(16)
tree.right = Node(39)

assert BTDepth(tree) == 4
assert BFS(tree) == [10, 7, 39, 11, 14, 16]


def minCoins(target):
    coins = [25, 10, 5, 1]
    for coin in coins:
        if coin > target:
            continue

    return 0


print(36)

# def isBST(node: Node):
# if node.left:
# if node.left.value > node.value:
# return False
# else:
# return isBST(node.left)
# if node.right.value < node.value:
# return False
# else:
# return isBST(node.right)
# return True


# tree2 = Node(12)
# tree2.left = Node(7)
# tree2.left.right = Node(11)
# tree2.right = Node(39)
# assert isBST(tree2) == True

