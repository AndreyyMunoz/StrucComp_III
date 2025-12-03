# src/ui/actions_traversals.py

from src.core.app_state import AppState
from src.core.display import list_to_user
from src.core.validators import validate_node_user
from src.traversals.bfs import bfs
from src.traversals.dfs import dfs


def action_bfs():
    state = AppState()
    graph = state.graph
    if graph is None:
        print("⚠ No hay grafo cargado.")
        return

    try:
        s_user = int(input("Nodo inicio BFS (1..n): "))
        validate_node_user(graph, s_user)
        s = s_user - 1
    except Exception as e:
        print("❌", e)
        return

    order = bfs(graph, s)
    print("BFS:", list_to_user(order))


def action_dfs():
    state = AppState()
    graph = state.graph
    if graph is None:
        print("⚠ No hay grafo cargado.")
        return
    try:
        s_user = int(input("Nodo inicio DFS (1..n): "))
        validate_node_user(graph, s_user)
        s = s_user - 1
    except Exception as e:
        print("❌", e)
        return
    print("DFS order:", dfs(graph, s))
