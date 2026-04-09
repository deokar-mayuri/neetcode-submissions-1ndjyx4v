class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        freq = len(nums) // 3
        for c in count:
            if count[c] > freq:
                res.append(c)
        return res