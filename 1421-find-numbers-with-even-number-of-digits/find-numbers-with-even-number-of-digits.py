class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        t=0
        for i in range(len(nums)):
            a=str(nums[i]) 
            # print(a) 
            if len(a)%2==0:
                t+=1
        return t