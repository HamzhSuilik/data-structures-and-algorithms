class Node:
  def __init__(self, data):
    self.data=data
    self.next=None


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head=None

    # adds a new node with the given value to the end of the list
    def append (self, value):
      new_node = Node(value)
      if self.head is None :
        self.head = new_node
        self.first_node = new_node
        return 0

      current_node =self.head
      while current_node.next :
        current_node=current_node.next
      current_node.next=new_node

    # add a new node with the given newValue immediately before the first value node
    def insertBefore(self,value, newVal):
      new_node = Node(newVal)

      node_1 = self.first_node
      node_2 = node_1

      if self.first_node.data == value :
        self.head = new_node
        new_node.next = node_1
        self.first_node = new_node
        return

      while node_1.data != value :
        node_2 = node_1
        node_1 = node_1.next
      new_node.next = node_1
      node_2.next = new_node


    # add a new node with the given newValue immediately after the first value node

    def insertAfter(self,value, newVal):
      new_node = Node(newVal)

      node_1 = self.first_node
      node_2 = node_1

      if self.first_node.data == value :
        new_node.next = node_1.next
        node_1.next = new_node
        return

      while node_1.data != value :
        node_1 = node_1.next
        node_2 = node_1.next

      node_1.next = new_node
      new_node.next = node_2




    def print_list(self):
      current_node =self.head

      while current_node:
         print(current_node.data)
         current_node=current_node.next

    def some_method(self):
        # method body here
        pass

    def __str__ (self):
        current_node =self.head
        text =''
        while current_node:
            text = text + current_node.data + '-'
            current_node=current_node.next
        return text

    def show_all (self):
        current_node =self.head
        text =''
        while current_node:
            text = text + current_node.data + '-'
            current_node=current_node.next
        return text


# new_list = LinkedList()

# new_list.append('1')
# new_list.append('2')
# new_list.append('3')
# new_list.append('4')
# new_list.insertBefore('1','ahahah')
# new_list.print_list()


# print(new_list.show_all())

# new_list = LinkedList()
# new_list.append('1')
# new_list.append('2')
# new_list.append('3')
# new_list.append('4')
# print( new_list.show_all() )
