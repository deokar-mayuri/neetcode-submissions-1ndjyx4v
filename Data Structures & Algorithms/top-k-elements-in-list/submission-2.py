class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        freq = defaultdict(list)
        for c in count:
            freq[count[c]].append(c)
        sortedFreq = dict(sorted(freq.items()))
        for s in reversed(sortedFreq):
            for f in sortedFreq[s]:
                res.append(f)
                k -= 1
                if not k:
                    return res
        return res