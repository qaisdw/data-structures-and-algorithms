from linked_list import Linkedlist


def test_linked_list():
    # Test instantiation of an empty linked list
    ll = Linkedlist()
    assert ll.head is None

    # Test inserting a single node
    ll.insert(1)
    assert ll.head.value == 1

    # Test head property pointing to the first node
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 3

    # Test inserting multiple nodes
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 1 } -> NULL"

    # Test finding an existing value
    assert ll.includes(2) is True

    # Test finding a non-existing value
    assert ll.includes(4) is False

    # Test returning a collection of all values
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 1 } -> NULL"

    # Test appending a node to the end
    ll.append(4)
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 1 } -> { 4 } -> NULL"

    # Test adding a node before a specific value
    ll.addBefore(5, 1)
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 5 } -> { 1 } -> { 4 } -> NULL"

    # Test adding a node after a specific value
    ll.addAfter(6, 2)
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 6 } -> { 5 } -> { 1 } -> { 4 } -> NULL"

    # Test deleting  a node in a specific value
    ll.insert(2)
    ll.delete(2)
    assert ll.to_string() == "head -> { 3 } -> { 2 } -> { 6 } -> { 5 } -> { 1 } -> { 4 } -> NULL"

    # Test if k is greater than the length of the linked list
    assert ll.kthFromEnd(7) == "Exception"

    # Test if k and the length of the list are the same
    assert ll.linkLength() == ll.kthFromEnd(3)

    # Test when k is not a positive integer
    assert ll.kthFromEnd(-2) == 2

    # “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    ll.insert(9)
    assert ll.kthFormEndIndex(6) == ll.linkLength()//2

    # Test if the linked list is of a size 1
    ll.delete(9)
    ll.delete(3)
    ll.delete(2)
    ll.delete(6)
    ll.delete(5)
    ll.delete(1)
    assert ll.linkLength() == 1

