#
#

from datastructs import BSTreeNode


class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        s = [root]
        successor = None
        while s:
            n = s[0]
            s = s[1:]
            if n.val > p.val:
                if successor is None:
                    successor = n
                elif successor.val > n.val:
                    successor = n
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        return successor


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        root = BSTreeNode(2)
        root.left = BSTreeNode(1)
        root.right = BSTreeNode(3)
        self.assertEqual(self.s.inorderSuccessor(root, BSTreeNode(1)).val, 2)

    def test_02(self):
        root = BSTreeNode(5)
        root.left = BSTreeNode(3)
        root.right = BSTreeNode(6)
        root.left.left = BSTreeNode(2)
        root.right.right = BSTreeNode(4)
        root.left.left.left = BSTreeNode(1)
        self.assertEqual(self.s.inorderSuccessor(root, BSTreeNode(6)), None)


unittest.main()