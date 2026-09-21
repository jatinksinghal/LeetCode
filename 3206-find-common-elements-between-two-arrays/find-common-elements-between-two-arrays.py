class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[0,0]
        for i in nums1:
            if i in nums2:
                a[0]+=1
        for j in nums2:
            if j in nums1:
                a[1]+=1
        return a