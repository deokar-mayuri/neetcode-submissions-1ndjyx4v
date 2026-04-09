class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        g = []
        for row in grid:
            for elem in row:
                g.append(elem)
        a, b = 0, 0
        count = Counter(g)
        for e in range(1, len(grid[0]) ** 2 + 1):
            if e not in count:
                b = e
            elif count[e] == 2:
                a = e
        return [a, b]