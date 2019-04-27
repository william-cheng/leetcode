#
# 46. Permutations


"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []

        def dfs(tmp, others):
            if len(tmp) == len(nums):
                permutations.append(copy.copy(tmp))
                return 0

            i = 0
            while i < len(others):
                tmp.append(others[i])
                dfs(tmp, others[:i] + others[i + 1:])
                del tmp[-1]
                i += 1

        dfs([], nums)
        return permutations