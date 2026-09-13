class Solution:
    def minimumFlips(self, n: int) -> int:
        a=format(n,'b')
        b=a[::-1]
        t=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                t+=1
        return t