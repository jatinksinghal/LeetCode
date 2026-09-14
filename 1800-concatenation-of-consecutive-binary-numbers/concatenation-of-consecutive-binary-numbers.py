class Solution:
    def concatenatedBinary(self, n: int) -> int:
        a=[]
        for i in range(1,n+1):
            a.append(format(i,'b'))
        a="".join(a)
        return (int(a,2))%(10**9 + 7)