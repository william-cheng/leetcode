# 283 Move Zeros


class Solution(object):
    def moveZeros(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1
        return nums


import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_00(self):
        self.assertEqual(self.s.moveZeros([0]), [0])

    def test_01(self):
        self.assertEqual(self.s.moveZeros([1]), [1])

    def test_02(self):
        self.assertEqual(self.s.moveZeros([0, 1]), [1, 0])

    def test_03(self):
        self.assertEqual(self.s.moveZeros([1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0])

    def test_04(self):
        self.assertEqual(self.s.moveZeros([0, 1, 2, 0, 3, 4, 0]), [1, 2, 3, 4, 0, 0, 0])


unittest.main()
