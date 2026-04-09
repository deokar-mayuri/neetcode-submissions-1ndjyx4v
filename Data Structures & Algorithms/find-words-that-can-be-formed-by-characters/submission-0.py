class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        ch = Counter(chars)
        for w in words:
            count = Counter(w)
            flag = 0
            for c in count:
                if c not in ch:
                    flag = 1
                    continue
                if count[c] > ch[c]:
                    flag = 1
                    continue
            if not flag: res += len(w)
        return res