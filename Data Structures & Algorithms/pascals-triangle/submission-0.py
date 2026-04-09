class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        for n in range(1, numRows):
            row = [0] + res[-1] + [0]
            newRow = []
            for i in range(len(row) - 1):
                newRow += [row[i] + row[i + 1]]
            res.append(newRow)
        return res