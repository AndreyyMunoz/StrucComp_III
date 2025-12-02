from src.graph import Graph

def kosaraju_scc(graph):
    """
    Calcula las componentes fuertemente conexas (SCC) usando Kosaraju.
    Parámetros:
    - graph: objeto Graph (directed=True)

    Regresa:
    - Lista de SCCs (cada una es lista de nodos)
    """
    n = graph.n
    visited = [False] * n
    order = []

    # 1) DFS para llenar el orden de finalización
    def dfs1(u):
        visited[u] = True
        for v, _ in graph.adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(n):
        if not visited[u]:
            dfs1(u)

    # 2) Construir el grafo transpuesto
    gt = Graph(n, directed=True)
    for u in range(n):
        for v, w in graph.adj[u]:
            gt.add_edge(v, u, w)

    visited = [False] * n
    sccs = []

    # 3) DFS sobre el grafo transpuesto, en orden inverso
    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v, _ in gt.adj[u]:
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(comp)

    return sccs
