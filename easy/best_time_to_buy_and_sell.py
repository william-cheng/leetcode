class Solution(object):
    def maxProfit_brute_force(self, prices):
        i = 0
        max_profit = 0
        prev_max = 0
        while i < len(prices) - 1:
            if prices[i] >= prev_max:
                prev_max = max(prices[i + 1 :])
            max_profit = max(prev_max - prices[i], max_profit)
            i += 1
        return max_profit

    def maxProfit(self, prices):
        _min = 1000000
        _max = 0
        for v in prices[1:]:
            if _min > v:
                _min = v
            elif _max < v - _min:
                _max = v - _min
        return _max


import unittest
from best_time_to_buy_and_sell_testdata import long_data


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_long(self):
        self.assertEqual(self.s.maxProfit(long_data), 3)


unittest.main()
