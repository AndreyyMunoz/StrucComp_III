# src/core/display.py

def to_user(u):
    """Convierte un nodo interno (0..n-1) a nodo de usuario (1..n)."""
    return u + 1


def edge_to_user(edge):
    """
    edge: (u, v, w)
    Retorna: (u+1, v+1, w)
    """
    u, v, w = edge
    return (u + 1, v + 1, w)


def edges_to_user(edges):
    """
    Convierte una lista de aristas [(u,v,w), ...] a números 1..n.
    """
    return [edge_to_user(e) for e in edges]


def list_to_user(lst):
    """
    Convierte una lista de nodos [0,2,4] -> [1,3,5]
    """
    return [x + 1 for x in lst]


def sets_to_user(s):
    """
    Convierte un set {0,2,4} -> {1,3,5}
    """
    return {x + 1 for x in s}


def matching_to_user(matching):
    """
    matching: set {(u,v)}
    Retorna nodos como 1..n
    """
    return {(u + 1, v + 1) for (u, v) in matching}
