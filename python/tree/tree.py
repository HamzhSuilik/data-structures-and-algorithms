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
    s=binary_tree.preOrder()
    ss = s.__str__()
    print (ss)


    print ('ok')
