def merge_sort (array):
  mid = len(array) // 2
  if mid > 0 :
    left = array[:mid]
    right = array[mid:]
    left = merge_sort (left)
    right = merge_sort (right)
  else :
    return array

  arr = []
  for l in left :
    for r in range(len(right)) :
      if right[r] != 'empty':
        if right[r] < l :
          pass
          arr.append(right[r])
          right[r] = 'empty'
    arr.append(l)

  for r in right :
    if r !='empty':
      arr.append(r)
  array = arr
  return arr




if __name__ =="__main__":
  arr = [11,5,3,6,18,9,10,22,99,100,7,47,21]
  final = merge_sort(arr)
  print(final)
