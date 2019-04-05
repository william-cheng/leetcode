#
# #433 Minimum Genetic Mutation

from collections import defaultdict

class Solution(object):

    def minMutation(self, start, end, bank):
        if not bank or end not in bank:
            return -1
        bank = dict([(g, None) for g in bank])
        queue = [start]
        while queue:
            n = queue[0]
            queue = queue[1:]
            for i in range(0, len(n)):
                if n[i] != end[i]:
                    tmp = [c for c in n]
                    tmp[i] = end[i]
                    tmp = "".join(tmp)
                    if tmp in bank:
                        queue.append
        return count

import unittest
class Tests(unittest.TestCase):

    s = None
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        r = self.s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
        self.assertEqual(r, 1)

    def test_2(self):
        r = self.s.minMutation(
            "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
        self.assertEqual(r, 2)

    def test_3(self):
        r = self.s.minMutation(
            "AACCGGTA", "GACCGGTT", ["AACCGGTA", "AACCGCTA"])
        self.assertEqual(r, -1)

    def test_4(self):
        r = self.s.minMutation(
            "GAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
        self.assertEqual(r, -1)

    def test_5(self):
        r = self.s.minMutation(
            "AAAAGCCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
        self.assertEqual(r, 3)

unittest.main()
