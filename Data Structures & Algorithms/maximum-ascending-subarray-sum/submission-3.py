class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = []
        curSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curSum += nums[i]
                maxSum = max(curSum, maxSum)
            else:
                curSum = nums[i]
        return maxSum