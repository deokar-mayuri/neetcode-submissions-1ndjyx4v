class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        stack = []
        idx = []
        for i, c in enumerate(arr):
            if c == "(":
                stack.append([i, c])
            if c == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                    continue
                idx.append(i)
        idx.extend(p[0] for p in stack)
        for i in idx[::-1]:
            arr.pop(i)
        return "".join(arr)