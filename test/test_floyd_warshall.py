from src.graph import Graph
from src.shortest_paths.floyd_warshall import floyd_warshall


def test_floyd_warshall_basic():
    g = Graph(4, directed=True)
    g.add_edge(0, 1, 3)
    g.add_edge(1, 2, 8)
    g.add_edge(0, 3, 5)
    g.add_edge(3, 2, 2)

    dist = floyd_warshall(g)

    assert dist[0][2] == 7
    assert dist[0][1] == 3
    assert dist[0][3] == 5


def test_floyd_warshall_undirected():
    g = Graph(3, directed=False)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 6)

    dist = floyd_warshall(g)

    assert dist[0][2] == 10
    assert dist[2][0] == 10
