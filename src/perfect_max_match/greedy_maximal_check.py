def is_maximal_matching(graph, matching):
    """
    Verifica si un matching dado es maximal.
    
    graph: dict -> {u: [(v, w), ...], ...}
    matching: set of tuples -> {(u, v), ...}  (las tuplas se normalizan)

    Retorna:
        True  si es maximal
        False si aún se puede agregar otra arista sin conflicto
    """

    # Normalizamos matching (ordenamos cada arista)
    normalized = {tuple(sorted(edge[:2])) for edge in matching}

    # Nodos ya ocupados
    used_nodes = set()
    for u, v in normalized:
        used_nodes.add(u)
        used_nodes.add(v)

    # Revisamos todas las aristas del grafo
    for u in graph:
        for v, _ in graph[u]:
            if u < v:  # evitar duplicados en grafos no dirigidos
                # si la arista no está en matching
                edge = (u, v)
                if edge not in normalized:
                    # y ambos nodos están libres
                    if u not in used_nodes and v not in used_nodes:
                        # matching NO es maximal
                        return False

    return True
