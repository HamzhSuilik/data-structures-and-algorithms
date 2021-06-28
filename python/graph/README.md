# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
create a graph class which contains methods : add node , add edge , get nodes , get neighbors , size

## Approach & Efficiency
- add_node
    - Time -> O(1)
    - Space -> O(1)
- add_edge
    - Time -> O(1)
    - Space -> O(0)
- get_nodes
    - Time -> O(1)
    - Space -> O(0)
- get_neighbors
    - Time -> O(1)
    - Space -> O(0)
- size
    - Time -> O(1)
    - Space -> O(0)

## API
- add_node : method tack a value as argument and then create a vertex object and add it to the graph
- add_edge : method tack a tow vertex as argument and crete edge object of the second vertex and add it to the first vertex
- get_nodes : method that return all nodes in the graph
- get_neighbors : method tack a vertex as argument and return all edges related to the input
- size : method that returns the number of nodes in the graph
