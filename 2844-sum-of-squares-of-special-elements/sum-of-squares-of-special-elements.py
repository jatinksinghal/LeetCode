class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        t=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                t+= nums[i]**2
        return t