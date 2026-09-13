class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s,sq=0,0
        while n>0:
            a=n%10
            s+=a
            sq+=a**2
            n=n//10
        if sq-s>=50:
            return True
        else:
            return False