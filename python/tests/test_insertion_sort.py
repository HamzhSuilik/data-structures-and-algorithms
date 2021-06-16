from challenges.insertion_sort.insertion_sort import selection_sort

def test_sort_1():
    arr = [2,1,99,88,100,14,5]
    selection_sort(arr)
    actual = arr
    expected = [1, 2, 5, 14, 88, 99, 100]
    assert actual == expected

def test_sort_1():
    arr = [0,9,7,3,1]
    selection_sort(arr)
    actual = arr
    expected = [0, 1, 3, 7, 9]
    assert actual == expected


# edge case empty array
def test_sort_1():
    arr = []
    selection_sort(arr)
    actual = arr
    expected = []
    assert actual == expected
