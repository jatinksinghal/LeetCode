class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n>0:
            a=n
            c=1
            while a>0:
                r=a%10
                c*=r
                a=a//10
            if c%t==0:
                return n
                break
            else:
                n=n+1