class Graph:
    """
    Clase base para representar un grafo dirigido o no dirigido
    usando lista de adyacencia.

    Cada entrada en adj[u] es una tupla (v, w), donde:
        v = nodo destino
        w = peso de la arista (por defecto = 1)
    """

    def __init__(self, n, directed=False):
        """
        Inicializa un grafo con n nodos.

        Parámetros:
        - n (int): número de nodos
        - directed (bool): True = grafo dirigido, False = no dirigido
        """
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, w=1):
        """
        Agrega una arista al grafo.

        Parámetros:
        - u (int): nodo origen
        - v (int): nodo destino
        - w (num): peso de la arista (default = 1)
        """
        self.adj[u].append((v, w))

        # Si no es dirigido, agregar la arista inversa
        if not self.directed:
            self.adj[v].append((u, w))

    def neighbors(self, u):
        """Regresa la lista de vecinos del nodo u."""
        return self.adj[u]

    def __str__(self):
        """Representación bonita del grafo (útil para depuración)."""
        lines = []
        for u in range(self.n):
            edges = ", ".join([f"{u}->{v} (w={w})" for v, w in self.adj[u]])
            lines.append(edges)
        return "\n".join(lines)
