import pytest
from tree.tree import Node,Queue,Tree,binary_search_tree,Tnode

def test_if_Can_successfully_instantiate_an_empty_tree():
    tree = Tree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_a_tree_with_a_single_root_node():
    tree = Tree()
    tree.root = Tnode(10)
    actual = tree.breadth_first()
    expected = [10]
    assert actual == expected

def test_left_child_and_right_child_properly_to_a_node():
    tree = binary_search_tree()
    tree.root = Tnode(10)
    tree.Add(5)
    tree.Add(15) 
    actual = tree.pre_order()
    expected = [10,5,15]
    assert actual == expected

def test_from_a_pre_order_traversal():
    tree = Tree()
    tree.root= Tnode(10)
    tree.root.left = Tnode(20)
    tree.root.right = Tnode(50)
    tree.root.left.left = Tnode(30)
    tree.root.left.right = Tnode(40)
    tree.root.right.left = Tnode(60)
    actual = tree.pre_order()
    expected = [10, 20, 30, 40, 50, 60]
    assert actual == expected

def test_collection_from_an_in_order_traversal():
    tree = Tree()
    tree.root= Tnode(10)
    tree.root.left = Tnode(20)
    tree.root.right = Tnode(50)
    tree.root.left.left = Tnode(30)
    tree.root.left.right = Tnode(40)
    tree.root.right.left = Tnode(60)
    actual = tree.in_order()
    expected = [30, 20, 40, 10, 60, 50]
    assert actual == expected

def test_from_a_post_order_traversal():
    tree = Tree()
    tree.root= Tnode(10)
    tree.root.left = Tnode(20)
    tree.root.right = Tnode(50)
    tree.root.left.left = Tnode(30)
    tree.root.left.right = Tnode(40)
    tree.root.right.left = Tnode(60)
    actual = tree.post_order()
    expected = [30, 40, 20, 60, 50, 10]
    assert actual == expected


def test_Returns_true_or_false():
    tree = binary_search_tree()
    tree.root= Tnode(10)
    tree.root.left = Tnode(20)
    tree.root.right = Tnode(50)
    tree.root.left.left = Tnode(30)
    tree.root.left.right = Tnode(40)
    tree.root.right.left = Tnode(60)
    actual = tree.Contains(77)
    expected = False
    assert actual == expected

    




   