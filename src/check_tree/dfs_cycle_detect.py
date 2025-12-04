def has_cycle(graph):
    """
    Detecta si un grafo tiene ciclos utilizando DFS.

    Parámetros:
    - graph: objeto Graph (dirigido o no dirigido)

    Retorna:
    - True si el grafo contiene un ciclo, False si NO lo contiene.
    """

    visited = [False] * graph.n
    rec_stack = [False] * graph.n 

    def dfs(u, parent):
        visited[u] = True
        rec_stack[u] = True

        for v, _ in graph.adj[u]:
            
            if not visited[v]:
                if dfs(v, u):
                    return True

            elif parent != v and not graph.directed:
                return True

            elif graph.directed and rec_stack[v]:
                return True

        rec_stack[u] = False
        return False

    for i in range(graph.n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False
