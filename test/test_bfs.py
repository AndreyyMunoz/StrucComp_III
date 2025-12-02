from src.graph import Graph
from src.traversals.bfs import bfs


def test_bfs_unweighted_undirected():
    # Grafo no dirigido, no ponderado
    g = Graph(4, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    assert bfs(g, 0) == [0, 1, 2, 3]


def test_bfs_directed():
    # Grafo dirigido
    g = Graph(4, directed=True)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)

    assert bfs(g, 0) == [0, 1, 2, 3]


def test_bfs_weighted_graph():
    # Grafo ponderado (BFS ignora peso pero debe funcionar)
    g = Graph(3)
    g.add_edge(0, 1, 10)
    g.add_edge(1, 2, 5)

    assert bfs(g, 0) == [0, 1, 2]
