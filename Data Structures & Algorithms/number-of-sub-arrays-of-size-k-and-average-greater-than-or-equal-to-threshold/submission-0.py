class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        total = sum(arr[l:r + 1])
        count = 0
        if float(total) / k >= float(threshold): count += 1
        while r + 1 < len(arr):
            total -= arr[l]
            total += arr[r + 1]
            l, r = l + 1, r + 1
            if float(total) / k >= float(threshold):
                count += 1
        return count