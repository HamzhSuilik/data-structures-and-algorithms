# ------ Queue -----------
class Node :
  def __init__(self,value):
    self.value = value
    self.next = None

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


class KNode:
  def __init__(self, value=None):
    self.value=value
    self.children=[]


class K_ary_Trees ():
    def __init__ (self,root):
        self.root = root


def FizzBuzzTree (tre):
    tree = tre
    if not tree.root :
        return
    queue = Queue()
    queue.enquene(tree.root)
    def order ():
        node = queue.dequeue()
        if node :
            # Fizz - Buzz
            if node.value % 3 == 0 and node.value % 5 == 0:
                node.value = 'FizzBuzz'
            elif node.value % 3 == 0:
                node.value = 'Fizz'
            elif node.value % 5 == 0 :
                node.value = 'Buzz'
            else :
                node.value = str(node.value)
            # ----------
            for i in node.children :
                queue.enquene(i)
            order()
    order()
    return tree


if __name__ == '__main__' :
    root = KNode(1)
    root.children.append(KNode(2))
    root.children.append(KNode(3))
    root.children.append(KNode(4))

    root.children[0].children.append(KNode(17))
    root.children[0].children.append(KNode(6))
    root.children[0].children.append(KNode(7))

    root.children[1].children.append(KNode(8))
    root.children[1].children.append(KNode(9))
    root.children[1].children.append(KNode(10))

    root.children[2].children.append(KNode(11))
    root.children[2].children.append(KNode(12))

    k_tree = K_ary_Trees(root)

    tree = FizzBuzzTree(k_tree)

    print (tree.root.children[0].children[0].value)

