class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        cur = []
        def dfs(idx, cur, total):
            if total == target:
                if cur not in self.res: self.res.append(cur.copy())
            if idx >= len(nums) or total > target:
                return
            cur.append(nums[idx])
            dfs(idx, cur, total + nums[idx])
            cur.pop()
            dfs(idx + 1, cur, total)
        dfs(0, [], 0)
        return self.res