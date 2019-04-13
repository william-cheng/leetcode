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

        if i < len(data):
            right = BTreeNode(data[i]) if data[i] else None
            i += 1
        else:
            right = None
        if left:
            n.left = left
            q.append(left)
        if right:
            n.right = right
            q.append(right)
    return root


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_linked_list(data):
    if not data:
        return None
    head = ListNode(data[0])
    n = head
    for x in data[1:]:
        n.next = ListNode(x)
        n = n.next
    return head


def linked_list_to_list(head):
    n = head
    r = []
    while n:
        r.append(n.val)
        n = n.next
    return r
