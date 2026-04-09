class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxCount = 1
        count = 1
        inc = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]: # inc
                if inc > 0:
                    count += 1
                else:
                    count = 2
                    inc = 1
            elif nums[i - 1] > nums[i]: # dec
                if inc < 0:
                    count += 1
                else:
                    count = 2
                    inc = -1
            else:
                count = 1
                inc = 0
            maxCount = max(maxCount, count)
        return maxCount