#
# 1197 Minimum Knight Moves


class Solution:
    def minKnightMoves(self, x, y):
        dia = x ** 2 + y ** 2
        min_step = float("inf")
        curr = [(0, 0, 0)]
        visited = set([(0, 0)])
        while curr:
            i, j, s = curr.pop(0)
            if (i, j) == (x, y):
                min_step = min(min_step, s)
            if x >= 0 and y >= 0:
                next_ = (
                    (i + 1, j + 2),
                    (i + 2, j + 1),
                    (i - 1, j + 2),
                    (i - 2, j + 1),
                    (i + 1, j - 2),
                    (i + 2, j - 1),
                )
            elif x > 0 and y < 0:
                next_ = (
                    (i + 2, j + 1),
                    (i + 1, j + 1),
                    (i + 1, j - 2),
                    (i + 2, j - 1),
                    (i - 1, j - 2),
                    (i - 2, j - 1),
                )
            elif x <= 0 and y <= 0:
                next_ = (
                    (i + 1, j - 2),
                    (i + 2, j - 1),
                    (i - 1, j - 2),
                    (i - 2, j - 1),
                    (i - 1, j + 2),
                    (i - 2, j + 1),
                )
            else:
                next_ = (
                    (i + 2, j + 1),
                    (i + 1, j + 1),
                    (i + 1, j - 2),
                    (i + 2, j - 1),
                    (i - 1, j - 2),
                    (i - 2, j - 1),
                )
            for a, b in next_:
                if a ** 2 + b ** 2 <= dia and (a, b) not in visited:
                    curr.append((a, b, s + 1))
                    visited.add((a, b))
        return min_step


def test_normal():
    s = Solution()
    #assert s.minKnightMoves(2, 1) == 1
    #assert s.minKnightMoves(2, 211) == 107
    assert s.minKnightMoves(-34, -156) == 78
