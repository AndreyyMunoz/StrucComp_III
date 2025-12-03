# src/ui/actions_shortest_paths.py

from src.core.app_state import AppState
from src.core.validators import validate_node_user
from src.shortest_paths.dijkstra import dijkstra
from src.shortest_paths.floyd_warshall import floyd_warshall

# ---------------------------------------------------------
# Utilidades internas
# ---------------------------------------------------------

def _format_distance(d):
    """Convierte distancias internas a una representación legible."""
    return "∞" if d == float("inf") else f"{d:.2f}"


def _print_distance_table(dist, start_user):
    print(f"\n📍 Distancias mínimas desde el nodo {start_user}:")
    print("-" * 42)
    print(" Nodo | Distancia ")
    print("-" * 42)

    for user_node, d in enumerate(dist, start=1):
        print(f"  {user_node:4d} | {_format_distance(d):>9}")

    print("-" * 42)


def _print_floyd_table(matrix):
    n = len(matrix)
    print("\n📘 Matriz de distancias (Floyd–Warshall)")
    print("    " + " ".join(f"{i+1:>6}" for i in range(n)))
    print("   " + "-" * (7 * n))

    for i, row in enumerate(matrix):
        formatted = " ".join(f"{_format_distance(x):>6}" for x in row)
        print(f"{i+1:>3} | {formatted}")


# ---------------------------------------------------------
# Acciones CLI
# ---------------------------------------------------------

def action_dijkstra():
    state = AppState()

    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    try:
        user_s = int(input("Nodo inicio Dijkstra (1..n): "))
        validate_node_user(state.graph, user_s)
    except Exception as e:
        print("❌", e)
        return

    internal_s = user_s - 1

    dist = dijkstra(state.graph, internal_s)

    _print_distance_table(dist, user_s)


def action_floyd():
    state = AppState()

    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    matrix = floyd_warshall(state.graph)

    _print_floyd_table(matrix)
