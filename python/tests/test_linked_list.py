from linked_list.linked_list import LinkedList



def test_import():
    assert LinkedList


# Can successfully instantiate an empty linked list
def test_1 () :
    new_list = LinkedList()
    actual = new_list.__str__()
    expected=' -> NULL'
    assert actual == expected

# Can properly insert into the linked list
def test_2 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    actual = new_list.__str__()
    expected='{ a } -> { b } ->  -> NULL'
    assert actual == expected
# The head property will properly point to the first node in the linked list
def test_3 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    actual = new_list.head.data
    expected='a'
    assert actual == expected
# Can properly insert multiple nodes into the linked list
def test_4 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    new_list.insert('c')
    new_list.insert('d')
    actual = new_list.__str__()
    expected='{ a } -> { b } -> { c } -> { d } ->  -> NULL'
    assert actual == expected
# Will return true when finding a value within the linked list that exists
def test_5 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    new_list.insert('c')
    actual = new_list.includes('a')
    expected= True
    assert actual == expected
# Will return false when searching for a value in the linked list that does not exist
def test_6 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    new_list.insert('c')
    actual = new_list.includes('z')
    expected= False
    assert actual == expected
# Can properly return a collection of all the values that exist in the linked list
def test_7 () :
    new_list = LinkedList()
    new_list.insert('a')
    new_list.insert('b')
    new_list.insert('c')
    actual = new_list.__str__()
    expected='{ a } -> { b } -> { c } ->  -> NULL'
    assert actual == expected

