# ui/menu.py

from src.ui.actions_bipartite import action_is_bipartite, action_two_color
from src.ui.actions_checkers import action_check_maximal, action_check_perfect
from src.ui.actions_components import action_connected_components, action_scc
from src.ui.actions_graph import action_create_graph, action_show_graph
from src.ui.actions_matching import *
from src.ui.actions_mst import action_kruskal, action_prim
from src.ui.actions_shortest_paths import action_dijkstra, action_floyd
from src.ui.actions_traversals import action_bfs, action_dfs
from src.ui.actions_checktree import action_check_cycle, action_check_tree


def run_menu():
    while True:
        print("""
        ===============================================
        🚀  Laboratorio Interactivo de Algoritmos en Grafos
        ===============================================

        [1] Crear / Cargar Grafo
        [2] Mostrar Grafo Actual

        --- 🔵 RECORRIDOS ---
        [3] BFS
        [4] DFS

        --- 🟢 COMPONENTES ---
        [5] Componentes Conectados (CC)
        [6] Componentes Fuertemente Conectados (SCC)

        --- 🟣 CAMINOS MÍNIMOS ---
        [7] Dijkstra
        [8] Floyd–Warshall

        --- 🟠 ÁRBOLES DE EXPANSIÓN MÍNIMA ---
        [9]  Kruskal
        [10] Prim

        --- 🟡 BIPARTITO ---
        [11] Verificar si es bipartito
        [12] Colorear con two_color

        --- 🔴 MATCHING ---
        [13] Maximal Matching (general)
        [14] Maximal Matching (manual U, V)
        [15] Maximal Matching (automático)

        [16] Hopcroft–Karp (manual)
        [17] Hopcroft–Karp (automático)

        --- 🧪 CHECKERS ---
        [18] Verificar Maximal Matching
        [19] Verificar Perfect Matching

        --- 🌳 ÁRBOLES ---
        [20] Verificar si tiene ciclo
        [21] Verificar si es Árbol

        [0] Salir
        """)

        opc = input("Opción: ").strip()

        if opc == "0":
            print("👋 Saliendo del laboratorio. ¡Hasta luego!")
            break

        # --- GRAFO ---
        elif opc == "1":   action_create_graph()
        elif opc == "2":   action_show_graph()

        # --- RECORRIDOS ---
        elif opc == "3":   action_bfs()
        elif opc == "4":   action_dfs()

        # --- COMPONENTES ---
        elif opc == "5":   action_connected_components()
        elif opc == "6":   action_scc()

        # --- CAMINOS MÍNIMOS ---
        elif opc == "7":   action_dijkstra()
        elif opc == "8":   action_floyd()

        # --- MST ---
        elif opc == "9":   action_kruskal()
        elif opc == "10":  action_prim()

        # --- BIPARTITO ---
        elif opc == "11":  action_is_bipartite()
        elif opc == "12":  action_two_color()

        # --- MATCHING ---
        elif opc == "13":  action_maximal_general()
        elif opc == "14":  action_maximal_manual()
        elif opc == "15":  action_maximal_auto()
        
        elif opc == "16":  action_hopcroft_manual()
        elif opc == "17":  action_hopcroft_auto()

        # --- CHECKERS ---
        elif opc == "18":  action_check_maximal()
        elif opc == "19":  action_check_perfect()

        # --- ÁRBOLES ---
        elif opc == "20":  action_check_cycle()
        elif opc == "21":  action_check_tree()

        else:
            print("❌ Opción inválida. Intenta otra vez.")
