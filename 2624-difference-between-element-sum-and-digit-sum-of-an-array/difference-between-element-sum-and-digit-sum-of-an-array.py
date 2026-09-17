class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        t=0
        for i in nums:
            while i>0:
                a=i%10
                i=i//10
                t+=a
        return abs(t-sum(nums))