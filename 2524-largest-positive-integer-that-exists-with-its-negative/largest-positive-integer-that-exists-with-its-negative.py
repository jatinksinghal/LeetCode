class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        m=-1
        nums=set(nums)
        for i in nums:
            if i*(-1) in nums and i>m:
                m=i
        return m