def maximal_matching_auto(graph):
    """
    MAXIMAL MATCHING general (Greedy).
    Funciona en cualquier grafo NO dirigido.

    Retorna:
    - Lista de aristas (u, v)
    """

    matched = [False] * graph.n
    matching = []

    for u in range(graph.n):
        if matched[u]:
            continue

        for v, _ in graph.adj[u]:
            if not matched[v]:
                matched[u] = matched[v] = True
                matching.append((u, v))
                break

    return matching
