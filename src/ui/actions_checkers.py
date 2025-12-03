# src/ui/actions_checkers.py

from src.core.app_state import AppState
from src.core.converters import dict_to_matching_set
from src.perfect_max_match.greedy_maximal_check import is_maximal_matching
from src.perfect_max_match.perfect_matching_check import is_perfect_matching


def action_check_maximal():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return
    if state.last_matching is None:
        print("⚠ No hay matching guardado. Ejecuta un algoritmo de matching primero.")
        return
    matching_set = dict_to_matching_set(state.last_matching)
    res = is_maximal_matching(state.graph.adj, matching_set)
    print("¿El último matching es maximal?:", res)

def action_check_perfect():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return
    if state.last_matching is None:
        print("⚠ No hay matching guardado. Ejecuta un algoritmo de matching primero.")
        return
    matching_set = dict_to_matching_set(state.last_matching)
    res = is_perfect_matching(state.graph.adj, matching_set)
    print("¿El último matching es perfecto?:", res)
