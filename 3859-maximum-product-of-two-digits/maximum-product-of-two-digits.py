class Solution:
    def maxProduct(self, n: int) -> int:
        a=[]
        s=1
        while n>0:
            b=n%10
            n=n//10
            a.append(b)
        for _ in range(2):
            s*=max(a)
            a.remove(max(a))
        return s