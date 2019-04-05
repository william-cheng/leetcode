
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

r_01 = TreeNode(5)
r_01.left = TreeNode(4)
r_01.right = TreeNode(5)
r_01.left.left = TreeNode(1)
r_01.left.right = TreeNode(1)
r_01.right.left = TreeNode(5)
r_01.right.right = TreeNode(5)
r_01.right.right.right = TreeNode(5)
r_01_expected = 3

r_02 = TreeNode(1)
r_02.left = TreeNode(4)
r_02.right = TreeNode(5)
r_02.left.left = TreeNode(4)
r_02.left.right = TreeNode(4)
r_02.right.right = TreeNode(5)
r_02_expected = 2


class Solution(object):
    def longestUnivaluePath(self, root):
        return -1

