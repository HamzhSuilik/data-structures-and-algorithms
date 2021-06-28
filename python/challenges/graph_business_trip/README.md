# Challenge Summary
write a function that tack a graph and list of nodes as argument
the graph nodes represents locations on the map , and the edges between the node represents the transportation cost between the nodes
the function should return the total cost of travel between the input list nodes and True if there are trip between the nodes
## Whiteboard Process
![image](../../white-bord/37.jpg?raw=true)

## Approach & Efficiency
Time --> (n^n)
space --> (n)

## Solution
- define graph_business_trip function that tack a graph and list of nodes as argument
- select the trip routes and calculate the cost of the trip between the rotes
- return True and the sum of the cost if there ara trips between the input list
- return False and zero if there is no trips between the input list

# Pull Request :
https://github.com/HamzhSuilik/data-structures-and-algorithms/pull/44

- [x] import the Graph class
- [x] write graph_business_trip function
- [x] prepare README file
- [x] prepare whiteboard
- [x] create test units
