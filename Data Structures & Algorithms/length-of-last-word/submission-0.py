class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, temp = [], 0
        for c in s:
            if c == " ":
                if temp: length.append(temp)
                temp = 0
            else:
                temp += 1
        if temp: length.append(temp)
        return length[-1]