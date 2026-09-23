class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        h={}
        t=[]
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]>1:
                t.append(i)
        return t