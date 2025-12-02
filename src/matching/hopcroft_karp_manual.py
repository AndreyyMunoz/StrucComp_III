from collections import deque


def hopcroft_karp_manual(graph, U, V):
    """
    Algoritmo Hopcroft-Karp (versión manual).
    Requiere que se pasen las particiones U y V explícitamente.

    Parámetros:
    - graph: Graph no dirigido
    - U: conjunto de nodos izquierda
    - V: conjunto de nodos derecha

    Retorna:
    - matching: diccionario {u: v, v: u}
    """

    INF = float("inf")

    pairU = {u: None for u in U}
    pairV = {v: None for v in V}
    dist = {}

    def bfs():
        q = deque()
        for u in U:
            if pairU[u] is None:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF

        dist[None] = INF

        while q:
            u = q.popleft()
            if dist[u] < dist[None]:
                for v, _ in graph.adj[u]:
                    if v in V:
                        if pairV[v] is None:
                            dist[None] = dist[u] + 1
                        elif dist[pairV[v]] == INF:
                            dist[pairV[v]] = dist[u] + 1
                            q.append(pairV[v])
        return dist[None] != INF

    def dfs(u):
        if u is not None:
            for v, _ in graph.adj[u]:
                if v in V:
                    if pairV[v] is None or (
                        dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])
                    ):
                        pairV[v] = u
                        pairU[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    while bfs():
        for u in U:
            if pairU[u] is None:
                dfs(u)

    matching = {}
    for u in U:
        if pairU[u] is not None:
            matching[u] = pairU[u]
            matching[pairU[u]] = u

    return matching
