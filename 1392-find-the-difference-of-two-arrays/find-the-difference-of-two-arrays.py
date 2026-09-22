class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1,n2=[],[]
        for i in nums1:
            if i not in nums2 and i not in n1:
                n1.append(i)
        for j in nums2:
            if j not in nums1 and j not in n2:
                n2.append(j)
        return [n1,n2]
        