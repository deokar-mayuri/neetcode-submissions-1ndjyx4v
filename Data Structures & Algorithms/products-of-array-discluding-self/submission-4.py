class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]
        prefix = []
        postfix = []
        p = 1
        for n in nums:
            p *= n
            prefix.append(p)
        postfix = [0] * len(nums)
        p = 1
        for i, n in enumerate(nums[::-1]):
            p *= n
            postfix[i] = p
        postfix = postfix[::-1]
        res = [postfix[1]]
        for i in range(1, len(nums) - 1):
            prod = prefix[i - 1] * postfix[i + 1]
            res.append(prod)
        res.append(prefix[i])
        return res