class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for h in range(len(heights)):
            if heights[h] != expected[h]:
                count += 1
        return count