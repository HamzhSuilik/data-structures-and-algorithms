from challenges.tree_intersection.tree_intersection import tree_intersection
from challenges.tree_intersection.tree import BinaryTree,TNode



def test_sort_1():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    tree_1 = BinaryTree(node1)

    node1 = TNode(3)
    node1.left = TNode(4)
    node1.right = TNode(5)
    tree_2 = BinaryTree(node1)

    actual = tree_intersection(tree_1,tree_2)
    expected = [3]

    assert set(actual) == set(expected)


def test_sort_2():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)
    tree_1 = BinaryTree(node1)

    node1 = TNode(7)
    node1.left = TNode(11)
    node1.right = TNode(2)
    node1.right.left = TNode(3)
    node1.right.right = TNode(9)
    node1.left.right = TNode(1)
    node1.left.left = TNode(13)
    tree_2 = BinaryTree(node1)

    actual = tree_intersection(tree_1,tree_2)
    expected = [1,2,3,7]

    assert set(actual) == set(expected)


def test_sort_3():
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(15)
    tree_1 = BinaryTree(node1)

    node1 = TNode(7)
    node1.left = TNode(11)
    node1.right = TNode(2)
    node1.right.left = TNode(3)
    tree_2 = BinaryTree(node1)

    actual = tree_intersection(tree_1,tree_2)
    expected = [2,3]

    assert set(actual) == set(expected)




