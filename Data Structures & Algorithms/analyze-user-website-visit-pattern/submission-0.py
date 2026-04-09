class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()
        seq = defaultdict(list)
        for time, user, site in arr:
            seq[user].append(site)
        count = defaultdict(int)
        for user in seq:
            pat = set()
            cur = seq[user]
            for i in range(len(cur) - 2):
                for j in range(i + 1, len(cur) - 1):
                    for k in range(j + 1, len(cur)):
                        pat.add((cur[i], cur[j], cur[k]))
            for p in pat:
                count[p] += 1
        maxCount = 0
        res = tuple()
        for c in count:
            if count[c] > maxCount or (count[c] == maxCount and c < res):
                maxCount = count[c]
                res = c
        return list(res)
