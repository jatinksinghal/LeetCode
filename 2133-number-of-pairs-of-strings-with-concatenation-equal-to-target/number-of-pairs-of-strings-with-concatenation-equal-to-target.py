class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        t=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    t+=1
        return t