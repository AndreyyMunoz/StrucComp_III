from src.graph import Graph
from src.components.kosaraju_scc import kosaraju_scc


def test_kosaraju_scc():
    # Grafo dirigido con tres SCCs: {0,1,2}, {3}, {4,5}
    g = Graph(6, directed=True)

    # SCC 1
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    # Aristas hacia otras SCC
    g.add_edge(2, 3)

    # SCC 2 (solo nodo 3)

    # SCC 3
    g.add_edge(4, 5)
    g.add_edge(5, 4)

    sccs = [set(c) for c in kosaraju_scc(g)]

    assert set([0, 1, 2]) in sccs
    assert set([3]) in sccs
    assert set([4, 5]) in sccs
    assert len(sccs) == 3
