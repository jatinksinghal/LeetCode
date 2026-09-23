class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        h={}
        t=0
        for i in nums:
            h[i]=h.get(i,0)+1
        a=max(h.values())
        for i in h:
            if h[i]==a:
                t+=a
        return t