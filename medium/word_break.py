#
#

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        q = set([s])
        while q:
            p = q.pop()
            for w in wordDict:
                if w == p:
                    return True
                if p.startswith(w):
                    remain = p[len(w):]
                    if remain not in q:
                        q.add(remain)
        return False


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertTrue(self.s.wordBreak("leetcode", ["leet", "code"]))

    def test_2(self):
        self.assertTrue(self.s.wordBreak("applepenapple", ["apple", "pen"]))

    def test_3(self):
        self.assertFalse(self.s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))


unittest.main()