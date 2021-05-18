from linked_list.linked_list import LinkedList


def zipLists(list_1 , list_2):
  node_1 = list_1.head
  node_2 = list_2.head
  merge_list = LinkedList()

  while node_1 or node_2 :
    if node_1 :
      merge_list.append(node_1.data)
      node_1=node_1.next
    if node_2 :
      merge_list.append(node_2.data)
      node_2=node_2.next
  return merge_list




# list_1 = LinkedList()

# list_1.append('1')
# list_1.append('3')
# list_1.append('2')



# list_2 = LinkedList()
# list_2.append('5')
# list_2.append('9')
# list_2.append('4')
# list_2.append('d')

# new_list = zipLists(list_1,list_2)
# new_list.print_list()
