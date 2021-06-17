# Helper classes
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

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


class Hashtable :
    def __init__(self, size =1024):
        self.size = size
        self.buckets = []
        for i in range(size):
            self.buckets.append(None)

    def hash(self,key):
        # The same key should always produce the same hash code.
        sum = 0
        for char in key :
            sum+=ord(char)
        sum = (sum*23) % self.size
        return key

    def add(self,value,key):
        hashed_key = self.hash(key)
        if not self.buckets[hashed_key]:
            self.buckets[hashed_key] = LinkedList()
        self.buckets[hashed_key].insert([key,value])

    def get(self,key):
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key].head
        while node:
            node = node.next
            if key == node.data[0] :
                return node.data[1]

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.buckets[hashed_key] :
            return True
        return False





if __name__ == "__main__":
    print('MAIN')

