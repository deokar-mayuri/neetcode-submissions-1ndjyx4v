class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        k = len(nums) - k
        while k:
            num = nums.pop(0)
            nums.append(num)
            k -= 1
        return nums