class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        count = dict()
        i = 0
        for c in s:
            if c not in count:
                count[c] = t[i]
                if countS[c] != countT[t[i]]:
                    return False
            else:
                if count[c] != t[i]:
                    return False
            i += 1
        return True