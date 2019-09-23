#
# 1186 maximum subarray sum with one deletion


class Solution:
    def maximumSum(self, a):
        ignored, notignored, res = 0, 0, a[0]
        for num in a:
            if num >= 0:
                ignored += num
                #notignored += num
            else:
                ignored = max(ignored + num, notignored)
            notignored += num

            res = max(
                    [
                        res,
                        ignored if ignored != 0 else -float("inf"),
                        notignored if notignored != 0 else -float("inf"),
                    ]
            )
            ignored = max(ignored, 0)
            notignored = max(notignored, 0)
            print(ignored, notignored, res)

        return max(res, max(a))


def test_solution():
    s = Solution()
    print("")
    #assert s.maximumSum([1, -4, -5, -2, 5, 0, 2]) == 7
    #assert s.maximumSum([1, -4, -5, -2, 5, 0, -1, 2]) == 7
    #assert s.maximumSum([1, -2, 3]) == 4
    assert s.maximumSum([1, -2, -2, 3]) == 3
