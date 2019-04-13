#
# #206 Reverse Linked List

from leetcode import ListNode, linked_list_to_list, list_to_linked_list


class Solution(object):
    def reverseList_mine(self, head):
        queue = []
        n = head
        while n:
            queue.append(n)
            n = n.next
        i = 0
        j = len(queue) - 1
        h = queue[0]
        while i < j:
            queue[i].next = queue[j].next
            queue[j].next = queue[i].next
            if i == 0:
                h = queue[j]
            else:
                queue[i - 1].next = queue[j]
            queue[j - 1].next = queue[i]
            tmp = queue[i]
            queue[i] = queue[j]
            queue[j] = tmp
            i += 1
            j -= 1
        if i == j and i != 0:
            queue[i - 1].next = queue[i]
        elif i > j:
            queue[j].next = queue[i]
            if i + 1 < len(queue):
                queue[i].next = queue[i + 1]
            else:
                queue[i].next = None
        return h

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_00(self):
        self.assertEqual(
            linked_list_to_list(self.s.reverseList(list_to_linked_list([1]))), [1]
        )

    def test_01(self):
        self.assertEqual(
            linked_list_to_list(
                self.s.reverseList(list_to_linked_list([1, 2, 3, 4, 5]))
            ),
            [5, 4, 3, 2, 1],
        )

    def test_02(self):
        self.assertEqual(
            linked_list_to_list(
                self.s.reverseList(list_to_linked_list([1, 3, 2, 4, 6, 7]))
            ),
            [7, 6, 4, 2, 3, 1],
        )

    def test_03(self):
        self.assertEqual(
            linked_list_to_list(self.s.reverseList(list_to_linked_list([1, 2]))), [2, 1]
        )


unittest.main()
