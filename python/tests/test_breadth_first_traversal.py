import pytest
from tree.tree import BinaryTree , BinarySearchTree , TNode , Stack

def test_1 (Tree):
    node1 = TNode(1)
    binary_tree = BinaryTree(node1)
    list = binary_tree.breadth_first_traversal()
    actual = list.__str__()
    expected = '1-'
    assert actual == expected

def test_2 (Tree):
    binary_tree = BinaryTree()
    list = binary_tree.breadth_first_traversal()
    actual = list.__str__()
    expected = ''
    assert actual == expected

def test_3 (Tree):
    list = Tree.breadth_first_traversal()
    actual = list.__str__()
    expected = '1-2-3-7-6-5-4-'
    assert actual == expected



@pytest.fixture
def Tree():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)

    #    1
    #    |
    #  --------
    #  |      |
    #  2      3
    #  |      |
    # ----  -----
    # |  |  |   |
    # 7  6  5   4

    binary_tree = BinaryTree(node1)
    return binary_tree
