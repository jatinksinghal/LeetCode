class Solution:
    def maxFreqSum(self, s: str) -> int:
        t1,t2=0,0
        for i in "aeiou":
            t=s.count(i)
            if t>t1:
                t1=t
        for i in "bcdfghjklmnpqrstvwxyz":
            t=s.count(i)
            if t>t2:
                t2=t
        return t1+t2