from collections import deque

def is_bipartite(graph):
    """
    Verifica si un grafo es bipartito usando BFS.
    
    Parámetros:
    - graph: objeto Graph (dirigido o no dirigido)

    Returna:
    - True si el grafo es bipartito, False si NO lo es.
    """

    color = [-1] * graph.n  # -1 = no coloreado

    for start in range(graph.n):
        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0  # primer color

        while q:
            u = q.popleft()
            for v, _ in graph.adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False

    return True
