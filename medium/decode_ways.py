class Solution(object):
    def numDecoding(self, s):
        computed = {s[0]: set([(int(s[0]), )])}
        i = 1
        while i < len(s):
            to_check_key = s[:i+1]
            a = int(s[i])
            prev_key = s[:i]
            prev = computed[prev_key]
            curr = set()
            for p in prev:
                if a > 0:
                    curr.add(p + (a, ))
                pc = p[-1]
                pc_h, pc_r = pc / 10, pc % 10
                b = pc_r * 10 + a
                if pc_h > 0 and pc_r != 0 and 0 < b <= 26:
                    key = (p[:-1]) + (pc_h, b,)
                    if key not in curr:
                        curr.add((p[:-1] + (pc_h, b,)))
                elif pc_h == 0 and 0 < b <= 26:
                    key = (p[:-1]) + (b,)
                    if key not in curr:
                        curr.add((p[:-1] + (b,)))
            computed[to_check_key] = curr
            i += 1
        return len(computed[s])


import unittest
class Tests(unittest.TestCase):

    s = None
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.numDecoding("12"), 2)

    def test_02(self):
        self.assertEqual(self.s.numDecoding("226"), 3)

    def test_1703(self):
        self.assertEqual(self.s.numDecoding("1703"), 0)

    def test_7206(self):
        self.assertEqual(self.s.numDecoding("7206"), 1)

    def test_large(self):
        r = self.s.numDecoding("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
        self.assertTrue(r, 589824)


#unittest.main()

import cProfile
cProfile.run('Solution().numDecoding("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")')
