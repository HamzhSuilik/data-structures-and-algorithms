def reverseArray (arr):
    arr2 = []
    length = len(arr)
    for i in arr:
        arr2.append(arr[length-1])
        length -=1
    return arr2

