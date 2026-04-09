class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        minNum = float("inf")
        maxNum = 0
        for n in nums:
            if n > maxNum:
                maxNum = n
            if n < minNum:
                minNum = n
        for n in range(minNum, maxNum + 1):
            if n in nums:
                while count[n]:
                    res.append(n)
                    count[n] -= 1
        return res