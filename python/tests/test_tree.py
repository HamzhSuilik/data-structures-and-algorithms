import pytest
from tree.tree import BinaryTree , BinarySearchTree , TNode , Stack

def test_1 (Tree):
    actual = '0'
    expected = '0'
    assert actual == expected

# Can successfully instantiate an empty tree
def test_1 ():
    binary_tree = BinaryTree()
    actual = binary_tree.root
    expected = None
    assert actual == expected
# Can successfully instantiate a tree with a single root node
def test_2 ():
    node = TNode(1)
    binary_tree = BinaryTree(node)
    actual = binary_tree.root
    expected = node
    assert actual == expected

    actual = binary_tree.root.value
    expected = 1
    assert actual == expected
# Can successfully add a left child and right child to a single root node
def test_3 ():
    node = TNode(1)
    node.left = TNode(2)
    node.right = TNode(3)
    binary_tree = BinaryTree(node)

    actual = binary_tree.root.left.value
    expected = 2
    assert actual == expected

    actual = binary_tree.root.right.value
    expected = 3
    assert actual == expected

# Can successfully return a collection from a preorder traversal
def test_4 ():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)
    binary_tree = BinaryTree(node1)


    actual = binary_tree.preOrder().__str__()
    expected = '-> 4 -> 5 -> 3 -> 6 -> 7 -> 2 -> 1 -> None'
    assert actual == expected


# Can successfully return a collection from an inorder traversal
def test_5 ():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)
    binary_tree = BinaryTree(node1)


    actual = binary_tree.inOrder().__str__()
    expected = '-> 4 -> 3 -> 5 -> 1 -> 6 -> 2 -> 7 -> None'
    assert actual == expected
# Can successfully return a collection from a postorder traversal
def test_6 ():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)
    binary_tree = BinaryTree(node1)


    actual = binary_tree.postOrder().__str__()
    expected = '-> 1 -> 3 -> 4 -> 5 -> 2 -> 6 -> 7 -> None'
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




