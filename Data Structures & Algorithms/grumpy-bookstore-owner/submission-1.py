class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, r = 0, minutes - 1
        res = 0
        satisfied = 0
        for c, g in zip(customers, grumpy):
            if not g:
                satisfied += c
        for i in range(l, r + 1):
            if grumpy[i]:
                satisfied += customers[i]
        res = satisfied
        while r + 1 < len(customers):
            if grumpy[l]:
                satisfied -= customers[l]
            if grumpy[r + 1]:
                satisfied += customers[r + 1]
            l, r = l + 1, r + 1
            res = max(res, satisfied)
        return res