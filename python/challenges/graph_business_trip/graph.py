class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

# class Queue :
#     pass

# class Stack :
#     pass

class Graph:
    def __init__(self) -> None:
        self._adjacency_list = {}

    def add_node (self , value):
        # New Vertex
        vertex = Vertex (value)
        # Add the Vertex to Graph
        self._adjacency_list[vertex] = []
        # Return the new vertex
        return vertex

    def add_edge (self, start_vertex , end_vertex ,  weight = 0):
        if start_vertex not in self._adjacency_list :
            raise KeyError("start vertex is not found in the graph")
        if end_vertex not in self._adjacency_list :
            raise KeyError("end vertex is not found in the graph")

        self._adjacency_list[start_vertex].append(Edge(end_vertex,weight))


    def get_nodes(self):
        if not self.size():
            return None
        return self._adjacency_list.keys()

    def get_neighbors(self,vertex):
        return self._adjacency_list.get(vertex , [] )

    def size(self):
        return len(self._adjacency_list)

    def breadth_first (self):
        pass


if __name__ == "__main__":
    graph = Graph()
    v1 = graph.add_node('first node')
    v2 = graph.add_node('second node')
    v3 = graph.add_node('last node')
    actual = graph.get_nodes()

    print({v1:0,v2:0,v3:0}.keys())
    print (actual)
