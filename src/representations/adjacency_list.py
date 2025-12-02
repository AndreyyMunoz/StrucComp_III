from src.graph import Graph


def build_graph_from_adj_list(adj_list, directed=False):
    """
    Construye un grafo a partir de una lista de adyacencia.

    Parámetros:
    - adj_list: lista donde adj_list[u] = [(v, w), (v2, w2), ...]
    - directed: True si el grafo es dirigido

    Regresa:
    - g: objeto Graph
    """
    n = len(adj_list)
    g = Graph(n, directed=directed)

    for u in range(n):
        for v, w in adj_list[u]:
            g.add_edge(u, v, w)

    return g
