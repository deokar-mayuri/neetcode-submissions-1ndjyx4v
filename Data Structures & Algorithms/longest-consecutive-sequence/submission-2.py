class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        start = []
        for n in nums:
            if n - 1 not in nums and n + 1 in nums:
                start.append(n)
        res = 0
        for s in start:
            count = 1
            while s + 1 in nums:
                count += 1
                s += 1
            res = max(res, count)
        return res if res else 1