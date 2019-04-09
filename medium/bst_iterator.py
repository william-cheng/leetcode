
#
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.stack = []
        n = root
        while n:
            self.stack.append(n)
            n = n.left

    def next(self):
        to_return = self.stack[-1]
        self.stack = self.stack[:-1]
        n = to_return.right
        while n:
            self.stack.append(n)
            n = n.left
        return to_return.val

    def hasNext(self):
        if self.stack:
            return True
        return False


import unittest


class Tests(unittest.TestCase):
    def test_01(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        iterator = BSTIterator(root)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 7)
        self.assertEqual(iterator.hasNext(), True)
        self.assertEqual(iterator.next(), 9)
        self.assertEqual(iterator.hasNext(), True)
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertEqual(iterator.hasNext(), False)

    def test_02(self):
        iterator = BSTIterator(None)
        self.assertEqual(iterator.hasNext(), False)


unittest.main()
