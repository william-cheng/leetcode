class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1

import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        s = []
        self.s.reverseString(s)
        self.assertEqual(s, [])

    def test_02(self):
        s = ["a"]
        self.s.reverseString(s)
        self.assertEqual(s, ["a"])

    def test_03(self):
        s = [c for c in "abcdefg"]
        self.s.reverseString(s)
        self.assertEqual(s, [c for c in"gfedcba"])

    def test_04(self):
        s = [c for c in "123456"]
        self.s.reverseString(s)
        self.assertEqual(s, [c for c in "654321"])

unittest.main()