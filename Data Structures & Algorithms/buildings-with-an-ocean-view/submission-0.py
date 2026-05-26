class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, maxHeight = [], 0
        for i in reversed(range(len(heights))):
            if heights[i] > maxHeight:
                res.append(i)
                maxHeight = heights[i]
        return res[::-1]