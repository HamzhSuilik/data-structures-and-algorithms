def replace_min(arr,pointer,num):
  min = arr[pointer]
  index = pointer
  for i in range(len(arr)-pointer):
    if arr[pointer + i] < min :
      min = arr[pointer + i]
      index = pointer + i
  arr[index] = num
  return min


def selection_sort(arr):
  for pointer in range(len(arr)):
    arr[pointer] = replace_min(arr,pointer,arr[pointer])


print (__name__)

if __name__ == "__main__":
  array = [2,1,99,88,100,14,5]
  print(array,'\n----------')
  selection_sort(array)
  print(array)


