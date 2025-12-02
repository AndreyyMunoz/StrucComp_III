from collections import deque

def two_color(graph):
    """
    Intenta colorear un grafo con 2 colores (0 y 1).
    
    Retorna:
    - color: lista con el color de cada nodo
    - None si el grafo NO es bipartito
    """

    color = [-1] * graph.n

    for start in range(graph.n):
        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0

        while q:
            u = q.popleft()
            for v, _ in graph.adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return None  # no es bipartito

    return color
