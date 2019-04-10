#


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        lists = filter(lambda x: x, lists)
        head = n = None
        lists.sort(key=lambda x: x.val)
        while lists:
            if len(lists) > 1 and lists[0].val > lists[1].val:
                lists.sort(key=lambda x: x.val)
            if head is None:
                head = n = lists[0]
            else:
                n.next = lists[0]
                n = n.next
            lists[0] = lists[0].next
            if lists[0] is None:
                lists = lists[1:]
        return head


import unittest


def as_list(n):
    _list = []
    while n:
        _list.append(n.val)
        n = n.next
    return _list


def build_list(lists):
    built = []
    for _list in lists:
        n = head = ListNode(_list[0])
        for i in _list[1:]:
            n.next = ListNode(i)
            n = n.next
        built.append(head)
    return built


import merge_k_sorted_list_testdata

long_list = build_list(merge_k_sorted_list_testdata.long_list)


class Tests(unittest.TestCase):
    s = None

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        self.assertEqual(as_list(self.s.mergeKLists(build_list(lists))), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_long(self):
        _ = self.s.mergeKLists(long_list)

    def test_negative(self):
        head = self.s.mergeKLists(
            build_list(
                [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
            )
        )
        self.assertEqual(
            as_list(head), [-10, -10, -8, -7, -7, -7, -5, -2, 0, 1, 1, 1, 2, 3, 3, 4]
        )

    def test_empty(self):
        head = self.s.mergeKLists([[]])
        self.assertEqual(head, None)


unittest.main()
