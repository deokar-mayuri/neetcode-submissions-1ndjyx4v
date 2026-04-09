class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        flag = 0
        for i in range(1, len(nums)):
            if (nums[i - 1] + nums[i]) % 2 != 1:
                flag = 1
        if not flag:
            return True
        return False