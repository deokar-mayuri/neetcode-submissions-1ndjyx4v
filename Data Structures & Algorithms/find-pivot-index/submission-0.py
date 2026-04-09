class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, postfix = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        for j in range(len(nums) - 2, -1, -1):
            postfix.append(nums[j] + postfix[-1])
        postfix = postfix[::-1]
        for k in range(len(nums)):
            if prefix[k] == postfix[k]:
                return k
        return -1