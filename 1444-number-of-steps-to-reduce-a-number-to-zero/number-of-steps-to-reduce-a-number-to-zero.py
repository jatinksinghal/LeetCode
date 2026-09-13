class Solution:
    def numberOfSteps(self, num: int) -> int:
        t=0
        while num>0:
            a=num%2
            if a==0:
                num=num//2
                t+=1
            else:
                num=num-1
                t+=1
        return t
            
