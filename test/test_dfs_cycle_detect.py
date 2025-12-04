from src.graph import Graph
from src.check_tree.dfs_cycle_detect import has_cycle

def test_is_tree_true():
    # Árbol: 0 -> 1 -> 2
    g = Graph(3, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    # Árbol NO debe tener ciclo
    result = has_cycle(g)
    print("\n[TEST PASSED] SI ES ÁRBOL" if result is False else "\n[TEST FAILED] NO ES ÁRBOL")
    assert result is False  # Es árbol


def test_is_tree_false():
    # NO es árbol: 0 -> 1 -> 2 -> 0 (ciclo)
    g = Graph(3, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    # NO es árbol por ciclo
    result = has_cycle(g)
    print("\n[TEST PASSED] NO ES ÁRBOL" if result is True else "\n[TEST FAILED] SI ES ÁRBOL")
    assert result is True  # No es árbol
