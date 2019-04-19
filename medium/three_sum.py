# 15. 3Sum


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        k = 0
        len_nums = len(nums)
        r = set()
        while k < len_nums:
            tgt = -nums[k]
            i = k + 1
            j = len_nums - 1
            while i < j:
                s = nums[i] + nums[j]
                if s > tgt:
                    j -= 1
                elif s < tgt:
                    i += 1
                else:
                    r.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
            k += 1
        return [list(i) for i in r]


import unittest
from three_sum_testdata import long_data


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(
            self.s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )

    def test_02(self):
        self.assertEqual(self.s.threeSum([-2, 0, 1, 1, 2]), [[-2, 1, 1], [-2, 0, 2]])

    def test_long(self):
        self.assertEqual(len(self.s.threeSum(long_data)), 16258)


unittest.main()
