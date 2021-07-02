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


# print(actual)

