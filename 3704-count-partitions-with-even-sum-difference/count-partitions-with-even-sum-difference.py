class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            a=nums[:i]
            b=nums[i:]
            a=sum(a)
            b=sum(b)
            c=max(a,b)-min(a,b)
            if c%2==0:
                count+=1
        return count