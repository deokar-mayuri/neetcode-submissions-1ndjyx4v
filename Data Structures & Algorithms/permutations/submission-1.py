class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for j in range(len(nums)):
                if nums[j] in perm:
                    continue
                perm.append(nums[j])
                backtrack(perm)
                perm.pop()
        backtrack([])
        return res