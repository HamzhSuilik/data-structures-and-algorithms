from stacks_and_queues.stacks_and_queues import Node , Stack , Queue

# Can successfully push onto a stack
def test_stacks_and_queues_1 ():
    stack = Stack()
    stack.push('a')
    actual = stack.top.value
    expected = 'a'
    assert actual == expected
# Can successfully push multiple values onto a stack
def test_stacks_and_queues_2 ():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    actual = stack.top.value
    expected = 'c'
    assert actual == expected
# Can successfully pop off the stack
def test_stacks_and_queues_3 ():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.pop()
    actual = stack.top.value
    expected = 'b'
    assert actual == expected
# Can successfully empty a stack after multiple pops
def test_stacks_and_queues_4 ():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected
# Can successfully peek the next item on the stack
def test_stacks_and_queues_5 ():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    actual = stack.peek()
    expected = 'c'
    assert actual == expected
# Can successfully instantiate an empty stack
def test_stacks_and_queues_6 ():
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected
# Calling pop or peek on empty stack raises exception
def test_stacks_and_queues_7 ():
    stack = Stack()
    actual = stack.pop()
    expected = None
    assert actual == expected
# Can successfully enqueue into a queue
def test_stacks_and_queues_8 ():
    queue = Queue()
    queue.enquene('a')
    actual = queue.front.value
    expected = 'a'
    assert actual == expected
# Can successfully enqueue multiple values into a queue
def test_stacks_and_queues_9 ():
    queue = Queue()
    queue.enquene('a')
    queue.enquene('b')
    queue.enquene('c')
    actual_1 = queue.front.value
    expected_1 = 'a'
    actual_2 = queue.rear.value
    expected_2 = 'c'
    assert actual_1 == expected_1 and actual_2 == expected_2
# Can successfully dequeue out of a queue the expected value
def test_stacks_and_queues_10 ():
    queue = Queue()
    queue.enquene('a')
    queue.enquene('b')
    queue.enquene('c')
    queue.dequeue()
    actual = queue.front.value
    expected = 'b'
    assert actual == expected
# Can successfully peek into a queue, seeing the expected value
def test_stacks_and_queues_11 ():
    queue = Queue()
    queue.enquene('a')
    queue.enquene('b')
    queue.enquene('c')
    actual = queue.peek()
    expected = 'a'
    assert actual == expected
# Can successfully empty a queue after multiple dequeues
def test_stacks_and_queues_12 ():
    queue = Queue()
    queue.enquene('a')
    queue.enquene('b')
    queue.enquene('c')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.peek()
    expected = None
    assert actual == expected
# Can successfully instantiate an empty queue
def test_stacks_and_queues_13 ():
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected
# Calling dequeue or peek on empty queue raises exception
def test_stacks_and_queues_14 ():
    queue = Queue()
    actual = queue.peek()
    expected = None
    assert actual == expected
