class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        while l < len(fruits):
            r = l
            count = [fruits[r]]
            total = 1
            while r + 1 < len(fruits) and len(count) <= 2:
                r += 1
                if fruits[r] not in count:
                    count.append(fruits[r])
                if len(count) <= 2: total += 1
                res = max(res, total)
            l += 1
            res = max(res, total)
            total = 0
            count = []
        return res