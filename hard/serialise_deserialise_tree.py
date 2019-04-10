#
#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):
    def serialize(self, root):
        if not root:
            return ""
        data = []
        queue = [root]
        while queue:
            n = queue[0]
            queue = queue[1:]
            if n:
                data.append(str(n.val))
                queue.append(n.left)
                queue.append(n.right)
            else:
                data.append("n")
        n = data[-1]
        while n == 'n':
            data = data[:-1]
            n = data[-1]
        return ",".join(data)

    def deserialize(self, data):
        if not data:
            return None
        queue = []
        data = data.split(',')
        root = TreeNode(int(data.pop(0)))
        queue.append(root)
        while queue:
            if not data:
                break
            n = queue.pop(0)
            if data[0] != 'n':
                n.left = TreeNode(int(data.pop(0)))
                queue.append(n.left)
            
            if data and data[0] != 'n':
                n.right = TreeNode(int(data.pop(0)))
                queue.append(n.right)

        return root


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Codec()

    def test_00(self):
        self.assertEqual(self.s.serialize(None), "")
        self.assertEqual(self.s.deserialize(""), None)

    def test_01(self):
        root = self.s.deserialize("1,2,3,n,n,4,5")
        self.assertEqual(root.val, 1)
        self.assertEqual(self.s.serialize(root), "1,2,3,n,n,4,5")

    def test_03(self):
        root = self.s.deserialize("1,2")
        self.assertEqual(root.val, 1)
        self.assertEqual(self.s.serialize(root), "1,2")

    def test_04(self):
        root = self.s.deserialize("1")
        self.assertEqual(root.val, 1)
        self.assertEqual(self.s.serialize(root), "1")


unittest.main()

