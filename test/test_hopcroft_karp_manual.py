from src.graph import Graph
from src.matching.hopcroft_karp_manual import hopcroft_karp


def test_hopcroft_karp_manual():
    g = Graph(6, directed=False)

    # Partición bipartita:
    U = {0, 1, 2}
    V = {3, 4, 5}

    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)

    match = hopcroft_karp(g, U, V)

    # Matching máximo tiene 3 pares (6 elementos en el diccionario bidireccional)
    assert len(match) == 6

    assert match[0] in {3, 4}
    assert match[1] in {3, 5}
    assert match[2] == 4
