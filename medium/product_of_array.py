class Solution(object):
    def productExceptSelf(self, nums):
        cache = {}
        length = len(nums)
        end = length - 1
        i = length - 2
        cache[(i, end)] = nums[end] * nums[i]

        i -= 1
        while i > 0:
            cache[(i, end)] = nums[i] * cache[(i + 1, end)]
            i -= 1

        i = 1
        cache[(0, i)] = nums[0] * nums[i]
        i += 1
        while i < length:
            cache[(0, i)] = nums[i] * cache[(0, i - 1)]
            i += 1

        cache[(0, 0)] = nums[0]
        cache[(end, end)] = nums[-1]
        i = 1
        r = []
        r.append(cache[(1, end)])
        while i < len(nums) - 1:
            r.append(cache[(0, i - 1)] * cache[(i + 1, end)])
            i += 1
        r.append(cache[(0, end - 1)])
        return r


import unittest


class Tests(unittest.TestCase):
    s = None

    def setUp(self):
        self.s = Solution()

    def test_0(self):
        self.assertEqual(self.s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_1(self):
        self.assertEqual(self.s.productExceptSelf([1, 2, 3, 4, 5]))


unittest.main()
