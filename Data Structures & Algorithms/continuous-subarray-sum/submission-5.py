class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        if sum(nums) == 0:
            return True
        if sum(nums) < k:
            return False
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        for r in range(1, len(prefix)):
            for l in range(r - 1):
                diff = prefix[r] - prefix[l]
                if diff % k == 0:
                    return True
        return False