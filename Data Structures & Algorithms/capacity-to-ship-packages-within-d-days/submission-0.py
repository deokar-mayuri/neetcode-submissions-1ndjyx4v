class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        def canShip(cap):
            curCap = cap
            ships = 1
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cap
                curCap -= w
            return ships <= days
        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res