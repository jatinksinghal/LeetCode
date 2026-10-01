class Solution:
    def arrangeCoins(self, n: int) -> int:
        t=0
        for i in range(1,n+1):
            if (n-i)>=0:
                n=n-i
                t+=1
            if (n-i)<0:
                break
        return t