from hashtable.hashtable  import Hashtable
# Adding a key/value to your hashtable results in the value being in the data structure
def test_1():
    hashtable = Hashtable()
    actual = hashtable.add('python','hkutr')
    expected = True
    assert actual == expected

# Retrieving based on a key returns the value stored
def test_2():
    hashtable = Hashtable()
    hashtable.add('Name','jkyjk')
    actual = hashtable.get('jkyjk')
    expected = 'Name'
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_3():
    hashtable = Hashtable()
    hashtable.add('python','k')
    actual = hashtable.get('rr')
    expected = None
    assert actual == expected

# Successfully handle a collision within the hashtable
def test_4():
    hashtable = Hashtable()
    hashtable.add('python','az') # hash key = 941
    actual = hashtable.add('Java','za') # hash key = 941
    expected = True
    assert actual == expected

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_5():
    hashtable = Hashtable()
    hashtable.add('python','az') # hash key = 941
    hashtable.add('Java','za') # hash key = 941
    actual = hashtable.get('az')
    expected = 'python'
    assert actual == expected
    actual = hashtable.get('za')
    expected = 'Java'
    assert actual == expected
# Successfully hash a key to an in-range value
def test_6():
    hashtable = Hashtable()
    actual = hashtable.hash('ABAB')
    # A -> 65
    # B -> 66
    # sum = 65+66+65+66 = 262
    # sum * 23 = 6026
    # sum % size(1024) --> 906
    expected = 906
    assert actual == expected


