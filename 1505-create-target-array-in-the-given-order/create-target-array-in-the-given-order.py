class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        t=[]
        for i in range(len(nums)):
            j=index[i]
            n=nums[i]
            t.insert(j,n)
        return t