try:
    from stacks_and_queues import Queue,Stack
except:
    from graph.stacks_and_queues import Queue,Stack

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

    def depth_first(self,root):
        visited = []
        items = []
        if not root :
            return []
        stack = Stack()
        stack.push(root)
        visited.append(root)

        def walk ():
            node = stack.pop().value
            items.append(node)
            for neighbor in self.get_neighbors(node) :
                if neighbor.vertex not in visited :
                    stack.push(neighbor.vertex)
                    visited.append(neighbor.vertex)
                    walk ()


        walk ()

        while not stack.isEmpty():
            items.append(stack.pop().value.value)
        return items


if __name__ == "__main__":
    # https://miro.com/app/board/o9J_l8KPhTQ=/
    graph = Graph()
    node_1 = graph.add_node('1')
    node_2 = graph.add_node('2')
    node_3 = graph.add_node('3')
    node_4 = graph.add_node('4')
    graph.add_edge(node_1 , node_2 , 0)
    graph.add_edge(node_1 , node_3 , 0)
    graph.add_edge(node_2 , node_4 , 0)

    print(node_1)
    print (graph.depth_first(node_1))

