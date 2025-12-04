def has_cycle(graph):
    """
    Detecta si un grafo (dirigido o no dirigido) contiene ciclos usando DFS.

    Parámetros:
    - graph: objeto Graph con atributos:
      - n: número de nodos
      - adj: lista de adyacencia con tuplas (v, peso)
      - directed: True si es dirigido, False si es no dirigido

    Retorna:
    - True si el grafo contiene al menos un ciclo.
    - False si NO contiene ciclos.
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

            elif not graph.directed and v != parent:
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
