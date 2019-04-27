#
#


def dfs(graph, s, t=None):
    """

    :param graph:
    :param t:
    :return:
    """
    stack = [s]
    visited = set()
    traversal = []
    while stack:
        n = stack[-1]
        stack = stack[:-1]
        if n not in visited:
            traversal.append(
                n
            )  # you can olways return visited instead but there traversal keeps the order
            visited.add(n)
        if n == t:
            return traversal
        for c in graph[n]:
            if c not in visited:
                stack.append(c)
    return traversal


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
        self.assertEqual(dfs(self.graph, "A"), ["A", "C", "F", "E", "B", "D"])

    def test_02(self):
        self.assertEqual(dfs(self.graph, "A", "E"), ["A", "C", "F", "E"])


unittest.main()
