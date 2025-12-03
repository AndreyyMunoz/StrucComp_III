# src/ui/actions_graph.py

from src.core.app_state import AppState
from src.core.validators import parse_edge_line
from src.graph import Graph


def action_create_graph():
    state = AppState()

    try:
        n = int(input("Número de nodos (usa 1..n): "))
        if n <= 0:
            print("❌ Debes ingresar un número positivo.")
            return
    except:
        print("❌ Entrada inválida.")
        return

    directed = input("¿Dirigido? (s/n): ").strip().lower() == "s"
    g = Graph(n, directed)

    print("Ingresa aristas en formato: u v [peso] (nodos 1..n)")
    print("Escribe 'done' para terminar.\n")

    while True:
        line = input("arista> ").strip()
        if line.lower() == "done":
            break

        try:
            u, v, w = parse_edge_line(line, g)
            g.add_edge(u, v, w)
            print(f"  ✔ arista añadida: {u+1} -> {v+1}  (w={w})")  # mostramos 1..n
        except Exception as e:
            print("  ❌", e)

    state.graph = g
    state.last_matching = None
    state.U = None
    state.V = None

    print("✔ Grafo creado con nodos 1..n (internamente 0..n-1).")
    
def action_show_graph():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado. Usa la opción para crear uno.")
        return
    print("--- Grafo actual ---")
    print(state.graph)
    print("--------------------")