class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        # if len(nums1)>len(nums2):
        #     for i in nums2:
        #         if i in nums1:
        #             nums1.pop(nums1.index(i))
        #             a.append(i)
        # else:
        #     for i in nums1:
        #         if i in nums2:
        #             nums2.pop(nums2.index(i))
        #             a.append(i)
        # return a
        for i in nums1:
            if i in nums2:
                a.append(i)
                nums2.pop(nums2.index(i))
        return a