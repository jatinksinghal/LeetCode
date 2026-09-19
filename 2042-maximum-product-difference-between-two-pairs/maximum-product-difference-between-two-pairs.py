class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a=sorted(nums)
        t=abs((a[0]*a[1])-(a[-1]*a[-2]))
        return t