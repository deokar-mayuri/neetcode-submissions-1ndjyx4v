class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            for j in range(i + 1, n):
                minHeight = min(heights[i], heights[j])
                base = j - i
                area = base * minHeight
                maxArea = max(area, maxArea)
        return maxArea