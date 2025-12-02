import heapq

def dijkstra(graph, start):
    """
    Algoritmo de Dijkstra para caminos más cortos desde un nodo origen.

    Parámetros:
    - graph: objeto Graph (debe ser ponderado)
    - start: nodo inicial

    Retorna:
    - dist: lista con la distancia mínima desde 'start' a cada nodo
    """

    dist = [float("inf")] * graph.n
    dist[start] = 0

    pq = [(0, start)]  # (costo, nodo)

    while pq:
        current_cost, u = heapq.heappop(pq)

        # Si es una entrada vieja, ignórala
        if current_cost > dist[u]:
            continue

        for v, w in graph.adj[u]:
            new_cost = dist[u] + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return dist
