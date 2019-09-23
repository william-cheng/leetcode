class Solution:
    def assignBikes(self, workers, bikes):
        min_dist = float("inf")
        computed = {}

        def dt(pc, rest_workers, rest_bikes):
            nonlocal min_dist
            nonlocal computed

            if not rest_workers:
                min_dist = min(min_dist, pc)
                return

            for i in range(len(rest_workers)):
                w_x, w_y = rest_workers[i]
                for j in range(len(rest_bikes)):
                    b_x, b_y = rest_bikes[j]
                    k = (w_x, w_y, b_x, b_y)
                    if k not in computed:
                        d = abs(w_x - b_x) + abs(w_y - b_y)
                        computed[k] = d
                    else:
                        d = computed[k]
                    if pc + d < min_dist:
                        dt(
                            pc + d,
                            rest_workers[:i] + rest_workers[i + 1 :],
                            rest_bikes[:j] + rest_bikes[j + 1 :],
                        )

        dt(0, workers, bikes)
        return min_dist


def test_01():
    workers = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
    bikes = [
        [0, 999],
        [1, 999],
        [2, 999],
        [3, 999],
        [4, 999],
        [5, 999],
        [6, 999],
        [7, 999],
        [8, 999],
    ]
    assert 4995 == Solution().assignBikes(workers, bikes)
