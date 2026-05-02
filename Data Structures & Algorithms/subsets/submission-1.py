class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        subset = []
        def dfs(idx):
            if idx >= len(nums):
                self.res.append(subset.copy())
                return
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return self.res