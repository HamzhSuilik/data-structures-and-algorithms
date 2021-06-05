class Node:
  def __init__(self, data):
    self.data=data
    self.next=None


class LinkedList:

    def __init__(self):
        # initialization here
        self.head=None

    # adds a new node with the given value to the end of the list
    def insert (self, value):
      new_node = Node(value)
      if self.head is None :
        self.head = new_node
        self.first_node = new_node
        return 0

      current_node =self.head
      while current_node.next :
        current_node=current_node.next
      current_node.next=new_node

    def includes (self, key):
        current_node =self.head

        while current_node:
            if key == current_node.data:
                return True
            current_node=current_node.next
        return False

    def __str__ (self):
        current_node =self.head
        text =''
        while current_node:
            text = text + '{ ' + current_node.data + ' } -> '
            current_node=current_node.next
        text = text + ' -> NULL'
        return text






# new_list = LinkedList()

# new_list.insert('1')
# new_list.insert('2')
# new_list.insert('3')
# new_list.insert('4')


# print()
# print('------------')
# print(new_list.includes('9'))


# print(new_list.kthFromEnd(2))


