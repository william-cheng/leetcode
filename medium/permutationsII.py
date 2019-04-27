#
# 47. Permutations II

"""Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = set()
        len_nums = len(nums)

        def dfs(tmp, others):
            if len(tmp) == len_nums:
                permutations.add(tuple(tmp))
                return 0

            i = 0
            while i < len(others):
                tmp.append(others[i])
                dfs(tmp, others[:i] + others[i + 1:])
                del tmp[-1]
                i += 1

        dfs([], nums)
        return [list(i) for i in permutations]