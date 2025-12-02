from src.graph import Graph
from src.components.connected_components import connected_components


def test_connected_components_simple():
    # Grafo NO dirigido con dos componentes: {0,1,2} y {3,4}
    g = Graph(5, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)

    comps = connected_components(g)

    # Para evitar problemas de orden, usamos conjuntos
    comps = [set(c) for c in comps]

    assert set([0, 1, 2]) in comps
    assert set([3, 4]) in comps
    assert len(comps) == 2
