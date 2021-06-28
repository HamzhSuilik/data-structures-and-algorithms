try :
    from graph import Graph
except :
    from graph.graph import Graph



def graph_business_trip(graph,list):
    sum = 0
    for i in range(len(list)-1):
        city = list[i]
        next_city = list[i+1]
        edges = graph.get_neighbors(city)
        trip = False
        for edge in edges:
            if edge.vertex==next_city:
                sum += edge.weight
                trip = True
        if not trip:
            return (False,0)
    return (True,sum)


if __name__ == "__main__":
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

    output = graph_business_trip(graph , [city_1 , city_4 , city_3, city_2])

    print(output)

print('')
