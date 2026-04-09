class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l < r:
            if people[r] == limit:
                count += 1
                r -= 1
                continue
            elif people[r] < limit:
                if people[l] + people[r] <= limit:
                    l, r = l + 1, r - 1
                    count += 1
                else:
                    r -= 1
                    count += 1
        if l == r:
            if people[l] <= limit:
                count += 1
        return count