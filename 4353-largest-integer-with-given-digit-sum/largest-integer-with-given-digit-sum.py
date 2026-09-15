class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        for i in range(10**n -1,-1,-1):
            a=list(str(i))
            t=0
            for j in a:
                t+=int(j)
            if t==s:
                return i
                break
        else:
            return -1