class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        index = defaultdict(int)
        for n in nums:
            index[n] += 1
        for i in index:
            count = 0
            j = index[i]
            j -= 1
            while j:
                count += j
                j -= 1
            res += count
        return res