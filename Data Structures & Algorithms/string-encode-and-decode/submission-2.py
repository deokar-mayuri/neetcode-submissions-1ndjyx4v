class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j < len(s):
            length = 0
            while s[i] != "#":
                length *= 10
                length += int(s[i])
                i += 1
            i += 1
            j = i
            while length:
                j += 1
                length -= 1
            res.append(s[i:j])
            i = j
        return res
