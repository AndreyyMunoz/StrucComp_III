class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.rank[ra] < self.rank[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
            return True
        return False


def kruskal(graph):
    """
    Algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima (MST).
    Funciona solo para grafos NO dirigidos y ponderados.
    
    Retorna:
    - Lista de aristas del MST en formato (u, v, w)
    """

    edges = []

    # Recolectar todas las aristas
    for u in range(graph.n):
        for v, w in graph.adj[u]:
            if graph.directed:
                continue
            if u < v:  # evitar duplicados
                edges.append((w, u, v))

    # Ordenar por peso
    edges.sort()

    dsu = DSU(graph.n)
    mst = []

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))

    return mst
