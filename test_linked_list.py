from typing import List, Optional
from nose2.tools import such  # type: ignore
from linked_list import LinkedList, Node


def ll_1():
    el1 = Node(3)
    el2 = Node(4)
    el3 = Node(5)
    el4 = Node(8)

    el1.next = el2
    el2.next = el3
    el3.next = el4
    el4.next = None
    return LinkedList(el1)


def ll_2():
    el1 = Node(2)
    el2 = Node(4)
    el3 = Node(8)
    el4 = Node(11)

    el1.next = el2
    el2.next = el3
    el3.next = el4
    el4.next = None

    return LinkedList(el1)


def ll_cycle():
    el1 = Node(2)
    el2 = Node(4)
    el3 = Node(8)
    el4 = Node(11)

    el1.next = el2
    el2.next = el3
    el3.next = el4
    el4.next = el2

    return LinkedList(el1)


with such.A("Linked list") as it:

    @it.should("reverse list")
    def test_reverse():
        ll = ll_1()
        ll.reverse()
        expected = [8, 5, 4, 3]
        it.assertEqual(list(ll), expected)

    @it.should("merge two sorted lists")
    def test_merge():
        ll1 = ll_1()
        ll2 = ll_2()
        result = list(ll1.merge(ll2))

        expected = [2, 3, 4, 4, 5, 8, 8, 11]
        it.assertEqual(result, expected)

    @it.should("delete index")
    def test_delete():
        ll1 = ll_1()
        _ = ll1.delete(2)

        expected = [3, 4, 8]
        it.assertEqual(list(ll1), expected)

    @it.should("should find a cycle")
    def test_is_cycle():
        ll = ll_cycle()
        result = ll.is_cycle()

        expected = True
        it.assertEqual(result, expected)

    @it.should("not find a cycle")
    def test_is_not_cycle():
        ll = ll_1()
        result = ll.is_cycle()

        expected = False
        it.assertEqual(result, expected)


it.createTests(globals())
