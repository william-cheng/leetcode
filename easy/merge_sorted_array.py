#
#


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = j = 0
        while j < n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop(-1)
                i += 1
                j += 1
                m += 1
            elif i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            else:
                i += 1


import unittest


class Tests(unittest.TestCase):
    s = None

    def setUp(self):
        self.s = Solution()

    def test_0(self):
        nums1 = []
        nums2 = []
        self.s.merge(nums1, 0, nums2, 0)
        self.assertEqual(nums1, [])

    def test_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.s.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])


unittest.main()
