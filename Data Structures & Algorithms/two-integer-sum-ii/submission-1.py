class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l < len(numbers):
            diff = target - numbers[l]
            if diff in numbers[l + 1:]:
                idx = numbers.index(diff)
                return [l + 1, idx + 1]
            l += 1
        return