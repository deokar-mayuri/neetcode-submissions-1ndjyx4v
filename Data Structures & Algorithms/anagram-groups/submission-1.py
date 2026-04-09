class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            arr[sortedStr].append(s)
        return list(arr.values())