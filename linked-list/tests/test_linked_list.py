from linked_list import Linkedlist


def test_linked_list():
    # Test instantiation of an empty linked list
    ll = Linkedlist()
    assert ll.head == None

    # Test inserting a single node
    ll.insert("a")
    assert ll.head.value == "a"

    # Test head property pointing to the first node
    ll.insert("b")
    ll.insert("c")
    assert ll.head.value == "c"

    # Test inserting multiple nodes
    assert ll.to_string() == "{ c } -> { b } -> { a } -> NULL"

    # Test finding an existing value
    assert ll.includes("b") == True

    # Test finding a non-existing value
    assert ll.includes("d") == False

    # Test returning a collection of all values
    assert ll.to_string() == "{ c } -> { b } -> { a } -> NULL"
