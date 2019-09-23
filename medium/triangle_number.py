# 611. Valid Triangle Number
class Solution(object):
    def triangleNumber(self, nums):
        nums = filter(lambda x:x>0, nums)
        nums.sort(reverse=True)
        k = 0
        count = 0
        len_nums = len(nums)
        while k < len(nums):
            tgt = nums[k]
            i = k + 1
            j = len_nums - 1
            while i < j:
                s = nums[i] + nums[j]
                if s > tgt:
                    count += j - i
                    i += 1
                    j = len_nums - 1
                else:
                    j -= 1
            k += 1
        return count


import unittest
from triangle_number_testdata import long_nums
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_01(self):
        self.assertEqual(self.s.triangleNumber([2,2,3,4]), 3)

    def test_02(self):
        self.assertEqual(self.s.triangleNumber([1,2,3,4,5,6]), 7)

    def test_03(self):
        self.assertEqual(self.s.triangleNumber([1,1,1]), 1)

    def test_04(self):
        self.assertEqual(self.s.triangleNumber(long_nums), 80688225)


unittest.main()