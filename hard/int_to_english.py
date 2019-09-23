# 273 Integer to English Words
#


class Solution(object):
    def numberToWords(self, num):

        return ""


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.numberToWords(123), "One Hundred Twenty Three")

    def test_02(self):
        self.assertEqual(self.s.numberToWords(1234567891), "One Billion Two Houndred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Niety One")


unittest.main()