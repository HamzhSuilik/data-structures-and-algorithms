from challenges.quick_sort.quick_sort import quick_sort

def test_sort_1():
    arr = [2,1,99,88,100,14,5]
    arr = quick_sort(arr)
    actual = arr
    expected = [1, 2, 5, 14, 88, 99, 100]
    assert actual == expected

def test_sort_2():
    arr = [0,9,7,3,1]
    arr = quick_sort(arr)
    actual = arr
    expected = [0, 1, 3, 7, 9]
    assert actual == expected


# edge case empty array
def test_sort_3():
    arr = []
    arr = quick_sort(arr)
    actual = arr
    expected = []
    assert actual == expected
