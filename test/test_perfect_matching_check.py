import unittest

from src.graph import Graph
from src.matching.hopcroft_karp_auto import hopcroft_karp_auto
from perfect_match_check.perfect_matching_check import is_perfect_matching


def convert_matching(matching_dict):
    seen = set()
    result = set()
    for u, v in matching_dict.items():
        if (v, u) not in seen:
            result.add(tuple(sorted((u, v))))
            seen.add((u, v))
    return result


class TestPerfectMatchingCheck(unittest.TestCase):

    def test_perfect_matching_from_hopcroft_karp_auto(self):
        # === 1) Grafo del usuario ===
        g = Graph(4, directed=False)

        edges = [
            (0, 2),
            (1, 3)
        ]

        for u, v in edges:
            g.add_edge(u, v)

        # === 2) Matching Hopcroft–Karp ===
        result = hopcroft_karp_auto(g)

        self.assertIsNotNone(result, "Debe ser bipartito")

        matching_dict, U, V = result

        # === 3) Convertir formato ===
        matching_set = convert_matching(matching_dict)

        # === 4) Comprobar perfección ===
        self.assertTrue(
            is_perfect_matching(g.adj, matching_set),
            "Debe detectar matching perfecto"
        )


if __name__ == "__main__":
    unittest.main()
