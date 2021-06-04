from tree.tree import BinaryTree , BinarySearchTree , TNode , Stack

def test_1 ():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    binary_tree = BinaryTree(node1)

    maximum = binary_tree.find_maximum_value()
    actual = maximum
    expected = 3
    assert actual == expected

def test_2 ():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(88)
    node1.left.left = TNode(7)
    binary_tree = BinaryTree(node1)

    maximum = binary_tree.find_maximum_value()

    actual = maximum
    expected = 88
    assert actual == expected

def test_3 ():
    node1 = TNode(1)
    binary_tree = BinaryTree(node1)

    maximum = binary_tree.find_maximum_value()

    actual = maximum
    expected = 1
    assert actual == expected




print('ok')
