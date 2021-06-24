def Vertex(value):
    return value

class graph:
    def __init__(self) -> None:
        self._adjacency_list = {}

    def add_node (self , value):
        # value = Vertex (value)
        self._adjacency_list[value] = []
        return value

    def add_edge (self, edge , value):
        pass

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self):
        pass

    def size(self):
        return len(self._adjacency_list)

