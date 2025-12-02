#!/usr/bin/env python3

import ast

from src.bipartite.bipartite_check import is_bipartite
from src.bipartite.color_two import two_color
from src.components.connected_components import connected_components
from src.components.kosaraju_scc import kosaraju_scc
from src.graph import Graph
from src.matching.hopcroft_karp_auto import hopcroft_karp_auto
from src.matching.hopcroft_karp_manual import hopcroft_karp
from src.matching.maximal_matching_auto import maximal_matching_auto
from src.matching.maximal_matching_manual import maximal_matching_manual
from src.mst.kruskal import kruskal
from src.mst.prim import prim
from src.perfect_max_match.greedy_maximal_check import is_maximal_matching
from src.perfect_max_match.perfect_matching_check import is_perfect_matching
from src.shortest_paths.dijkstra import dijkstra
from src.shortest_paths.floyd_warshall import floyd_warshall
from src.traversals.bfs import bfs
from src.traversals.dfs import dfs

# =======================================================
# UTILIDADES SEGURAS
# =======================================================

def read_set(prompt):
    """Lee un conjunto de forma segura sin usar eval()."""
    while True:
        try:
            value = ast.literal_eval(input(prompt))
            if isinstance(value, set):
                return value
            print("❌ Eso no es un conjunto. Ejemplo: {0,2,4}")
        except Exception:
            print("❌ Formato inválido. Ejemplo correcto: {0,2,4}")


def validate_node(graph, u):
    """Revisa que u esté en rango."""
    if u < 0 or u >= graph.n:
        print(f"❌ Error: el nodo {u} está fuera de rango (0–{graph.n - 1}).")
        return False
    return True


def convert_matching_dict_to_set(matching_dict):
    """
    Convierte matching estilo {u:v, v:u} a {(u,v)} sin duplicados.
    """
    seen = set()
    result = set()

    for u, v in matching_dict.items():
        edge = tuple(sorted((u, v)))
        if edge not in seen:
            result.add(edge)
            seen.add(edge)

    return result


# =======================================================
# CREAR GRAFO
# =======================================================

def build_graph():
    try:
        n = int(input("Número de nodos: "))
        if n <= 0:
            print("❌ Debes ingresar un número positivo.")
            return None
    except:
        print("❌ Entrada inválida.")
        return None

    directed = input("¿Dirigido? (s/n): ").lower() == 's'
    g = Graph(n, directed)

    print("\nIngresa aristas en formato: u v peso")
    print("O simplemente: u v (peso = 1)")
    print("Escribe 'done' para terminar.\n")

    while True:
        line = input("arista> ")
        if line.lower() == "done":
            break

        parts = line.split()
        if len(parts) not in (2, 3):
            print("❌ Formato inválido.")
            continue

        try:
            u, v = int(parts[0]), int(parts[1])
            if not (validate_node(g, u) and validate_node(g, v)):
                continue

            w = float(parts[2]) if len(parts) == 3 else 1
            g.add_edge(u, v, w)
        except:
            print("❌ Entrada inválida. Ejemplo: 0 1 3.5")

    print("✔ Grafo creado correctamente.\n")
    return g


# =======================================================
# MENÚ PRINCIPAL
# =======================================================

def main():
    print("""
    =========================================
    🚀 Bienvenido al Laboratorio de Grafos
    =========================================
    """)

    graph = None

    while True:
        print("""
    [1] Crear/Cargar grafo

    --- Recorridos ---
    [2] BFS
    [3] DFS

    --- Componentes ---
    [4] Componentes Conectados (CC)
    [5] Componentes Fuertemente Conectadas (SCC)

    --- Caminos Mínimos ---
    [6] Dijkstra
    [7] Floyd–Warshall

    --- MST ---
    [8] Kruskal
    [9] Prim

    --- Bipartito ---
    [10] Verificar bipartito
    [11] two_color

    --- Matching ---
    [12] Maximal Matching (AUTO)
    [13] Maximal Matching (MANUAL)
    [14] Hopcroft–Karp (MANUAL)
    [15] Hopcroft–Karp (AUTO)

    --- Checkers ---
    [16] Verificar si matching es MAXIMAL
    [17] Verificar si matching es PERFECTO

    [0] Salir
    """)

        opc = input("Opción> ").strip()

        if opc == "0":
            print("👋 Saliendo...")
            break

        # Si la opción requiere grafo
        if opc != "1" and graph is None:
            print("⚠ Primero debes crear un grafo (opción 1).")
            continue

        # =====================================================
        # OPCIONES
        # =====================================================

        if opc == "1":
            graph = build_graph()

        elif opc == "2":
            s = int(input("Nodo inicio BFS: "))
            if validate_node(graph, s):
                print("BFS:", bfs(graph, s))

        elif opc == "3":
            s = int(input("Nodo inicio DFS: "))
            if validate_node(graph, s):
                print("DFS:", dfs(graph, s))

        elif opc == "4":
            print("CC:", connected_components(graph))

        elif opc == "5":
            print("SCC:", kosaraju_scc(graph))

        elif opc == "6":
            s = int(input("Nodo inicio Dijkstra: "))
            if validate_node(graph, s):
                print("Distancias:", dijkstra(graph, s))

        elif opc == "7":
            print("Matriz FW:")
            for row in floyd_warshall(graph):
                print(row)

        elif opc == "8":
            print("MST (Kruskal):", kruskal(graph))

        elif opc == "9":
            s = int(input("Nodo inicio Prim: "))
            if validate_node(graph, s):
                print("MST (Prim):", prim(graph, s))

        elif opc == "10":
            print("¿Bipartito?:", is_bipartite(graph))

        elif opc == "11":
            print("two_color:", two_color(graph))

        # ------ MAXIMAL MATCHING AUTO ------
        elif opc == "12":
            res = maximal_matching_auto(graph)
            if res:
                matching, U, V = res
                print("U:", U)
                print("V:", V)
                print("Matching:", matching)
            else:
                print("❌ El grafo no es bipartito.")

        # ------ MAXIMAL MATCHING MANUAL ------
        elif opc == "13":
            U = read_set("Ingresa U (ej. {0,2,4}): ")
            V = read_set("Ingresa V (ej. {1,3,5}): ")
            print("Matching manual:", maximal_matching_manual(graph, U, V))

        # ------ HOPCROFT–KARP MANUAL ------
        elif opc == "14":
            U = read_set("Ingresa U: ")
            V = read_set("Ingresa V: ")
            print("HK manual:", hopcroft_karp(graph, U, V))

        # ------ HOPCROFT–KARP AUTO ------
        elif opc == "15":
            res = hopcroft_karp_auto(graph)
            if res is None:
                print("❌ No es bipartito.")
            else:
                matching, U, V = res
                print("U:", U)
                print("V:", V)
                print("Matching:", matching)

        # =====================================================
        # CHECKERS
        # =====================================================

        elif opc == "16":
            res = hopcroft_karp_auto(graph)
            if res is None:
                print("❌ No es bipartito.")
                continue
            matching_dict, U, V = res
            matching_set = convert_matching_dict_to_set(matching_dict)
            print("¿Es maximal?:", is_maximal_matching(graph.adj, matching_set))

        elif opc == "17":
            res = hopcroft_karp_auto(graph)
            if res is None:
                print("❌ No es bipartito.")
                continue
            matching_dict, U, V = res
            matching_set = convert_matching_dict_to_set(matching_dict)
            print("¿Es perfecto?:", is_perfect_matching(graph.adj, matching_set))

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
