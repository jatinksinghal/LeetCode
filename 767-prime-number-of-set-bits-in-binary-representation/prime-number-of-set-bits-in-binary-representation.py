class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        t=0
        for i in range(left,right+1):
            a=format(i,'b')
            b=a.count("1")
            if b>1:
                for j in range(2,b//2+1):
                    if b%j==0:
                        break
                else:
                    t+=1
        return t
