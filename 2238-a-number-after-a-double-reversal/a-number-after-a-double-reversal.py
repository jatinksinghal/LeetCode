class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=num
        b,c=0,0
        while a>0:
            r=a%10
            a=a//10
            b=b*10 + r
        while b>0:
            r=b%10
            b=b//10
            c=c*10 + r
        if c==num:
            return True
        else:
            return False