from linked_list.linked_list import LinkedList

# from challenges.array_reverse.array_reverse import reverseArray


def test_import():
    assert LinkedList

def test_1 () :
    new_list = LinkedList()
    new_list.append('1')
    assert new_list.show_all() == '1-'

def test_2 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')
    assert new_list.show_all() == '1-2-3-4-'

def test_3 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')
    new_list.insertBefore('2','***')
    assert new_list.show_all() == '1-***-2-3-4-'

def test_4 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')
    new_list.insertBefore('1','***')
    assert new_list.show_all() == '***-1-2-3-4-'

def test_5 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')
    new_list.insertAfter('1','***')
    assert new_list.show_all() == '1-***-2-3-4-'

def test_6 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')
    new_list.insertAfter('4','***')
    assert new_list.show_all() == '1-2-3-4-***-'

# code challenge 7 tests

def test_1_code_challenge_7 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')

    assert new_list.kthFromEnd(7) == 'Not Exist'


def test_2_code_challenge_7 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')

    assert new_list.kthFromEnd(4) == 'Not Exist'

def test_3_code_challenge_7 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')

    assert new_list.kthFromEnd(-2) == 'Not Exist'

def test_4_code_challenge_7 () :
    new_list = LinkedList()
    new_list.append('1')


    assert new_list.kthFromEnd(0) == '1'

def test_5_code_challenge_7 () :
    new_list = LinkedList()
    new_list.append('1')
    new_list.append('2')
    new_list.append('3')
    new_list.append('4')

    assert new_list.kthFromEnd(2) == '2'
