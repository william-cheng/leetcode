
class Solution(object):
    def recursiveNumTrees(self, )
    def numTrees(self, n):
        self.computed = {}


import unittest
class Tests(unittest.TestCase):

    s = None
    def setUp(self):
        self.s = Solution()

    def test_0(self):
        self.assertEqual(self.s.numTrees(0), 0)

    def test_3(self):
        self.assertEqual(self.s.numTrees(3), 5)

    def test_5(self):
        self.assertEqual(self.s.numTrees(5), 42)

    def test_8(self):
        self.assertEqual(self.s.numTrees(8), 1430)

    def test_10(self):
        self.assertEqual(self.s.numTrees(10), 16796)

unittest.main()
