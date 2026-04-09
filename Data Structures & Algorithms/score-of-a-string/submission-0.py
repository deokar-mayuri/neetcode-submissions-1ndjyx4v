class Solution:
    def scoreOfString(self, s: str) -> int:
        absSum = 0
        for i in range(1, len(s)):
            absSum += abs(ord(s[i - 1]) - ord(s[i]))
        return absSum