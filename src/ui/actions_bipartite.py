# src/ui/actions_bipartite.py

from src.core.app_state import AppState
from src.bipartite.bipartite_check import is_bipartite
from src.bipartite.color_two import two_color

def action_is_bipartite():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return
    print("¿Bipartito?:", is_bipartite(state.graph))

def action_two_color():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return
    colors = two_color(state.graph)
    print("two_color:", colors)
