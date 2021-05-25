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

  def peek (self):
    if self.top :
      return self.top.value

  def isEmpty(self):
    if not self.top :
      return True
    return False

class PseudoQueue :
  def __init__(self) :
    self.items = Stack()

  def enquene (self,value):
    self.items.push(value)

  def dequeue (self):
    # first-in, first-out
    node = self.items.top
    if node.next :
        while node :
            if not node.next.next :
                pop_val = node.next.value
                node.next = None
                return pop_val
            node = node.next
    else :
        last_value = self.items.top.value
        self.items = Stack()
        return last_value

  def peck (self):
      return self.items.top.value



  def __str__ (self):
    node = self.items.top
    text = ''
    while node :
        text = text +' -> '+ node.value
        node = node.next
    return text

