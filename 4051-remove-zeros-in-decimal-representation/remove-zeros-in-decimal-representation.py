class Solution:
    def removeZeros(self, n: int) -> int:
        t=0
        r=0
        while n>0:
            a=n%10
            n=n//10
            if a!=0:
                t=t*10+a
        while t>0:
            a=t%10
            t=t//10
            r=r*10+a
        return r
            