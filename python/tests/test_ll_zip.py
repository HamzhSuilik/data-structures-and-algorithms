from challenges.ll_zip.ll_zip import zipLists
from linked_list.linked_list import LinkedList

def test_zip_1():
    list_1 = LinkedList()
    list_1.append('1')
    list_1.append('3')
    list_1.append('2')


    list_2 = LinkedList()
    list_2.append('5')
    list_2.append('9')
    list_2.append('4')

    new_list = zipLists(list_1,list_2)
    assert new_list.show_all() == '1-5-3-9-2-4-'


def test_zip_2():
    list_1 = LinkedList()
    list_1.append('1')
    list_1.append('3')

    list_2 = LinkedList()
    list_2.append('5')
    list_2.append('9')
    list_2.append('4')

    new_list = zipLists(list_1,list_2)
    assert new_list.show_all() == '1-5-3-9-4-'

def test_zip_3():
    list_1 = LinkedList()
    list_1.append('1')
    list_1.append('3')
    list_1.append('2')

    list_2 = LinkedList()
    list_2.append('5')
    list_2.append('9')


    new_list = zipLists(list_1,list_2)
    assert new_list.show_all() == '1-5-3-9-2-'

