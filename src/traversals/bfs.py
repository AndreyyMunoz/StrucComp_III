from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search (BFS).
    Funciona con grafos dirigidos/no dirigidos y ponderados/no ponderados.

    Parámetros:
    - graph: objeto Graph
    - start: nodo inicial

    Regresa:
    - lista con el orden de visita de los nodos
    """
    visited = [False] * graph.n
    order = []
    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()
        order.append(u)

        for v, _ in graph.adj[u]:   # ignoramos el peso
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return order
