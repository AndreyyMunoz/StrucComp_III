def dfs(graph, start):
    """
    Depth-First Search (DFS) recursivo.
    Funciona con grafos dirigidos/no dirigidos y ponderados/no ponderados.

    Parámetros:
    - graph: objeto Graph
    - start: nodo inicial

    Regresa:
    - lista con el orden de visita de los nodos
    """
    visited = [False] * graph.n
    order = []

    def explore(u):
        visited[u] = True
        order.append(u)
        for v, _ in graph.adj[u]:   # ignoramos peso
            if not visited[v]:
                explore(v)

    explore(start)
    return order
