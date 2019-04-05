import unittest

def num_squares(n):
    squares = []
    i = p = 1
    while p <= n:
        squares.append(p)
        i += 1
        p = pow(i, 2)
    squares.reverse()
    from collections import OrderedDict
    lasts = OrderedDict({n:0})
    while lasts:
        last, c = lasts.popitem(last=False)
        #last = lasts.keys()[0]
        #c = lasts.pop(last)
        for i in squares:
            if last == i:
                return c+1
            elif last > i and last-i not in lasts:
                lasts[last - i] = c+1
    return least


def num_squares_their(n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp
    return cnt

class tests(unittest.TestCase):
    def test_12(self):
        self.assertEqual(num_squares(12), 3)
    def test_13(self):
        self.assertEqual(num_squares(13), 2)
    def test_6255(self):
        self.assertEqual(num_squares(6255), 4)
    def test_427(self):
        self.assertEqual(num_squares(427), 3)
    def test_162(self):
        self.assertEqual(num_squares(162), 2)
    def test_7691(self):
        self.assertEqual(num_squares(7691), 3)
    def test_8935(self):
        self.assertEqual(num_squares(8935), 4)

unittest.main()

