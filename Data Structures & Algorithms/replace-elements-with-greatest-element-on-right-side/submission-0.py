class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * (len(arr) - 1) + [-1]
        maxElem = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            maxElem = max(maxElem, arr[i + 1])
            res[i] += maxElem
        return res
