class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = -1
        for row in matrix:
            idx += 1
            if row[0] > target:
                idx -= 1
                break
        l = 0
        r = len(matrix[idx]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[idx][m] < target:
                l = m + 1
            elif matrix[idx][m] > target:
                r = m - 1
            else:
                return True
        return False