
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isValidBST(self, root):
        if not root:
            return True

        def helper(n, lower, upper):
            if lower is not None and n.val <= lower:
                return False
            if upper is not None and n.val >= upper:
                return False
            
            if n.left and n.right:
                return helper(n.left, lower, n.val) and helper(n.right, n.val, upper)
            elif n.left and not n.right:
                return helper(n.left, lower, n.val)
            elif not n.left and n.right:
                return helper(n.right, n.val, upper)
            else:
                return True

        return helper(root, None, None)


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.s.isValidBST(root))

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(self.s.isValidBST(root))

    def test_3(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.s.isValidBST(root))

    def test_4(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)
        self.assertTrue(self.s.isValidBST(root))

    def test_5(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        right = root.right
        left = root.left
        left.left = TreeNode(0)
        left.right = TreeNode(2)
        left.right.right = TreeNode(3)
        right.left = TreeNode(4)
        right.right = TreeNode(6)
        self.assertFalse(self.s.isValidBST(root))

unittest.main()
