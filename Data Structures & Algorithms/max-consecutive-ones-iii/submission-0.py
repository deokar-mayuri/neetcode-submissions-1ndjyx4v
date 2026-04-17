class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if not nums[r]:
                zero += 1
            while l < r and zero > k:
                if not nums[l]:
                    zero -= 1
                l += 1
            if zero <= k: res = max(res, r - l + 1)
        return res