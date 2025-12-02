from src.graph import Graph
from src.bipartite.color_two import two_color


def test_two_color_success():
    # Grafo bipartito
    g = Graph(4, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    colors = two_color(g)

    assert colors is not None
    # Verificar que adyacentes tengan distinto color
    for u in range(g.n):
        for v, _ in g.adj[u]:
            assert colors[u] != colors[v]


def test_two_color_fail():
    # Ciclo impar (no bipartito)
    g = Graph(3, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    assert two_color(g) is None
