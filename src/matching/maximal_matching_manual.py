def maximal_matching_manual(graph, U, V):
    """
    MAXIMAL MATCHING bipartito (manual).
    El usuario debe pasar las particiones U y V.

    Retorna:
    - Lista de aristas (u, v) con u ∈ U y v ∈ V
    """

    matched = set()
    matching = []

    for u in U:
        if u in matched:
            continue

        for v, _ in graph.adj[u]:
            if v in V and v not in matched:
                matched.add(u)
                matched.add(v)
                matching.append((u, v))
                break

    return matching
