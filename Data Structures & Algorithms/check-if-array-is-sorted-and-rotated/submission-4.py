class Solution:
    def check(self, nums: List[int]) -> bool:
        maxNum = max(nums)
        flag = 0
        if len(nums) < 3:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break
        if i == len(nums) - 2 and nums[-1] >= nums[0]:
            return True
        if i == len(nums) - 2 and nums[-1] < nums[0]:
            return False
        nums = nums[i + 1:] + nums[:i + 1]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True