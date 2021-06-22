from challenges.left_join.left_join import left_join
from challenges.left_join.hashtable import Hashtable

def test_1():
    hash_1 = Hashtable(4)
    hash_1.add('key1','word1')
    hash_1.add('key2','word2')
    hash_1.add('key3','word3')

    hash_2 = Hashtable(4)
    hash_2.add('key1','word11')
    hash_2.add('key2','word22')
    hash_2.add('key3','word33')

    actual = left_join(hash_1,hash_2)
    expected = [
        ['key3','word3','word33'],
        ['key2','word2','word22'],
        ['key1','word1','word11'],
    ]
    assert actual == expected


def test_2():
    hash_1 = Hashtable(4)
    hash_1.add('key1','word1')
    hash_1.add('key2','word2')
    hash_1.add('key3','word3')
    hash_1.add('key4','word4')

    hash_2 = Hashtable(4)
    hash_2.add('key1','word11')
    hash_2.add('key2','word22')
    hash_2.add('key3','word33')

    actual = left_join(hash_1,hash_2)
    expected = [
        ['key3','word3','word33'],
        ['key2','word2','word22'],
        ['key1','word1','word11'],
        ['key4','word4',None],
    ]
    assert len(actual) == len(expected)


def test_3():
    hash_1 = Hashtable(8)
    hash_1.add('key1','word1')
    hash_1.add('key2','word2')
    hash_1.add('key3','word3')
    hash_1.add('key4','word4')
    hash_1.add('key5','word5')

    hash_2 = Hashtable(8)
    hash_2.add('key1','word11')
    hash_2.add('key2','word22')
    hash_2.add('key3','word33')
    hash_2.add('key6','word66')

    actual = left_join(hash_1,hash_2)
    expected = [
        ['key5','word55',None],
        ['key4','word4',None],
        ['key3','word3','word33'],
        ['key2','word2','word22'],
        ['key1','word1','word11'],
    ]
    assert len(actual) == len(expected)
