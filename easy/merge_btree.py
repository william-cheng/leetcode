#
# #617 Merge Two Binary Trees


class Solution(object):
    def mergeTrees(self, t1, t2):
        end = False
        curr_t1 = [t1]
        curr_t2 = [t2]
        if not t1:
            return t2
        while not end:
            next_t1 = []
            next_t2 = []
            i = 0
            none_b = 0
            while i < len(curr_t1):
                a = curr_t1[i]
                b = curr_t2[i]
                if a and b:
                    a.val = a.val + b.val
                    if not a.left and b.left:
                        a.left = b.left
                        b.left = None
                    next_t1.append(a.left)
                    next_t2.append(b.left)
                    if not a.right and b.right:
                        a.right = b.right
                        b.right = None
                    next_t1.append(a.right)
                    next_t2.append(b.right)
                if not b:
                    none_b += 1
                i += 1
            if none_b == len(curr_t2):
                end = True
            curr_t1 = next_t1
            curr_t2 = next_t2
        return t1


import leetcode
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_00(self):
        t1 = leetcode.list_to_btree([1, 2, None, 3])
        t2 = leetcode.list_to_btree([1, None, 2, None, 3])
        self.assertEqual(
            leetcode.btree_to_list(self.s.mergeTrees(t1, t2)),
            [2, 2, 2, 3, None, None, 3],
        )

    def test_01(self):
        t1 = leetcode.list_to_btree([1, 2, None, 3])
        t2 = leetcode.list_to_btree([1, None, 2, None, 3])
        self.assertEqual(
            leetcode.btree_to_list(self.s.mergeTrees(t1, t2)),
            [2, 2, 2, 3, None, None, 3],
        )

    def test_02(self):
        t1 = leetcode.list_to_btree([])
        t2 = leetcode.list_to_btree([1])
        self.assertEqual(
            leetcode.btree_to_list(self.s.mergeTrees(t1, t2)), [1]
        )


unittest.main()
