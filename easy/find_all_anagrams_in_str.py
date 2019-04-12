class Solution(object):
    def findAnagrams(self, s, p):
        p_sig = {}
        for c in p:
            if c in p_sig:
                p_sig[c] += 1
            else:
                p_sig[c] = 1
        p_sig_str = str(sorted(p_sig.items(), key=lambda x: x[0]))

        i = 0
        r = []
        win_size = len(p)
        computed = set()
        while i + win_size <= len(s):
            if s[i:i+win_size] in computed:
                r.append(i)
                i += 1
                continue
            sig = {}
            for j in range(i, i+win_size):
                c = s[j]
                if c not in p_sig:
                    break
                else:
                    if c in sig:
                        sig[c] += 1
                    else:
                        sig[c] = 1
            if str(sorted(sig.items(), key=lambda x: x[0])) == p_sig_str:
                computed.add(s[i:i+win_size])
                r.append(i)
            i += 1
        return r


import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_long(self):
        s = "a" * 20000
        p = "a" * 10000
        self.assertEqual(len(self.s.findAnagrams(s, p)), 10001)


unittest.main()
