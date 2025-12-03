# src/ui/actions_matching.py

from src.core.app_state import AppState
from src.core.display import list_to_user, matching_to_user, sets_to_user
from src.core.validators import parse_edge_line
from src.matching.hopcroft_karp_auto import hopcroft_karp_auto
from src.matching.hopcroft_karp_manual import hopcroft_karp_manual
from src.matching.maximal_matching_auto import maximal_matching_auto
from src.matching.maximal_matching_manual import maximal_matching_manual


# ---------------------------------------------------------
# MAXIMAL MATCHING (manual)
# ---------------------------------------------------------
def action_maximal_manual():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    try:
        print("\nPartición U:")
        U = parse_edge_line("  Ingresa nodos separados por espacio: ", state.graph)
        print("Partición V:")
        V = parse_edge_line("  Ingresa nodos separados por espacio: ", state.graph)
    except Exception as e:
        print("❌", e)
        return

    matching = maximal_matching_manual(state.graph, U, V)

    # Guardar estado interno
    state.last_matching = matching
    state.U = U
    state.V = V

    print("\n🔎 Maximal Matching (manual)")
    print("--------------------------------")
    print(" U =", sets_to_user(U))
    print(" V =", sets_to_user(V))
    print(" Matching =", matching_to_user(matching))
    print("--------------------------------\n")


# ---------------------------------------------------------
# MAXIMAL MATCHING (auto)
# ---------------------------------------------------------
def action_maximal_auto():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    res = maximal_matching_auto(state.graph)
    if res is None:
        print("❌ El grafo NO es bipartito.")
        return

    matching, U, V = res

    state.last_matching = matching
    state.U = U
    state.V = V

    print("\n🔎 Maximal Matching (automático)")
    print("--------------------------------")
    print(" U =", sets_to_user(U))
    print(" V =", sets_to_user(V))
    print(" Matching =", matching_to_user(matching))
    print("--------------------------------\n")


# ---------------------------------------------------------
# HOPCROFT–KARP (manual)
# ---------------------------------------------------------
def action_hopcroft_manual():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    try:
        print("\nPartición U:")
        U = parse_edge_line("  Ingresa nodos separados por espacio: ", state.graph)
        print("Partición V:")
        V = parse_edge_line("  Ingresa nodos separados por espacio: ", state.graph)
    except Exception as e:
        print("❌", e)
        return

    matching = hopcroft_karp_manual(state.graph, U, V)

    state.last_matching = matching
    state.U = U
    state.V = V

    print("\n🔎 Hopcroft–Karp (manual)")
    print("--------------------------------")
    print(" U =", sets_to_user(U))
    print(" V =", sets_to_user(V))
    # Hopcroft manual retorna dict
    print(" Matching =", {k + 1: v + 1 for k, v in matching.items()})
    print("--------------------------------\n")


# ---------------------------------------------------------
# HOPCROFT–KARP (auto)
# ---------------------------------------------------------
def action_hopcroft_auto():
    state = AppState()
    if state.graph is None:
        print("⚠ No hay grafo cargado.")
        return

    res = hopcroft_karp_auto(state.graph)
    if res is None:
        print("❌ El grafo NO es bipartito.")
        return

    matching, U, V = res

    state.last_matching = matching
    state.U = U
    state.V = V

    print("\n🔎 Hopcroft–Karp (automático)")
    print("--------------------------------")
    print(" U =", sets_to_user(U))
    print(" V =", sets_to_user(V))
    print(" Matching =", {k + 1: v + 1 for k, v in matching.items()})
    print("--------------------------------\n")
