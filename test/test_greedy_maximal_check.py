import unittest

from perfect_match_check.greedy_maximal_check import is_maximal_matching

from src.graph import Graph
from src.matching.hopcroft_karp_auto import hopcroft_karp_auto


def convert_matching(matching_dict):
    """
    Convierte matching {u: v, v: u} → {(u, v)}
    (evita duplicados)
    """
    seen = set()
    result = set()

    for u, v in matching_dict.items():
        if (v, u) not in seen:
            result.add(tuple(sorted((u, v))))
            seen.add((u, v))

    return result


class TestGreedyMaximalMatching(unittest.TestCase):

    def test_greedy_maximal_from_hopcroft_karp_auto(self):
        # === 1) Usuario crea un grafo ===
        g = Graph(6, directed=False)

        edges = [
            (0, 3),
            (0, 4),
            (1, 3),
            (2, 5),
        ]

        for u, v in edges:
            g.add_edge(u, v)

        # === 2) Ejecutamos Hopcroft–Karp AUTO ===
        result = hopcroft_karp_auto(g)

        self.assertIsNotNone(result, "El grafo debe ser bipartito")

        matching_dict, U, V = result

        # === 3) Convertimos formato ===
        matching_set = convert_matching(matching_dict)

        # === 4) Validación con greedy ===
        self.assertTrue(
            is_maximal_matching(g.adj, matching_set),
            "El matching producido debe ser maximal"
        )


unittest.main()
