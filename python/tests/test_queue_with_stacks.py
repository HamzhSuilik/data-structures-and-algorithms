import pytest
from challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_1 (pseudoQueue):
    actual = pseudoQueue.__str__()
    expected = ' -> 2 -> 1 -> 0'
    assert actual == expected

def test_2 (pseudoQueue):
    actual = pseudoQueue.dequeue()
    expected = '0'
    assert actual == expected

    actual = pseudoQueue.__str__()
    expected = ' -> 2 -> 1'
    assert actual == expected

def test_3 (pseudoQueue):
    pseudoQueue.dequeue()
    pseudoQueue.dequeue()
    pseudoQueue.dequeue()

    actual = pseudoQueue.__str__()
    expected = ''
    assert actual == expected

@pytest.fixture
def pseudoQueue():
    pq = PseudoQueue()
    pq.enquene('0')
    pq.enquene('1')
    pq.enquene('2')

    return pq



