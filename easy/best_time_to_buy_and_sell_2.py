# 122 Best Time to Buy and Sell Stock II


class Solution(object):
    def maxProfit(self, prices):
        min_v = prices[0]
        max_p = 0
        total = 0
        for v in prices[1:]:
            if v - min_v < max_p:
                total += max_p
                max_p = 0
                min_v = v
            elif min_v > v:
                min_v = v
            elif v - min_v > max_p:
                max_p = v - min_v
        return total + max_p


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.maxProfit([2, 1, 2, 0, 1]), 2)

    def test_02(self):
        self.assertEqual(self.s.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_03(self):
        self.assertEqual(self.s.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_04(self):
        self.assertEqual(self.s.maxProfit([7, 6, 4, 3, 1]), 0)


unittest.main()
