class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        store = []
        while l < r:
            left, right = heights[l], heights[r]
            store.append(min(left, right) * abs(l - r))
            if left >= right:
                r -= 1
            else:
                l += 1
        return max(store)       