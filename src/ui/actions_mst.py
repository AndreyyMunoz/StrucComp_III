# src/ui/actions_mst.py

from src.core.app_state import AppState
from src.core.display import edges_to_user
from src.core.validators import validate_node_user
from src.mst.kruskal import kruskal
from src.mst.prim import prim


def action_kruskal():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    if state.graph.directed:
        print("⚠ Kruskal requiere grafo NO dirigido.")
        return

    mst = kruskal(state.graph)

    print("MST (Kruskal):")
    for u, v, w in edges_to_user(mst):
        print(f"({u}, {v}, {w})")


def action_prim():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    if state.graph.directed:
        print("⚠ Prim requiere grafo NO dirigido.")
        return

    try:
        s_user = int(input("Nodo inicio Prim (1..n): "))
        validate_node_user(state.graph, s_user)
        s = s_user - 1
    except Exception as e:
        print("❌", e)
        return

    mst = prim(state.graph, s)
    print("MST (Prim):")
    for u, v, w in edges_to_user(mst):
        print(f"({u}, {v}, {w})")
