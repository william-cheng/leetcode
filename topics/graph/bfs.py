#
# BFS of Graph


def bfs(graph, s, t=None):
    queue = [s]
    visited = set()
    traversal = []
    while queue:
        n = queue[0]
        queue = queue[1:]
        if n in visited:
            continue
        visited.add(n)
        traversal.append(n)
        if n == t:
            return traversal
        queue += graph[n]
    return traversal


def bfs_path(graph, s, t):
    queue = [(s, [s])]
    visited = set()
    while queue:
        v, p = queue[0]
        queue = queue[1:]
        if t == v:
            return p
        for c in graph[v]:
            if c not in visited:
                queue.append((c, p + [c]))
    return None


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"],
        }

    def test_01(self):
        self.assertEqual(bfs(self.graph, "A"), ["A", "B", "C", "D", "E", "F"])

    def test_02(self):
        self.assertEqual(bfs(self.graph, "A", "F"), ["A", "B", "C", "D", "E", "F"])

    def test_03(self):
        self.assertEqual(bfs_path(self.graph, "A", "F"), ["A", "C", "F"])


unittest.main()
