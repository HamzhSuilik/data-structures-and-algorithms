def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    pivot = arr[-1]
    i = -1
    for pointer in range(len(arr)):
        if arr[pointer] <= pivot:
            i+=1
            arr[i],arr[pointer]=arr[pointer],arr[i]
    return quick_sort(arr[:i]) + quick_sort(arr[i:])


if __name__ == "__main__":
    print(quick_sort([2,1,99,88,100,14,5]))
