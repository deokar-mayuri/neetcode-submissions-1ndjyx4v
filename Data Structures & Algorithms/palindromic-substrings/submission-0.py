class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            l, r = l + 1, r - 1
            return count
        res = 0
        for i in range(len(s)):
            res += 1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                res += helper(i, i + 1)
            if i - 1 >= 0 and i + 1 < len(s) and s[i + 1] == s[i - 1]:
                res += helper(i - 1, i + 1)
        return res