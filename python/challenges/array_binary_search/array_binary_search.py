
def BinarySearch(arr,key):
    index = 0
    for i in arr :
        if (i==key):
            return index
        index+=1
    return -1
