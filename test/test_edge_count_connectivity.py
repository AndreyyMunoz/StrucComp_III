from src.graph import Graph
from src.check_tree.edge_count_connectivity import is_connected_edge_count


# ==============================
#      NO DIRIGIDOS
# ==============================

def test_undirected_tree_true():
    # Grafo NO dirigido que SÍ cumple conectividad mínima
    # 0 -- 1 -- 2
    g = Graph(3, directed=False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    result = is_connected_edge_count(g)
    print("\n[TEST PASSED] Árbol NO DIRIGIDO (es conexo y suficiente en aristas)"
          if result else "\n[TEST FAILED] Debería ser árbol NO DIRIGIDO")
    assert result is True


def test_undirected_tree_false():
    # Grafo NO dirigido que NO es árbol (desconectado)
    # 0 -- 1    2 (aislado)
    g = Graph(3, directed=False)
    g.add_edge(0, 1)
    # 2 queda aislado

    result = is_connected_edge_count(g)
    print("\n[TEST PASSED] NO es árbol NO DIRIGIDO (no es conexo)"
          if result is False else "\n[TEST FAILED] Debería NO ser árbol")
    assert result is False


# ==============================
#          DIRIGIDOS
# ==============================

def test_directed_tree_true():
    # Grafo DIRIGIDO fuertemente conexo lineal (como camino)
    # 0 -> 1 -> 2 -> 3, pero no regresa (esto NO sería fuertemente conexo)
    # Entonces para que sea considerado árbol en esta validación,
    # hacemos fuerte conectividad con aristas de regreso:

    g = Graph(4, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)

    result = is_connected_edge_count(g)
    print("\n[TEST PASSED] Árbol DIRIGIDO (fuertemente conexo)"
          if result else "\n[TEST FAILED] Debería ser árbol DIRIGIDO")
    assert result is True


def test_directed_tree_false():
    # Grafo DIRIGIDO NO fuertemente conexo
    # 0 -> 1 -> 2  (no puedes volver a 0 ni 1)
    g = Graph(3, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    result = is_connected_edge_count(g)
    print("\n[TEST PASSED] NO es árbol DIRIGIDO (no es fuertemente conexo)"
          if result is False else "\n[TEST FAILED] Debería NO ser árbol")
    assert result is False
