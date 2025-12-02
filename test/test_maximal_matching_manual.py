from src.graph import Graph
from src.matching.maximal_matching_manual import maximal_matching_manual


def test_maximal_matching_manual():
    g = Graph(6, directed=False)

    U = {0, 1, 2}
    V = {3, 4, 5}

    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)

    matching = maximal_matching_manual(g, U, V)

    # El matching maximal tiene 3 pares
    assert len(matching) == 3

    # Convertimos a sets para permitir (u,v) u (v,u)
    mset = {frozenset(e) for e in matching}

    assert frozenset((0, 3)) in mset or frozenset((0, 4)) in mset
    assert frozenset((1, 3)) in mset or frozenset((1, 5)) in mset
    assert frozenset((2, 4)) in mset
