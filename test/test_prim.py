from src.graph import Graph
from src.mst.prim import prim


def test_prim_simple_mst():
    g = Graph(4, directed=False)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 3)
    g.add_edge(2, 3, 4)

    mst = prim(g, start=0)

    expected_edges = {(0, 1, 1), (0, 2, 2), (2, 3, 4)}

    assert set(mst) == expected_edges
