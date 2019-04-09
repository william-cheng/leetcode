#
#

class Solution(object):
    def twoSum(self, nums, target):
        return []


import unittest
class Tests(unittest.TestCase):
    s = None
    def setUp(self):
        self.s = Solution()

    def test_0(self):
        self.assertEqual(self.s.twoSum([2,7,11,15], 9), [0,1])


unittest.main()