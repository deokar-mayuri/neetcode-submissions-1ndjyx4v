class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in  range(n)]
        k = 0
        top, bottom = 0, n
        left, right = 0, n
        while top < bottom and left < right:
            for i in range(left, right):
                k = k + 1
                res[top][i] = k
            top += 1
            for i in range(top, bottom):
                k += 1
                res[i][right - 1] = k
            right -= 1
            for i in range(right - 1, left - 1, -1):
                k += 1
                res[bottom - 1][i] = k
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                k += 1
                res[i][left] = k
            left += 1
        return res