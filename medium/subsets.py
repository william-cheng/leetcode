#
# 78. Subsets

"""Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []

        def dfs(tmp, idx):
            """
            tmp: the prev path calculated
            idx: the start idx of the up-coming items
            """
            subsets.append(copy.copy(tmp))
            for i in range(idx, len(nums)):
                tmp.append(nums[i])  # add one pissiblity with the upcoming item
                dfs(tmp, i + 1)  # proceed to the next level
                tmp.pop()  # backtrack, must use pop() because it is to pop from the SAME INSTANCE tmp = tmp[:-1] does not do the job (in Python)

        dfs([], 0)
        return subsets