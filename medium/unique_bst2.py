

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    computed = {}
    def generate_tree(self, ints):
        if not ints:
            return [None]
        if len(ints) == 1:
            return [TreeNode(ints[0])]
        if str(ints) in self.computed:
            return self.computed[str(ints)]
        r = []
        for i in range(0, len(ints)):
            x = ints[i]
            left = self.generate_tree(ints[:i])
            right = self.generate_tree(ints[i+1:])
            for L in left:
                for R in right:
                    n = TreeNode(x)
                    n.left = L
                    n.right = R
                    r.append(n)
        self.computed[str(ints)] = r
        return r

    def generateTree(self, n):
        if not n:
            return []
        return self.generate_tree([i for i in range(1, n+1)])


def flat_tree(root):
    r = []
    q = [root]
    while q:
        n = q[0]
        q = q[1:]
        r.append(n.val if n else 'null')
        if n:
            q.append(n.left)
            q.append(n.right)
    while r[-1] == 'null':
        r = r[:-1]
    return r


if __name__ == "__main__":
    inputs = (0, 3, 5, 8, 10)
    s = Solution()
    for i in inputs:
        print("- {0}: {1}".format(i, len(s.generateTree(i))))

