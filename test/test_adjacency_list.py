from src.representations.adjacency_list import build_graph_from_adj_list

adj = [
    [(1, 1)],        # 0 → 1
    [(2, 5)],        # 1 → 2
    [(3, 2)],        # 2 → 3
    []
]

g = build_graph_from_adj_list(adj, directed=True)
