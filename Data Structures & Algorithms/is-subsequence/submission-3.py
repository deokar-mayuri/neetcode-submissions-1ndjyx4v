class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrS, ptrT = 0, 0
        if not s:
            return True
        if not t:
            return False
        while ptrT < len(t) and ptrS < len(s):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
                ptrT += 1
            else:
                ptrT += 1
        return True if ptrS == len(s) else False