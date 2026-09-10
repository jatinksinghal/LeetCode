class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))
        # a=[]
        # for i in nums1:
        #     if i in nums2:
        #         a.append(i)
        # return(list(set(a)))