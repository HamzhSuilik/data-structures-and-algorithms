from graph.graph import Graph


def test_0():
    actual = None
    expected = None
    assert actual == expected

# Node can be successfully added to the graph
def test_1():
    graph = Graph()
    actual = graph.add_node('first node').value
    expected = 'first node'
    assert actual == expected

# An edge can be successfully added to the graph
def test_2():
    graph = Graph()
    start = graph.add_node('first node')
    end = graph.add_node('edge')
    graph.add_edge(start , end , 0)
    actual = graph._adjacency_list[start][0].vertex
    expected = end
    assert actual == expected
# A collection of all nodes can be properly retrieved from the graph
def test_3():
    graph = Graph()
    v1 = graph.add_node('first node')
    v2 = graph.add_node('second node')
    v3 = graph.add_node('last node')
    actual = graph.get_nodes()
    expected = {v1:0,v2:0,v3:0}.keys()
    assert actual == expected
# All appropriate neighbors can be retrieved from the graph
def test_4():
    graph = Graph()
    vertex = graph.add_node('first node')
    edge_1 = graph.add_node('edge node 1')
    edge_2 = graph.add_node('edge node 2')
    graph.add_edge(vertex , edge_1 , 0)
    graph.add_edge(vertex , edge_2 , 0)


    actual = graph.get_neighbors(vertex)[0].vertex
    expected = edge_1
    assert actual == expected

    actual = graph.get_neighbors(vertex)[1].vertex
    expected = edge_2
    assert actual == expected

# Neighbors are returned with the weight between nodes included
def test_5():
    graph = Graph()
    vertex = graph.add_node('first node')
    edge_1 = graph.add_node('edge node 1')
    edge_2 = graph.add_node('edge node 2')
    graph.add_edge(vertex , edge_1 , 0)
    graph.add_edge(vertex , edge_2 , 1)


    actual = graph.get_neighbors(vertex)[0].weight
    expected = 0
    assert actual == expected

    actual = graph.get_neighbors(vertex)[1].weight
    expected = 1
    assert actual == expected
# The proper size is returned, representing the number of nodes in the graph
def test_6():
    graph = Graph()
    graph.add_node('first node')
    graph.add_node('node')
    graph.add_node('node')
    graph.add_node('node')

    actual = graph.size()
    expected = 4
    assert actual == expected

# A graph with only one node and edge can be properly returned
def test_7():
    graph = Graph()
    vertex = graph.add_node('first node')

    actual = graph.get_nodes()
    expected = {vertex:0}.keys()

    assert actual == expected
# An empty graph properly returns null
def test_8():
    graph = Graph()

    actual = graph.get_nodes()
    expected = None

    assert actual == expected


print('')
