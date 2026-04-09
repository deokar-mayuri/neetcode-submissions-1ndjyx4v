class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for c in count:
            if count[c] % 2:
                return False
        return True