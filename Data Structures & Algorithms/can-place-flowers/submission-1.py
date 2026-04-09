class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if not (flowerbed[i - 1] or flowerbed[i] or flowerbed[i + 1]):
                res += 1
                flowerbed[i] = 1
        return res >= n