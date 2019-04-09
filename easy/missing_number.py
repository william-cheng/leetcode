
class Solution(object):
    def missingNumber(self, nums):
        i = 0
        missing = None
        while i < len(nums):
            if nums[i] >= len(nums):
                missing = i
                i += 1
            elif nums[i] == -1:
                i += 1
            elif nums[i] == i:
                nums[i] = -1
                i += 1
            else:
                tmp = nums[nums[i]]
                nums[nums[i]] = -1
                nums[i] = tmp
        return missing if missing is not None else len(nums)


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Solution()

    def test_0(self):
        self.assertEqual(self.s.missingNumber([0]), 1)

    def test_1(self):
        self.assertEqual(self.s.missingNumber([3, 0, 1]), 2)

    def test_2(self):
        self.assertEqual(self.s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_3(self):
        self.assertEqual(self.s.missingNumber([9, 6, 8, 2, 3, 5, 7, 0, 1]), 4)

unittest.main()
