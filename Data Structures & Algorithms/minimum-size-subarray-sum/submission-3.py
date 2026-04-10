class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        res = float("inf")
        while l < len(nums):
            r = l
            while r < len(nums):
                total += nums[r]
                if total >= target:
                    res = min(res, r - l + 1)
                    break
                r += 1
            l += 1
            r = l
            total = 0
        return 0 if res == float("inf") else res