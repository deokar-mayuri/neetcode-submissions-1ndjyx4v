class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        visited = []
        for a in arr:
            if a not in visited:
                visited.append(a)
                res.append(a)
            else:
                if a in res: res.remove(a)
        return res[k - 1] if (k - 1) < len(res) else ""