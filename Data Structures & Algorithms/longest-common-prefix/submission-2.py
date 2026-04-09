class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            i, j = 0, 0
            while prefix and i < len(prefix) and j < len(s) and prefix[i] == s[j]:
                i += 1
                j += 1
            if prefix: prefix = prefix[:i]
        return prefix