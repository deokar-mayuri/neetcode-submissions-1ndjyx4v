class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(" ", "")
        num = 0
        op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(- num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)
