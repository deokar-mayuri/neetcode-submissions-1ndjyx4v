class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                add = stack.pop() + stack.pop()
                stack.append(add)
            elif t == "-":
                num = stack.pop()
                sub = stack.pop() - num
                stack.append(sub)
            elif t == "*":
                mul = stack.pop() * stack.pop()
                stack.append(mul)
            elif t == "/":
                num = stack.pop()
                div = stack.pop() / num
                stack.append(int(float(div)))
            else:
                stack.append(int(t))
        return stack[-1]