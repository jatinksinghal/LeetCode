class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in h:
            if i%2==0 and h[i]==1:
                return i
        return -1