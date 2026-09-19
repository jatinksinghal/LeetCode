class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        a=(sum(nums2)-sum(nums1))//len(nums1)
        return a