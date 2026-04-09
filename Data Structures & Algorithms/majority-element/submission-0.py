class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maj = len(nums) // 2
        for n in nums:
            count[n] += 1
            if count[n] > maj:
                return n
        return