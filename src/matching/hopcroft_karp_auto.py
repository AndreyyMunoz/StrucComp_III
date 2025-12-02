from src.bipartite.color_two import two_color
from matching.hopcroft_karp_manual import hopcroft_karp


def hopcroft_karp_auto(graph):
    """
    Versión automática de Hopcroft-Karp.
    1) Colorea el grafo con two_color()
    2) Obtiene U y V automáticamente
    3) Llama a hopcroft_karp() manual

    Retorna:
    - (matching, U, V)
    o
    - None si el grafo NO es bipartito
    """

    colors = two_color(graph)
    if colors is None:
        return None  # No bipartito → no existe matching bipartito

    # Particiones según color
    U = {i for i, c in enumerate(colors) if c == 0}
    V = {i for i, c in enumerate(colors) if c == 1}

    matching = hopcroft_karp(graph, U, V)
    return matching, U, V
