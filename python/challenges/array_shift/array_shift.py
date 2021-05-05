def insertShiftArray(arr , num):
    length = int(len(arr) / 2)
    if(len(arr) % 2 ==1):
        length+=1
    arr.insert(length, num)
    return arr
