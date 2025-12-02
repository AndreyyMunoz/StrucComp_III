from src.graph import Graph
from src.matching.hopcroft_karp_auto import hopcroft_karp_auto


def test_hopcroft_karp_auto():
    g = Graph(6, directed=False)

    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)

    result = hopcroft_karp_auto(g)
    assert result is not None

    match, U, V = result

    assert len(match) == 6
    assert U == {0, 1, 2}
    assert V == {3, 4, 5}

    assert match[0] in {3, 4}
    assert match[1] in {3, 5}
    assert match[2] == 4
