class Solution:
    def concatenatedBinary(self, n: int) -> int:
        a=[]
        for i in range(1,n+1):
            a.append(format(i,'b'))
        b="".join(a)
        e=(int(b,2))
        return e%(10**9 + 7)