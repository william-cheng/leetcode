#

"""
Help module for LeetCode
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []


class BTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def btree_to_list(root):
    """Convert a binary tree to list"""
    q = [root]
    r = []
    while q:
        n = q.pop(0)
        if n:
            r.append(n.val)
            q.append(n.left)
            q.append(n.right)
        else:
            r.append(n)
    n = r[-1]
    while n is None:
        r = r[:-1]
        n = r[-1]
    return r


def list_to_btree(data):
    if not data:
        return None
    root = BTreeNode(data[0])
    q = [root]
    i = 1
    while q and i < len(data):
        n = q.pop(0)
        left = BTreeNode(data[i]) if data[i] else None
        i += 1
        right = BTreeNode(data[i]) if data[i] else None
        i += 1
        if left:
            n.left = left
            q.append(left)
        if right:
            n.right = right
            q.append(right)
    return root
