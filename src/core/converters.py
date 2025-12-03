# core/converters.py

def dict_to_matching_set(matching):
    """
    Convierte:
        {0: 1, 1: 0, 2: 3, 3: 2}
    A:
        {(0,1), (2,3)}
    """
    seen = set()
    edges = set()

    for u, v in matching.items():
        if (u, v) not in seen and (v, u) not in seen:
            edges.add(tuple(sorted((u, v))))
            seen.add((u, v))
            seen.add((v, u))

    return edges
