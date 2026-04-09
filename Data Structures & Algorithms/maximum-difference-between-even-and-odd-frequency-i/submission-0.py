class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        cnt = count.values()
        maxOdd, minEven = 0, max(cnt)
        for c in cnt:
            if c % 2: #odd
                maxOdd = max(maxOdd, c)
            else:
                minEven = min(minEven, c)
        diff = maxOdd - minEven
        return diff