class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        t=k*max(nums) + (k*(k-1)//2)
        return(t)