class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        for c in [0, 1, 2]:
            while c in count and count[c]:
                nums[i] = c
                count[c] -= 1
                i += 1