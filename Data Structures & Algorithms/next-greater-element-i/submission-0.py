class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        def nextGreater(x):
            for i in range(x + 1, len(nums2)):
                if nums2[i] > nums2[x]:
                    return nums2[i]
            return -1
        nums2 += [0]
        for n in nums1:
            index = nums2.index(n)
            res.append(nextGreater(index))
        return res