from src.graph import Graph
from src.traversals.dfs import dfs


def test_dfs_unweighted_undirected():
    # Grafo no dirigido, no ponderado
    g = Graph(5, directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    # El orden puede variar si se cambia el orden de inserción.
    assert dfs(g, 0) == [0, 1, 3, 2, 4]


def test_dfs_directed():
    # Grafo dirigido
    g = Graph(4, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    assert dfs(g, 0) == [0, 1, 2, 3]


def test_dfs_weighted():
    # Grafo ponderado debe comportarse igual
    g = Graph(3)
    g.add_edge(0, 1, 7)
    g.add_edge(1, 2, 20)

    assert dfs(g, 0) == [0, 1, 2]
