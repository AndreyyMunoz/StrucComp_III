from src.graph import Graph
from src.traversals.dfs import dfs

g = Graph(5, directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print(dfs(g, 0))  # [0, 1, 3, 2, 4]
