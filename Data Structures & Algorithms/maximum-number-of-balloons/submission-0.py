class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        instance = "balloon"
        count = Counter(instance)
        textCount = Counter(text)
        minCount = len(text)
        for c in count:
            length = textCount[c]
            required = count[c]
            minCount = min(minCount, length // required)
        return minCount