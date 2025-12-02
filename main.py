#!/usr/bin/env python3

# Main interactive menu for graph algorithms project

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
from src.shortest_paths.dijkstra import dijkstra
from src.shortest_paths.floyd_warshall import floyd_warshall
from src.traversals.bfs import bfs
from src.traversals.dfs import dfs


def build_graph():
    n = int(input("Número de nodos: "))
    directed = input("¿Dirigido? (s/n): ").lower() == 's'
    g = Graph(n, directed)

    print("Ingresa aristas en formato: u v peso (o u v si no hay peso)")
    print("Escribe 'done' para terminar\n")

    while True:
        line = input("arista> ")
        if line.lower() == "done":
            break
        parts = line.split()
        if len(parts) == 2:
            u, v = map(int, parts)
            g.add_edge(u, v)
        elif len(parts) == 3:
            u, v, w = int(parts[0]), int(parts[1]), float(parts[2])
            g.add_edge(u, v, w)
        else:
            print("Formato inválido.")

    return g


def main():
    print("""
    =========================================
    🚀 Bienvenido al Laboratorio de
        Algoritmos en Grafos (Python)
    =========================================
    Elije una categoría para comenzar.
    """)

    menu = True
    graph = None

    while menu:
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
    [7] Floyd-Warshall

    --- MST ---
    [8] Kruskal
    [9] Prim

    --- Bipartito ---
    [10] Verificar si es bipartito
    [11] Colorear con two_color

    --- Matching ---
    [12] Maximal Matching (general)
    [13] Maximal Matching (manual U,V)
    [14] Maximal Matching (auto)
    [15] Hopcroft–Karp (manual)
    [16] Hopcroft–Karp (auto)

    [0] Salir
    """)

        opc = input("Opción> ")

        if opc == "0":
            print("Saliendo... ¡Hasta luego! 👋")
            break

        # Ensure graph exists
        if opc != "1" and graph is None:
            print("Primero debes crear o cargar un grafo (opción [1]).")
            continue

        # Option handlers
        if opc == "1":
            graph = build_graph()
            print("Grafo creado correctamente.")

        elif opc == "2":
            s = int(input("Nodo inicio BFS: "))
            print("Resultado BFS:", bfs(graph, s))

        elif opc == "3":
            s = int(input("Nodo inicio DFS: "))
            print("Resultado DFS:", dfs(graph, s))

        elif opc == "4":
            print("CC:", connected_components(graph))

        elif opc == "5":
            print("SCC:", kosaraju_scc(graph))

        elif opc == "6":
            s = int(input("Nodo inicio Dijkstra: "))
            print("Distancias:", dijkstra(graph, s))

        elif opc == "7":
            print("Matriz de distancias FW:")
            for row in floyd_warshall(graph):
                print(row)

        elif opc == "8":
            print("MST (Kruskal):", kruskal(graph))

        elif opc == "9":
            s = int(input("Nodo inicio Prim: "))
            print("MST (Prim):", prim(graph, s))

        elif opc == "10":
            print("¿Bipartito?:", is_bipartite(graph))

        elif opc == "11":
            print("two_color:", two_color(graph))

        elif opc == "12":
            print("Maximal matching general:", maximal_matching(graph))

        elif opc == "13":
            U = eval(input("Ingresa U (p.ej. {0,2,4}): "))
            V = eval(input("Ingresa V (p.ej. {1,3,5}): "))
            print("Maximal matching manual:", maximal_matching_manual(graph, U, V))

        elif opc == "14":
            res = maximal_matching_auto(graph)
            if res:
                matching, U, V = res
                print("U:", U)
                print("V:", V)
                print("Matching:", matching)
            else:
                print("El grafo no es bipartito.")

        elif opc == "15":
            U = eval(input("Ingresa U: "))
            V = eval(input("Ingresa V: "))
            print("Hopcroft–Karp manual:", hopcroft_karp(graph, U, V))

        elif opc == "16":
            res = hopcroft_karp_auto(graph)
            if res:
                match, U, V = res
                print("U:", U)
                print("V:", V)
                print("Matching:", match)
            else:
                print("El grafo no es bipartito.")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()