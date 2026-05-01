class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap.append([x ** 2 + y ** 2, [x, y]])
        heapq.heapify(minHeap)
        res = []
        while k:
            res.append(heapq.heappop(minHeap))
            k -= 1
        return [q for p, q in res]