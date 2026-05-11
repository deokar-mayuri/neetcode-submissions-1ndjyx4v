class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:   
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit = set()
        minHeap = [[0, 0, 0]]
        ROWS, COLS = len(heights), len(heights[0])
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visit:
                    continue
                maxDiff = max(diff, abs(heights[r][c] - heights[row][col]))
                heapq.heappush(minHeap, [maxDiff, row, col])            