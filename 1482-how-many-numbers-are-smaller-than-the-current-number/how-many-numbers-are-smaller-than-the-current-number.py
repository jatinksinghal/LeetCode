class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            t=0
            for j in nums:
                if i>j:
                    t+=1
            a.append(t)
        return a