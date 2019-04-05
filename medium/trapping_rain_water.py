#

"""#42 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

import unittest


def trap_rain_water_slow(height):
    # calculate water row by row, water is trapped by two 1s
    # 0 0 1 0 0 1 0 0 1 -> 4 units of water
    row_len = len(height)
    height_sum = sum(height)
    water = 0
    #for row in matrix:
    while height_sum:
        i = 0
        while i < row_len:
            if height[i] > 0:
                height[i] -= 1
                height_sum -= 1
                j = i + 1
                while j < row_len:
                    if height[j] > 0:
                        height[j] -= 1
                        height_sum -= 1
                        water += j - i - 1
                        i = j
                        j = i + 1
                    else:
                        j += 1
                if j == row_len:
                    break
            else:
                i += 1
    return water


def trap_rain_water(height):
    if not height:
        return 0
    i = water = 0
    max_h = max(height)
    len_h = len(height)
    while i < len_h:
        if height[i] == max_h:
            water += trap_rain_water(height[:i] + [max(height[:i])])
            j = i + 1
            found = False
            while j < len_h:
                if height[j] == max_h:
                    water += sum([max_h - h for h in height[i+1:j]]) + trap_rain_water([max(height[j+1:)] + height[j+1:])
                    found = True
                else:
                    j += 1
            if not found:
                water += trap_rain_water([max(height[i+1:])] + height[i+1:])
            if j == len_h:
                break
        else:
            i += 1
    return water


from trapping_rain_water_testcase import height
class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
    #def test_2(self):
        self.assertEqual(trap_rain_water([0,0,0,0,0]), 0)
    #def test_3(self):
    #    self.assertEqual(trap_rain_water(height), 174801674)
    def test_4(self):
        self.assertEqual(trap_rain_water([1]), 0)


unittest.main()
