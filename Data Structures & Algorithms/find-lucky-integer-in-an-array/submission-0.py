class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxFreq = -1
        count = Counter(arr)
        for c in count:
            if count[c] == c:
                maxFreq = max(maxFreq, c)
        return maxFreq