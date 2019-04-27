# 1021. Remove Outmost Parentheses

class Solution(object):
    def removeOuterParentheses(self, S):
        output = ""
        sect = ""
        stack = []
        for c in S:
            sect += c
            if c == ")" and stack[-1] == "(":
                stack = stack[:-1]
            else:
                stack.append(c)
            if not stack:
                if len(sect) > 2:
                    output += sect[1:-1]
                else:
                    output += sect
                sect = ""
        return output


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.removeOuterParentheses("(()())(())"), "()()()")

    def test_02(self):
        self.assertEqual(self.s.removeOuterParentheses("()"), "()")

    def test_03(self):
        self.assertEqual(self.s.removeOuterParentheses("()()()"), "()()()")

    def test_04(self):
        self.assertEqual(self.s.removeOuterParentheses("(())()"), "()()")

    def test_05(self):
        self.assertEqual(self.s.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")

unittest.main()