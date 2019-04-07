

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []


class BSTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None