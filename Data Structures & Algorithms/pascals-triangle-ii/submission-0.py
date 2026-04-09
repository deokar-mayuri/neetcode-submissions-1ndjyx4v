class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [0, 1, 1, 0]
        while rowIndex > 1:
            newRow = [0] * (len(row) + 1)
            for i in range(1, len(newRow) - 1):
                newRow[i] = row[i - 1] + row[i]
            row = newRow
            rowIndex -= 1
        return row[1:-1]