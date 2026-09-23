class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        h={}
        t=0
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]%k==0:
                t+=(i*h[i])
        return t