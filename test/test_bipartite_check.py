from src.graph import Graph
from src.bipartite.bipartite_check import is_bipartite


def test_bipartite_true():
    # Grafo bipartito: 0--1--2--3
    g = Graph(4, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    assert is_bipartite(g) is True


def test_bipartite_false():
    # Grafo NO bipartito: ciclo impar (0--1--2--0)
    g = Graph(3, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    assert is_bipartite(g) is False
