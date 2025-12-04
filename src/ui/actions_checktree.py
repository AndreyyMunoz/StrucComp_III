# src/ui/actions_tree.py

from src.core.app_state import AppState
from src.check_tree.dfs_cycle_detect import has_cycle
from src.check_tree.edge_count_connectivity import is_connected_edge_count


def action_check_cycle():
    """Verifica si el grafo tiene ciclo (si tiene, NO es árbol)."""
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    result = has_cycle(state.graph)
    print("\n🔎 ¿Tiene ciclo?:", result)
    if result:
        print("El grafo tiene ciclo → NO es árbol.")
    else:
        print("No hay ciclo → Podría ser árbol (seguir verificando).")


def action_check_tree():
    """
    Verifica si el grafo es árbol usando:
    - conectividad por conteo de aristas (no dirigido)
    - fuerte conectividad (dirigido)
    """
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    # Primero revisamos si tiene ciclo
    if has_cycle(state.graph):
        print("\nNO es árbol: El grafo tiene ciclo.")
        return

    # Luego revisamos conectividad / fuerte conectividad
    connected = is_connected_edge_count(state.graph)

    print("\n🔎 ¿Es árbol?:", connected)
    if connected:
        print("🌳 ✔ Sí es árbol.")
    else:
        print("NO es árbol: No es (fuertemente) conexo.")
