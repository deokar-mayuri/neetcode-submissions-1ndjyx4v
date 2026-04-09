class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count1 = Counter(s1)
        l, r = 0, len(s1) - 1
        count2 = defaultdict(int)
        for c in s2[l:r + 1]:
            if c in s1:
                count2[c] += 1
        flag = 0
        for c in count1:
            if count1[c] != count2[c]:
                flag = 1
        if not flag: return True
        while r + 1 < len(s2):
            if s2[l] in s1: count2[s2[l]] -= 1
            l, r = l + 1, r + 1
            if s2[r] not in s1:
                continue
            count2[s2[r]] += 1
            if count1 == count2:
                return True
        return False