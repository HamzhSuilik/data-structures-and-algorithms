from challenges.array_binary_search.array_binary_search import BinarySearch


def test_array_binary_search_1():
    expected = 2
    actual = BinarySearch([4,8,15,16,23,42], 15)
    assert expected is actual, "Input is [4,8,15,16,23,42], 15 || your output is " + str(actual) + " || The output should be -1"



def test_array_binary_search_2():
    expected = -1
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    assert expected is actual, "Input is [11,22,33,44,55,66,77], 90 || your output is " + str(actual) + " || The output should be -1"


def test_array_binary_search_3():
    expected = -1
    actual = BinarySearch([1, 2, 3, 5, 6, 7], 4)
    assert expected is actual, "Input is [4,8,15,16,23,42], 15 || your output is " + str(actual) + " || The output should be -1"


