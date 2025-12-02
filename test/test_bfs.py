from src.graph import Graph
from src.traversals.bfs import bfs

g = Graph(5, directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print(bfs(g, 0))  # [0, 1, 2, 3, 4]

