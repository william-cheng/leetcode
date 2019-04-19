# 16. 3Sum Closest
#


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        nums.sort()
        k = 0
        closest = None
        len_nums = len(nums)
        while k < len_nums:
            two_sum_tgt = target - nums[k]
            i = k + 1
            j = len_nums - 1
            while i < j:
                two_sum = nums[i] + nums[j]
                gap = abs(two_sum_tgt - two_sum)
                if closest is None:
                    closest = (two_sum + nums[k], gap)
                elif gap < closest[1]:
                    closest = (two_sum + nums[k], gap)
                if two_sum < two_sum_tgt:
                    i += 1
                elif two_sum > two_sum_tgt:
                    j -= 1
                else:
                    return target
            k += 1
        return closest[0]


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.threeSumClosest([-1,2,1,4], 1), 2)

    def test_02(self):
        self.assertEqual(self.s.threeSumClosest([0,1,2], 3), 3)


unittest.main()