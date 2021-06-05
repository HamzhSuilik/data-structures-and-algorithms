## Singly Linked List
A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.


## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called insert , includes , `__str__`

## Approach & Efficiency
**Big O :**
- insert :
Time : O(1)
Space : O(1)
- includes :
Time : O(n)
Space : O(n)
- `__str__` :
Time : O(n)
Space : O(n)

## API
insert :  add new node to the linked list
includes :  search for key value in the linked list and return boolean value
`__str__` : print list of all node in the linked list start from head
