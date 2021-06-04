# Challenge Summary
Write a breadth first traversal method which takes a Binary Tree as its unique input ,traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Whiteboard Process
![image](../white-bord/17.jpg?raw=true)

## Approach & Efficiency
**Big O :**
Time -> (n)
Space -> (2n)

## Solution
write method that tack self as argument
define new empty linked list
if the tree empty return empty linked list
write function to travel into the tree and use queue to save nodes then move the nodes values in the linked list
call the function and start with tree root
return the linked list
