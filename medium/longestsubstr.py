class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        r_len = 0
        sub = None
        sub_len = 0
        s_len = len(s)
        for i in range(0, s_len):
            sub_max = s_len - i
            print(sub_max, r_len)
            if sub_max < r_len:
                break
            sub = s[i]
            sub_len = 1
            j = i + 1
            while j < s_len:
                if s[j] not in sub:
                    sub += s[j]
                    sub_len += 1
                    j += 1
                else:
                    break
            print("sub: " + sub)
            if sub_len > r_len:
                r_len = sub_len
        return r_len

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
