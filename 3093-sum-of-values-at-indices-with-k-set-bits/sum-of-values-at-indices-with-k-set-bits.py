class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        t=0
        for i in range(len(nums)):
            a=format(i,'b').count('1')
            if a==k:
                t+=nums[i]
        return t