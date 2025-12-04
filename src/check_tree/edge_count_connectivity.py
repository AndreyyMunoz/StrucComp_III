from collections import deque

def is_connected_edge_count(graph):
    """
    Verifica si un grafo es conexo.
    - Si es NO dirigido → revisa conectividad por BFS y condición de aristas.
    - Si es dirigido → revisa si es fuertemente conexo (todos llegan a todos).

    Parámetros:
    - graph: objeto Graph

    Retorna:
    - True si el grafo es conexo (o fuertemente conexo si es dirigido)
    - False en caso contrario
    """

    if graph.directed:

        def bfs(start, adj_list):
            visited = [False] * graph.n
            q = deque([start])
            visited[start] = True
            while q:
                u = q.popleft()
                for v, _ in adj_list[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            return visited

        first_run = bfs(0, graph.adj)
        if not all(first_run):
            return False

        reversed_adj = [[] for _ in range(graph.n)]
        for u in range(graph.n):
            for v, w in graph.adj[u]:
                reversed_adj[v].append((u, w))

        second_run = bfs(0, reversed_adj)
        return all(second_run)

    else:
        visited = [False] * graph.n
        q = deque([0])
        visited[0] = True

        while q:
            u = q.popleft()
            for v, _ in graph.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        if not all(visited):
            return False

        total_edges = sum(len(a) for a in graph.adj) // 2
        return total_edges >= graph.n - 1
