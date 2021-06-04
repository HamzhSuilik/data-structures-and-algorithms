# ---------- Linked list -------
class NodeLinkedList:
  def __init__(self, data):
    self.data=data
    self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    def append (self, value):
      new_node = NodeLinkedList(value)
      if self.head is None :
        self.head = new_node
        self.first_node = new_node
        return 0

      current_node =self.head
      while current_node.next :
        current_node=current_node.next
      current_node.next=new_node


    def __str__ (self):
        current_node =self.head
        text =''
        while current_node:
            text = text + current_node.data + '-'
            current_node=current_node.next
        return text

# ---------- Stack --------------
class Node :
  def __init__(self,value):
    self.value = value
    self.next = None

class Stack :
  def __init__ (self):
    self.top = None

  def push (self,value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node

  def pop(self):
    if self.top :
      temp = self.top
      self.top = self.top.next
      temp.next = None
    return temp

  def peek (self):
    if self.top :
      return self.top.value

  def isEmpty(self):
    if not self.top :
      return True
    return False

  def __str__(self):
      node_1 = self.top
      text = '-> '
      while node_1 is not None :
          text = text + node_1.value +' -> '
          node_1 = node_1.next
      text = text + 'None'
      return text

# ------ Queue -----------
class Queue :
  def __init__(self) :
    self.front = None
    self.rear = None

  def enquene (self,value):
    new_node = Node(value)
    if self.front :
      self.rear.next = new_node
      self.rear = new_node
    else :
      # we have an emtpy queue
      self.front = new_node
      self.rear = new_node

  def dequeue (self):
    if self.front :
      if not self.front.next :
        temp = self.front
        self.front = None
        temp.next = None
        return temp.value

      temp = self.front
      self.front = self.front.next
      temp.next = None
      return temp.value

  def peek(self):
    if self.front :
      return self.front.value

  def isEmpty (self):
    if self.front :
      return False
    return True

# -------------------------------
# *******************************

# -------------- Tree Data Structure -----------------

class TNode :
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree :
    def __init__(self,root=None) :
        self.root = root

    # traversal

    # Root -> Left -> Right
    def preOrder(self):
        stack = Stack()

        """ Pre-order traversal of our tree """
        def walk(root):
            stack.push(str(root.value))

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

        walk(self.root)

        return stack

    # Left -> Root -> Right
    def inOrder(self):
        stack = Stack()

        """ In-order traversal of our tree """
        def walk(root):

            if root.left:
                walk(root.left)

            stack.push(str(root.value))

            if root.right:
                walk(root.right)

        walk(self.root)

        return stack

    # Left -> Right -> Root
    def postOrder(self):
        stack = Stack()

        """ Post-order traversal of our tree """
        def walk(root):

            if root.left:
                walk(root.left)


            if root.right:
                walk(root.right)

            stack.push(str(root.value))

        walk(self.root)

        return stack

    # code challenge 16 : find maximum numerical value in the tree
    def find_maximum_value (self) :
        def walk(root,val):
            if root.left:
                if root.left.value > val :
                    val = walk(root.left,root.left.value)
                else :
                    val = walk(root.left,val)
            if root.right:
                if root.right.value > val :
                    val = walk(root.right,root.right.value)
                else :
                    val =walk(root.right,val)
            return val
        return walk(self.root,self.root.value)

    # code challenge 17
    def breadth_first_traversal (self):
        new_list = LinkedList()
        if not self.root :
            return new_list
        queue = Queue()
        queue.enquene(self.root)
        def order ():
            node = queue.dequeue()
            if node :
                new_list.append(str(node.value))
                if (node.left):
                    queue.enquene(node.left)
                if (node.right):
                    queue.enquene(node.right)
                order()
        order()
        return new_list

# Binary Search Tree (BST)
class  BinarySearchTree :
    def __init__(self,root=None) :
        self.root = root

      # Root -> Left -> Right
    def preOrder(self):
        stack = Stack()

        """ Pre-order traversal of our tree """
        def walk(root):
            stack.push(str(root.value))

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

        walk(self.root)

        return stack


    def add (self,value):
        pointer = self.root

        if pointer is None :
            self.root = TNode(value)
            return

        while pointer is not None :
            if pointer.value > value :
                if  pointer.left is None :
                    pointer.left = TNode(value)
                    return
                else :
                    pointer = pointer.left
            elif pointer.value < value :
                if  pointer.right is None :
                    pointer.right = TNode(value)
                    return
                else :
                    pointer = pointer.right
            else :
                return 'The value is already exists'





if __name__ == "__main__":
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)

    node1.right.left = TNode(5)
    node1.right.right = TNode(4)

    node1.left.right = TNode(6)
    node1.left.left = TNode(7)

    #     1
    #     |
    # --------
    # |      |
    # 2      3
    # |      |
    # ----  -----
    # |  |  |   |
    # 7  6  5   4


    binary_tree = BinaryTree(node1)
    binary_tree.breadth_first_traversal()



    print ('ok')
