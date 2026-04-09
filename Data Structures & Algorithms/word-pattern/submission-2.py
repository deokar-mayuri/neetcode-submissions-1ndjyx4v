class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        pair = defaultdict(str)
        for c in range(len(pattern)):
            if pattern[c] in pair and pair[pattern[c]] != words[c]:
                return False
            if words[c] in pair.values():
                if pair[pattern[c]] == words[c]:
                    continue
                return False
            pair[pattern[c]] = words[c]
        return True