# Challenge Summary
In a breadth first traversal, you are starting at a specific vertex/node. This node must be specified when calling the BreadthFirst() method. The breadth-first traversal of a graph is like that of a tree, with the exception that graphs can have cycles.

## Whiteboard Process
![image](../white-bord/36.jpg?raw=true)

## Approach & Efficiency
BigO :
Time : O(n)
Space : O(n)

## Solution
- the breadth first travels need queue because the queue principle is First In First Out , so I use a Queue data structure to order the graph nodes before adding the to the result list
- and it is important to use a visited list , to prevent re cycle in the graph



# Pull Request
https://github.com/HamzhSuilik/data-structures-and-algorithms/issues/45

- [x] import Queue map class
- [x] write breadth_first method
- [x] prepare README file
- [x] prepare whiteboard
- [x] create test units
