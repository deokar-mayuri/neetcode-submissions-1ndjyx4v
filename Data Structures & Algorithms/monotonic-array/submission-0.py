class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i] and inc == 1:
                return False
            if nums[i - 1] < nums[i] and inc == -1:
                return False
            if inc == 0:
                if nums[i - 1] < nums[i]:
                    inc = 1
                if nums[i - 1] > nums[i]:
                    inc = -1
        return True