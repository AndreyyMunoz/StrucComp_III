# src/ui/actions_components.py

from src.components.connected_components import connected_components
from src.components.kosaraju_scc import kosaraju_scc
from src.core.app_state import AppState

# ---------------------------------------------------------
# Utilidades de impresión
# ---------------------------------------------------------

def _print_components(title, components):
    """
    Imprime componentes en formato:
        Componente 1: {1, 4, 7}
    Con conversión automática 0..n-1 → 1..n
    """
    print(f"\n🔍 {title}")
    print("-----------------------------------")

    if not components:
        print(" (vacío)")
        return

    for i, comp in enumerate(components, start=1):
        pretty = {u + 1 for u in comp}
        print(f" Componente {i}: {sorted(pretty)}")

    print("-----------------------------------\n")


# ---------------------------------------------------------
# Acciones principales
# ---------------------------------------------------------

def action_connected_components():
    state = AppState()

    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    comps = connected_components(state.graph)
    
    # ordenamos componentes y nodos dentro de cada componente
    comps = [sorted(c) for c in comps]
    comps.sort(key=lambda c: (len(c), c))

    _print_components("Componentes conectadas (CC)", comps)


def action_scc():
    state = AppState()

    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    sccs = kosaraju_scc(state.graph)

    # ordenar para legibilidad
    sccs = [sorted(c) for c in sccs]
    sccs.sort(key=lambda c: (len(c), c))

    _print_components("Componentes fuertemente conectadas (SCC)", sccs)
