class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()
        for c in s:
            countS[c] = 1 + countS.get(c, 0)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        for c in countS:
            if c not in countT:
                return False
            if countS[c] != countT[c]:
                return False
        for c in countT:
            if c not in countS:
                return False
        return True