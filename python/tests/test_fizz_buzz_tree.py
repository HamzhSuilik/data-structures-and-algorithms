import pytest
from challenges.fizz_buzz_tree.fizz_buzz_tree import FizzBuzzTree , KNode , K_ary_Trees


def test_num(Tree):
    tree = FizzBuzzTree(Tree)
    actual = tree.root.children[2].value
    expected = '4'
    assert actual == expected

def test_Fizz(Tree):
    tree = FizzBuzzTree(Tree)
    actual = tree.root.children[1].value
    expected = 'Fizz'
    assert actual == expected

def test_buzz(Tree):
    tree = FizzBuzzTree(Tree)
    actual = tree.root.children[0].children[0].value
    expected = 'Buzz'
    assert actual == expected

def test_fuzzbuzz(Tree):
    tree = FizzBuzzTree(Tree)
    actual = tree.root.children[2].children[1].value
    expected = 'FizzBuzz'
    assert actual == expected

def test_empty(Tree):
    tree = K_ary_Trees(KNode())
    actual = tree.root.value
    expected = None
    assert actual == expected

@pytest.fixture
def Tree():
    root = KNode(1)
    root.children.append(KNode(2))
    root.children.append(KNode(3))
    root.children.append(KNode(4))

    root.children[0].children.append(KNode(5))
    root.children[0].children.append(KNode(6))
    root.children[0].children.append(KNode(7))

    root.children[1].children.append(KNode(8))
    root.children[1].children.append(KNode(9))
    root.children[1].children.append(KNode(10))

    root.children[2].children.append(KNode(11))
    root.children[2].children.append(KNode(15))

    k_tree = K_ary_Trees(root)
    return k_tree

print('ok')
