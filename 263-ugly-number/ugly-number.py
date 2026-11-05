class Solution:
    def isUgly(self, n: int) -> bool:
        a=n
        if(n<=0):
            return False
        while a>1 or a<-1:
            if(a%2==0):
                a=a//2
                continue
            elif(a%3==0):
                a=a//3
                continue
            elif(a%5==0):
                a=a//5
                continue
            else:
                return False
        return True

        
