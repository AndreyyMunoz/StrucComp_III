import heapq

def prim(graph, start=0):
    """
    Algoritmo de Prim para construir el MST.
    Parámetros:
    - graph: objeto Graph (NO dirigido)
    - start: nodo inicial para iniciar el MST

    Retorna:
    - Lista de aristas del MST en formato (u, v, w)
    """

    visited = [False] * graph.n
    mst = []
    pq = []

    # Agregar todas las aristas desde el nodo inicial
    visited[start] = True
    for v, w in graph.adj[start]:
        heapq.heappush(pq, (w, start, v))

    while pq and len(mst) < graph.n - 1:
        w, u, v = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True
        mst.append((u, v, w))

        for x, w2 in graph.adj[v]:
            if not visited[x]:
                heapq.heappush(pq, (w2, v, x))

    return mst
