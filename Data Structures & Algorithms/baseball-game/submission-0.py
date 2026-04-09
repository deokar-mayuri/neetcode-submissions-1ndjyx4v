class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                a, b = stack[-1], stack[-2]
                stack.append(int(a) + int(b))
            elif op == "D":
                s = stack[-1]
                stack.append(2 * int(s))
            elif op == "C":
                stack.pop()
            else:
                stack.append(op)
        total = 0
        for s in stack:
            total += int(s)
        return total