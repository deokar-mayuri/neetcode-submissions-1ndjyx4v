class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptrS, ptrT = 0, 0
        while ptrS < len(s) and ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
                ptrT += 1
            else:
                ptrS += 1
        return len(t[ptrT:])