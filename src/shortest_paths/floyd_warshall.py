def floyd_warshall(graph):
    """
    Algoritmo Floyd-Warshall para todos los pares de caminos mínimos.

    Parámetros:
    - graph: objeto Graph (ponderado)

    Retorna:
    - matriz dist[n][n] con la distancia mínima entre cada par (i,j)
    """

    n = graph.n

    # Inicializar matriz de distancias
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Cargar las aristas del grafo
    for u in range(n):
        for v, w in graph.adj[u]:
            dist[u][v] = min(dist[u][v], w)

    # Algoritmo Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[j][i]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
