class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = []
        count = 0
        for n in nums:
            if n == 0:
                arr.append(count)
                count = 0
            else:
                count += 1
        arr.append(count)
        return max(arr)