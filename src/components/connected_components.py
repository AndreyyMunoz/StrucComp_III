def connected_components(graph):
    """
    Calcula las componentes conexas en un grafo NO dirigido.

    Parámetros:
    - graph: objeto Graph (directed=False)

    Regresa:
    - Lista de componentes, cada una es una lista de nodos.
    """
    visited = [False] * graph.n
    components = []

    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        for v, _ in graph.adj[u]:
            if not visited[v]:
                dfs(v, comp)

    for u in range(graph.n):
        if not visited[u]:
            comp = []
            dfs(u, comp)
            components.append(comp)

    return components
