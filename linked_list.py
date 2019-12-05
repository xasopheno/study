from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return f"{list(self)}"

    def __copy__(self):
        return LinkedList(self.head)

    def reverse(self):
        curr = self.head
        prev = None
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def delete(self, idx: int) -> Optional[Node]:
        if self.head.value == None:
            return None

        i = 0
        current_idx = self.head
        while i < idx - 1:
            current_idx = current_idx.next
            i += 1

        deleted = current_idx.next
        current_idx.next = current_idx.next.next

        return deleted

    def merge(self, other):
        if not self.head:
            return other
        if not other.head:
            return self

        curr_a = self.head
        curr_b = other.head

        result = LinkedList(Node(-1))
        curr_result = result.head

        while curr_a is not None and curr_b is not None:
            if curr_a < curr_b:
                curr_result.next = curr_a
                curr_result = curr_result.next
                curr_a = curr_a.next
            else:
                curr_result.next = curr_b
                curr_result = curr_result.next
                curr_b = curr_b.next

        while curr_a is not None:
            curr_result.next = curr_a
            curr_result = curr_result.next
            curr_a = curr_a.next

        while curr_b is not None:
            curr_result.next = curr_b
            curr_result = curr_result.next
            curr_b = curr_b.next

        result.head = result.head.next

        return result

    def is_cycle(self) -> bool:
        seen: List[Node] = []
        self.current = self.head
        while self.current:
            for node in seen:
                if self.current is node:
                    return True
            seen.append(self.current)
            self.current = self.current.next

        return False
