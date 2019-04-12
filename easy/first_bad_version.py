def isBadVersion(n):
    pass



class Solution(object):
    def firstBadVersion(self, n):
        s = 1
        e = n
        while s < e - 1:
            m = (s + e) / 2
            if isBadVersion(m):
                e = m
            else:
                s = m
        if isBadVersion(s):
            return s
        else:
            return e
        

version_03 = {1:0}
version_04 = {1:1}


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        global isBadVersion
        def func(n):
            versions = {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 1,
                6: 1,
                7: 1,
            }
            return versions[n]

        isBadVersion = func
        self.assertEqual(self.s.firstBadVersion(7), 5)

    def test_02(self):
        global isBadVersion
        def func(n):
            versions = {1:1, 2:1}
            return versions[n]

        isBadVersion = func
        self.assertEqual(self.s.firstBadVersion(2), 1)

unittest.main()

