from challenges.graph_business_trip.graph_business_trip import graph_business_trip
from graph.graph import Graph
import pytest

def test_1(graph_sample):
    graph = graph_sample[0]
    city_1 = graph_sample[1][0]
    city_2 = graph_sample[1][1]
    city_3 = graph_sample[1][2]
    actual = graph_business_trip(graph,[city_1,city_2,city_3])
    expected = (True,100)
    assert actual == expected

def test_2(graph_sample):
    graph = graph_sample[0]
    city_1 = graph_sample[1][0]
    city_2 = graph_sample[1][1]
    city_5 = graph_sample[1][4]
    actual = graph_business_trip(graph,[city_1,city_2,city_5])
    expected = (False,0)
    assert actual == expected

def test_3(graph_sample):
    graph = graph_sample[0]
    city_1 = graph_sample[1][0]
    city_2 = graph_sample[1][1]
    city_3 = graph_sample[1][2]
    city_4 = graph_sample[1][3]
    city_5 = graph_sample[1][4]
    actual = graph_business_trip(graph,[city_1,city_2,city_3,city_4,city_5])
    expected = (True,280)
    assert actual == expected


@pytest.fixture
def graph_sample():
    graph = Graph()
    city_1 = graph.add_node('city_1')
    city_2 = graph.add_node('city_2')
    city_3 = graph.add_node('city_3')
    city_4 = graph.add_node('city_4')
    city_5 = graph.add_node('city_5')


    graph.add_edge(city_1 , city_2 , 40)
    graph.add_edge(city_1 , city_4 , 20)

    graph.add_edge(city_2 , city_1 , 40)
    graph.add_edge(city_2 , city_3 , 60)

    graph.add_edge(city_3 , city_2 , 60)
    graph.add_edge(city_3 , city_4 , 80)

    graph.add_edge(city_4 , city_1 , 20)
    graph.add_edge(city_4 , city_3 , 80)
    graph.add_edge(city_4 , city_5 , 100)

    graph.add_edge(city_5 , city_4 , 100)
    return (graph,[city_1,city_2,city_3,city_4,city_5])

print('****')
