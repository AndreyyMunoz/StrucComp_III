# StrucComp_III
In this repository, you'll find a complete collection of graph algorithms implemented in Python.
The goal of this project is to provide clean, organized, and documented implementations of fundamental graph topics.

Each topic includes two different algorithms, giving you multiple approaches to solve the same type of problem.
All algorithms are located in the **/src/** directory, and each implementation includes its own dedicated test file inside **/test/**.

This repository is useful for anyone studying:

- Graph theory
- Data structures
- Competitive programming
- Algorithmic problem solving

Or anyone who wants to understand how to store, manipulate, traverse, and analyze graphs in Python.

## 📁 Project Structure
```
StrucComp_III/
│
├── src/
│   ├── bipartite/
│   │   ├── bipartite_check.py
│   │   └── color_two.py
│   │
│   ├── components/
│   │   ├── connected_components.py
│   │   └── kosaraju_scc.py
│   │
│   ├── matching/
│   │   ├── hopcroft_karp.py
│   │   └── maximal_matching.py
│   │
│   ├── mst/
│   │   ├── kruskal.py
│   │   └── prim.py
│   │
│   ├── representations/
│   │   ├── adjacency_list.py
│   │   └── adjacency_matrix.py
│   │
│   ├── shortest_paths/
│   │   ├── dijkstra.py
│   │   └── floyd_warshall.py
│   │
│   ├── traversals/
│   │   ├── bfs.py
│   │   └── dfs.py
│   │
│   └── graph.py          ← Core graph class (if applicable)
│
├── test/
│   ├── test_bipartite_check.py
│   ├── test_color_two.py
│   ├── test_connected_components.py
│   ├── test_kosaraju_scc.py
│   ├── test_hopcroft_karp.py
│   ├── test_maximal_matching.py
│   ├── test_kruskal.py
│   ├── test_prim.py
│   ├── test_adjacency_list.py
│   ├── test_adjacency_matrix.py
│   ├── test_dijkstra.py
│   ├── test_floyd_warshall.py
│   ├── test_bfs.py
│   └── test_dfs.py
│
└── README.md
```
## 🔍 Topics Covered (9 total)

Each topic includes two implementations, summing up to 18 algorithms:

### ✔ Graph Representations
- Adjacency matrix
- Adjacency list

### ✔ Graph Traversals
- Breadth-first search (BFS)
- Depth-first search (DFS)

### ✔ Graph Components
- Connected components (BFS/DFS)
- Kosaraju’s algorithm for strongly connected components (SCCs)

### ✔ Shortest Paths
- Dijkstra’s algorithm
- Floyd–Warshall algorithm

### ✔ Check Tree by Properties
- DFS Cycle Detection + Connectivity Check
- Edge Count + Connectivity

### ✔ Minimum Spanning Tree (MST)
- Kruskal's algorithm
- Prim's algorithm

### ✔ Bipartite Graphs
- Check if a graph is bipartite
- 2-coloring algorithm

### ✔ Graph Matching
- Hopcroft–Karp algorithm
- Maximal matching

### ✔ Perfect and Maximal Matchings
- Greedy Maximal Matching
- Perfect Matching Check






## 🛠 Requirements

- Python 3.10+

> No external dependencies unless required by specific algorithms (e.g., heapq is built-in)

## 📚 Purpose

This repository was created as a final project for the subject **Estructuras Computacionales III**, focusing on:

- Applying theoretical graph concepts
- Implementing efficient algorithms
- Building a clean, maintainable software structure using professional engineering practices (tests, folders, modularity)


## 👤 Authors

:octocat: [Luis Gerardo Escamilla López]()

:octocat: [Pedro Fernando López Vazquéz](https://github.com/ferbigDK)

:octocat: [Santiago Andrey Muñoz Muñoz](https://github.com/AndreyyMunoz).

#### Engineering Students / Software Developers