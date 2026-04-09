class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        res = []
        while l < len(nums) - 1:
            r = l + 1
            while r < len(nums):
                diff = - (nums[l] + nums[r])
                if diff in nums[r + 1:]:
                    arr = [nums[l], nums[r], diff]
                    arr.sort()
                    if arr not in res: res.append(arr)
                r += 1
            l += 1
        return res