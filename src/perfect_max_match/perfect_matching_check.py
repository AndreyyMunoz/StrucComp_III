def is_perfect_matching(graph, matching):
    """
    Verifica si un matching es perfecto:
    - No tiene nodos repetidos
    - Cubre TODOS los nodos del grafo sin dejar ninguno libre

    graph: dict -> {u: [(v, w), ...], ...}
    matching: set of tuples -> {(u, v), ...}

    Retorna:
        True  si es perfecto
        False si NO lo es
    """

    n = len(graph)

    # Un matching perfecto debe tener n/2 aristas
    if n % 2 != 0:
        return False  # imposible cubrir un número impar de nodos

    # Normalizamos
    normalized = {tuple(sorted(edge[:2])) for edge in matching}

    # Nodos cubiertos
    covered = set()
    for u, v in normalized:
        # si un nodo aparece dos veces → no es matching válido
        if u in covered or v in covered:
            return False
        covered.add(u)
        covered.add(v)

    # matching perfecto = cubre TODOS los nodos
    return len(covered) == n
