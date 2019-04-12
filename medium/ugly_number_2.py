

class Solution(object):
    def nthUglyNumber(self, n):
        computed = set()
        computed.add(1)
        length = len(computed)
        current = [1]
        while length < 4 * n:
            _next = []
            for c in current:
                for f in (2, 3, 5):
                    m = c * f
                    if m not in computed:
                        _next.append(m)
                        computed.add(m)
                        length += 1
            current = _next
        return sorted(list(computed))[n-1]


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.nthUglyNumber(10), 12)

    def test_02(self):
        self.assertEqual(self.s.nthUglyNumber(1690), 2123366400)

    def test_03(self):
        self.assertEqual(self.s.nthUglyNumber(169), 8748)

    def test_04(self):
        self.assertEqual(self.s.nthUglyNumber(1352), 402653184)


unittest.main()
