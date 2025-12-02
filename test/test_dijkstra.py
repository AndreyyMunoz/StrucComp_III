from src.graph import Graph
from src.shortest_paths.dijkstra import dijkstra


def test_dijkstra_simple():
    # Grafo ponderado sencillo
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(0, 3, 1)
    g.add_edge(3, 4, 7)
    g.add_edge(4, 2, 1)

    dist = dijkstra(g, 0)

    assert dist == [0, 2, 3, 1, 8]


def test_dijkstra_directed():
    g = Graph(4, directed=True)
    g.add_edge(0, 1, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(0, 3, 10)
    g.add_edge(3, 2, 2)

    dist = dijkstra(g, 0)

    assert dist == [0, 3, 4, 10]
