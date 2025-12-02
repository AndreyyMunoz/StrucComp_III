from src.graph import Graph


def build_graph_from_adj_matrix(matrix, directed=False):
    """
    Construye un grafo a partir de una matriz de adyacencia.

    La matriz debe ser de tamaño n x n.
    Se considera:
        - 0 o None como ausencia de arista
        - Cualquier número > 0 como peso
        - También permite usar float('inf') para indicar ausencia

    Parámetros:
    - matrix: matriz cuadrada con pesos o 0
    - directed: True si el grafo es dirigido

    Regresa:
    - g: objeto Graph
    """
    n = len(matrix)
    g = Graph(n, directed=directed)

    for u in range(n):
        for v in range(n):
            w = matrix[u][v]

            # No hay arista si:
            # - w es 0
            # - w es None
            # - w es inf
            if w == 0 or w is None:
                continue

            if w == float("inf"):
                continue

            g.add_edge(u, v, w)

    return g
