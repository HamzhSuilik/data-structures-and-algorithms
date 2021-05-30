# Stacks and Queue
are a data structure array save values

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated with functions : push , pop , Peek , IsEmpty
Create a Queue class that has a front property. It creates an empty Queue when instantiated, with functions : Enqueue , Dequeue ,  Peek , IsEmpty


## Approach & Efficiency
Big O :
**Stack**
- push
Time -> (n)
Space -> (1)
- pop
Time -> (1)
Space -> (1)
- Peek
Time -> (1)
Space -> (1)
- IsEmpty
Time -> (1)
Space -> (1)
**Queue**
- Enqueue O(1)
Time -> (n)
Space -> (1)
- Dequeue
Time -> (1)
Space -> (1)

## API
- create data structure Stack based on principle First In Last Out , with functions : push , pop , Peek , IsEmpty
- create data structure Queue based on principle First In First Out , with functions : Enqueue to add new node at last od queue , Dequeue to remove first node on the class
