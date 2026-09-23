class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h={}
        c=0
        for i in s:
            h[i]=h.get(i,0)+1
        for i in t:
            h[i]=h.get(i,0)-1
        for i in h:
            if h[i]>0:
                c+=h[i]
        return c