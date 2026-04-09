class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if not s:
            return 0
        res = 1
        while r < len(s) and s[r] == s[l]:
            l += 1
            r += 1
        if r < len(s) and s[l] != s[r]: res = 2
        while r + 1 < len(s):
            r += 1
            while s[r] in s[l:r]:
                l += 1
            res = max(res, len(s[l: r + 1]))
        return res