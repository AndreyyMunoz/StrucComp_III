# core/validators.py

def validate_node_user(graph, u):
    """
    Valida nodos ingresados por el usuario.
    Ahora el usuario trabaja con nodos 1..n (más intuitivo).
    Internamente convertiremos a 0..n-1.
    """
    if not isinstance(u, int):
        raise ValueError(f"El nodo '{u}' debe ser un entero.")

    if u < 1 or u > graph.n:
        raise ValueError(
            f"Nodo fuera de rango: {u}. "
            f"Rango válido para el usuario: 1..{graph.n}"
        )


def validate_node_internal(graph, u):
    """
    Valida nodos dentro del grafo real (0..n-1).
    Se usa internamente.
    """
    if u < 0 or u >= graph.n:
        raise ValueError(
            f"Nodo interno fuera de rango: {u}. "
            f"(0..{graph.n - 1})"
        )


# ============================================================
#   PARSE (u v [peso])
#   Usuario usa nodos 1..n → convertimos a 0..n-1
# ============================================================
def parse_edge_line(line, graph):
    parts = line.split()

    if len(parts) not in (2, 3):
        raise ValueError("Formato inválido. Use: u v [peso]")

    try:
        u_user = int(parts[0])   # nodos 1..n
        v_user = int(parts[1])
    except ValueError:
        raise ValueError("Los nodos deben ser enteros.")

    validate_node_user(graph, u_user)
    validate_node_user(graph, v_user)

    # Mapear a 0..n-1
    u = u_user - 1
    v = v_user - 1

    # Peso
    w = 1.0
    if len(parts) == 3:
        try:
            w = float(parts[2])
        except ValueError:
            raise ValueError("El peso debe ser un número.")

    return u, v, w


# ============================================================
#   PARSE DE CONJUNTOS U Y V (para matching)
# ============================================================
def parse_set_input(text, graph):
    """
    Entrada segura para conjuntos definidos por el usuario en formato 1..n.
    Convertimos todo a 0..n-1 internamente.
    """
    raw = text.strip()
    if not raw:
        raise ValueError("Entrada vacía.")

    # Separar por espacios o comas
    tokens = raw.replace(",", " ").split()

    try:
        user_items = [int(x) for x in tokens]
    except:
        raise ValueError("Solo números enteros separados por espacio.")

    # Validar 1..n
    for x in user_items:
        validate_node_user(graph, x)

    # Convertir a 0..n-1
    internal_nodes = [x - 1 for x in user_items]

    return set(internal_nodes)
