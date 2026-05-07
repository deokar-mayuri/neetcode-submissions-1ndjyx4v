class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l, r = l + 1, r - 1
            return [r - l + 1, s[l:r + 1]]
        
        res = 0
        arr = [s[0]]
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                length, pal = helper(i, i + 1)
                res = max(res, length)
                if res == length:
                    arr.append(pal)
            if i - 1 >= 0 and i + 1 < len(s) and s[i + 1] == s[i - 1]:
                length, pal = helper(i - 1, i + 1)
                res = max(res, length)
                if res == length:
                    arr.append(pal)
        return arr[-1]