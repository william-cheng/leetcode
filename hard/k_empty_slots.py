
def kEmptySlots(flowers, k):
    rearranged = [(i+1, flowers[i]) for i in range(0, len(flowers))]
    rearranged.sort(key=lambda x:x[1])
    s = 0
    e = s + k + 1
    found_days = []
    prev_min = None
    while e < len(rearranged):
        day = max(rearranged[s][0], rearranged[e][0])
        if k == 0:
            found_days.append(day)
            s += 1
            e += 1
            continue
        if prev_min is None or rearranged[s][0] == prev_min:
            prev_min = min([i[0] for i in rearranged[s+1: e]])
        else:
            prev_min = min(prev_min, rearranged[e-1][0])
        if prev_min > day:
            found_days.append(day)
        s += 1
        e += 1
    if found_days:
        return min(found_days)
    else:
        return -1


import unittest
import k_empty_slot_testdata

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(kEmptySlots([1,3,2], 1), 2)

    def test_2(self):
        self.assertEqual(kEmptySlots([1,2,3], 1), -1)

    def test_3(self):
        self.assertEqual(kEmptySlots([1,2,3], 0), 2)

    def test_4(self):
        self.assertEqual(kEmptySlots([1,3,2], 0), 3)

    def test_long(self):
        flowers = k_empty_slot_testdata.very_long_flowers
        self.assertEqual(kEmptySlots(flowers, 4973), -1) 

unittest.main()
