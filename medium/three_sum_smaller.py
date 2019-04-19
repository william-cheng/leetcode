# 259. 2Sum Smaller
#


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: int
        """
        nums.sort()
        count = 0
        k = 0
        len_nums = len(nums)
        while k < len_nums:
            i = k + 1
            j = len_nums - 1
            vk = nums[k]
            while i < j:
                s = vk + nums[i] + nums[j]
                if s < target:
                    count += j - i
                    i += 1
                    j = len_nums - 1
                else:
                    j -= 1
            k += 1
        return count


import unittest
import three_sum_smaller_testdata


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.threeSumSmaller([-2, 0, 1, 3], 2), 2)

    def test_02(self):
        self.assertEqual(self.s.threeSumSmaller([3, 1, 0, -2], 4), 3)

    def test_long(self):
        self.assertEqual(
            self.s.threeSumSmaller(
                three_sum_smaller_testdata.nums, three_sum_smaller_testdata.target
            ),
            97107,
        )


unittest.main()
