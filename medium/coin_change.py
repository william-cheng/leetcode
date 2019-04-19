# 322. Coin Change


class Solution(object):
    def coinChangeMine(self, coins, amount):
        if not amount:
            return 0
        coins.sort(reverse=True)
        min_coins = amount / min(coins) + 1
        computed = {amount: 0}
        while computed:
            r = sorted(computed.keys(), reverse=True)[0]
            count = computed[r]
            del computed[r]
            for c in coins:
                rc = r - c
                if rc == 0:
                    min_coins = min(min_coins, count + 1)
                elif rc > 0:
                    if (
                        rc in computed
                        and count + 1 < computed[rc]
                        or rc not in computed
                    ):
                        computed[rc] = count + 1
        if min_coins == amount / min(coins) + 1:
            return -1
        return min_coins

    def coinChange(self, coins, amount):
        if not coins:
            return -1

        # init a list, the length of the list is `amount + 1`, init all of its elements value to -1
        # count_cache[i] represents make amount of i money should use number of count_cache[i] coins at least
        #count_cache = [-1 for _ in range(amount + 1)]

        # [KEY POINT] make amount of 0 money should use zero coin at least
        #count_cache[0] = 0
        count_cache = [0] + [-1] * amount
        # store the min_coin value, prepare it for the using in future
        min_coin = min(coins)
        # here starts calculate that make every amount i of money(i from 1 to amount + 1) should use how many coins at least?
        for i in range(1, amount + 1):
            # [KEY POINT] if i is less than the minimum of coins, there is no exchange solution, return -1, and store the value in count_cache list
            if i < min_coin:
                count_cache[i] = -1
                continue

            # init min_count to the impossible count
            min_count = amount + 1
            # [KEY POINT] traverse the coins list, in which every element is less than i
            for c in [coin for coin in coins if coin <= i]:
                # if there is no solution to make amount of i-c money, continue
                if count_cache[i - c] == -1:
                    continue
                # [KEY POINT] here is the key point, consider that first use ONE c money, and then make i-c money, plus the two values as cur_count
                cur_count = 1 + count_cache[i - c]
                # compare cur_count to min_count, if cur_count is smaller, update min_count to cur_count
                if cur_count < min_count:
                    min_count = cur_count
            # [KEY POINT] at last, if min_count is still inf, update it to -1
            if min_count == amount + 1:
                min_count = -1
            # store the min_count
            count_cache[i] = min_count
        return count_cache[amount]


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.coinChange([1, 2, 5], 11), 3)

    def test_02(self):
        self.assertEqual(self.s.coinChange([2], 3), -1)

    def test_large(self):
        self.assertEqual(self.s.coinChange([1, 2, 5], 1234), 248)

    def test_large_02(self):
        self.assertEqual(
            self.s.coinChange([249, 459, 494, 426, 32, 372, 225], 4235), 10
        )

    def test_large_03(self):
        self.assertEqual(self.s.coinChange([470, 18, 66, 301, 403, 112, 360], 8235), 20)

    def test_large_04(self):
        self.assertEqual(self.s.coinChange([186, 419, 83, 408], 6249), 20)


unittest.main()
