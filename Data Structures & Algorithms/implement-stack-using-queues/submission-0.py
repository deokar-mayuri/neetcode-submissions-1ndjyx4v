class MyStack:

    def __init__(self):
        self.p = collections.deque()
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        while(self.p):
            self.q.append(self.p.popleft())
        self.q, self.p = self.p, self.q

    def pop(self) -> int:
        return self.p.popleft()

    def top(self) -> int:
        return self.p[0]

    def empty(self) -> bool:
        return len(self.p) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()