class Solution:
    def countEven(self, num: int) -> int:
        t=0
        for i in range(1,num+1):
            n=0
            while i>0:
                a=i%10
                i=i//10
                n+=a
            if n%2==0:
                t+=1
        return t