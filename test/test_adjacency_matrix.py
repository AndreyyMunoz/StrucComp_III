from src.representations.adjacency_matrix import build_graph_from_adj_matrix

matrix = [
    [0, 2, 0],
    [0, 0, 3],
    [4, 0, 0]
]

g = build_graph_from_adj_matrix(matrix, directed=True)
