try:
    from stacks_and_queues import Queue
except:
    from graph.stacks_and_queues import Queue

class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

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

    def breadth_first (self,root):
        visited = []
        items = []
        if not root :
            return []
        queue = Queue()
        queue.enquene(root)
        visited.append(root)
        def walk ():
            if queue.isEmpty() :
                return
            node = queue.dequeue()
            items.append(node)
            for neighbor in self.get_neighbors(node) :
                if neighbor.vertex not in visited :
                    queue.enquene(neighbor.vertex)
                    visited.append(neighbor.vertex)
            walk ()
        walk ()
        return items




if __name__ == "__main__":
    graph = Graph()
    node_1 = graph.add_node('1')
    node_2 = graph.add_node('10')
    node_3 = graph.add_node('20')
    node_4 = graph.add_node('100')
    node_5 = graph.add_node('1000')
    node_6 = graph.add_node('2000')

    graph.add_edge(node_1 , node_2 , 0)
    graph.add_edge(node_1 , node_3 , 1)
    graph.add_edge(node_2 , node_4 , 1)
    graph.add_edge(node_2 , node_5 , 1)
    graph.add_edge(node_3 , node_6 , 1)

    # graph.add_edge(node_5 , node_3 , 1)
    graph.add_edge(node_6 , node_2 , 1)


    print (graph.breadth_first(node_1))

