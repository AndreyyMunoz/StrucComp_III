from src.graph import Graph
from src.matching.maximal_matching_auto import maximal_matching_auto


def test_maximal_matching_auto():
    g = Graph(6, directed=False)

    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)

    result = maximal_matching_auto(g)
    assert result is not None

    matching, U, V = result

    assert U == {0, 1, 2}
    assert V == {3, 4, 5}

    assert len(matching) == 3

    mset = {frozenset(e) for e in matching}

    assert frozenset((0, 3)) in mset or frozenset((0, 4)) in mset
    assert frozenset((1, 3)) in mset or frozenset((1, 5)) in mset
    assert frozenset((2, 4)) in mset
