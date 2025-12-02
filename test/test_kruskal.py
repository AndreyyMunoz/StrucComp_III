from src.graph import Graph
from src.mst.kruskal import kruskal


def test_kruskal_simple_mst():
    # Grafo no dirigido
    g = Graph(4, directed=False)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 3)
    g.add_edge(0, 2, 2)
    g.add_edge(2, 3, 4)

    mst = kruskal(g)

    expected = {(0, 1, 1), (0, 2, 2), (2, 3, 4)}

    assert set(mst) == expected
