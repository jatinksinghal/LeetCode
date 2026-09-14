class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        x=0
        while n>0:
            a=n%10
            n=n//10
            if a!=0:
                x=x*10+a
            s+=a
        x=str(x)
        x=int(x[::-1])
        return(x*s)