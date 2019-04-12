class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def serialise(head):
    r = []
    n = head
    while n:
        r.append(n.val)
        n = n.next
    return r


def make_list(s):
    if not s:
        return None
    n = ListNode(s[0])
    head = n
    for i in s[1:]:
        n.next = ListNode(i)
        n = n.next
    return head


class Solution(object):
    def swapPairs(self, head):
        prev = None
        _next = head
        while _next:
            left = _next
            right = left.next
            if right is None:
                break
            _next = right.next
            left.next = _next
            right.next = left
            if prev is None:
                head = right
                prev = head.next
            else:
                prev.next = right
                prev = left
        return head


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(
            serialise(self.s.swapPairs(make_list([1,2,3,4]))),
            [2,1,4,3])

    def test_02(self):
        self.assertEqual(serialise(self.s.swapPairs(make_list([1]))), [1])

    def test_03(self):
        self.assertEqual(serialise(self.s.swapPairs(make_list([1,2,3]))), [2,1,3])

    def test_04(self):
        self.assertEqual(serialise(self.s.swapPairs(make_list([2,5,3,4,6,2,2]))), [5,2,4,3,2,6,2])


unittest.main()
