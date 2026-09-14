class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a=[]
        while n>0:
            b=n%10
            n=n//10
            a.append(b)
        a=a[::-1]
        p=sum(a[::2])
        ne=sum(a[1::2])
        return(p-ne)