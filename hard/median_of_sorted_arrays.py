class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            merged = nums2
        elif not nums2:
            merged = nums1
        elif nums1[-1] <= nums2[0]:
            merged = nums1 + nums2
        else:
            len_nums2 = len(nums2)
            i = j = 0
            while j < len_nums2:
                if i >= len(nums1):
                    nums1.append(nums2[j])
                    j += 1
                elif nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    i += 1
                    j += 1
                else:
                    i += 1
            merged = nums1
        print("merged:", merged)
        len_merged = len(merged)
        if len_merged % 2 == 0:
            return (merged[len_merged / 2] + merged[len_merged / 2 - 1]) / 2.0
        else:
            return merged[len_merged / 2]


import unittest
from random import randint

nums1_large = sorted([randint(1, 10000) for i in range(0, 100000)])
nums2_large = sorted([randint(1, 10000) for i in range(0, 100000)])


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        r = self.s.findMedianSortedArrays([1, 3], [2])
        self.assertEqual(r, 2.0)

    def test_02(self):
        r = self.s.findMedianSortedArrays([1, 2, 3], [4, 5, 6])
        self.assertEqual(r, 3.5)

    def test_03(self):
        r = self.s.findMedianSortedArrays([], [2])
        self.assertEqual(r, 2.0)

    def test_04(self):
        r = self.s.findMedianSortedArrays([3], [-2, -1])
        self.assertEqual(r, -1.0)

    # def test_large(self):
    #    r = self.s.findMedianSortedArrays(nums1_large, nums2_large)
    #    print("large:", r)


unittest.main()
