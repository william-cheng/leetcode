# 904. Fruit into Basket
class Solution(object):
    def totalFruit(self, tree):
        if not tree:
            return 0
        i = 1
        prev_idx = 0
        picked = [tree[0]]
        count = max_picked = 1
        while i < len(tree):
            f = tree[i]
            if f not in picked and len(picked) == 1:
                picked.append(f)
                count += 1
            elif len(picked) == 2 and f not in picked:
                picked = [tree[prev_idx], f]
                max_picked = max(count, max_picked)
                count = i - prev_idx + 1
            elif f in picked:
                count += 1
            else:
                count += 1
                picked.append(f)
            if tree[prev_idx] != tree[i]:
                prev_idx = i
            i += 1

        return max(max_picked, count)


import unittest

all_zero = [0 for i in range(0, 40000)]
long_binary = [i % 2 for i in range(0, 40000)]


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_0(self):
        self.assertEqual(self.s.totalFruit(all_zero), 40000)

    def test_01(self):
        self.assertEqual(self.s.totalFruit(long_binary), 40000)

    def test_02(self):
        self.assertEqual(self.s.totalFruit([1, 2, 1]), 3)

    def test_03(self):
        self.assertEqual(self.s.totalFruit([0, 1, 2, 2]), 3)

    def test_04(self):
        self.assertEqual(self.s.totalFruit([1, 2, 3, 2, 2]), 4)

    def test_05(self):
        self.assertEqual(self.s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_06(self):
        self.assertEqual(self.s.totalFruit([1, 0, 3, 4, 3]), 3)


unittest.main()
