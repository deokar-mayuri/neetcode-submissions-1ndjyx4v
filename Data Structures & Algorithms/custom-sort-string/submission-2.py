class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not order:
            return s
        res = []
        count = Counter(s)
        for o in order:
            if o in s:
                while count[o]:
                    res.append(o)
                    count[o] -= 1
                count.pop(o)
        for c in count:
            while count[c]:
                res.append(c)
                count[c] -= 1
        return "".join(res)