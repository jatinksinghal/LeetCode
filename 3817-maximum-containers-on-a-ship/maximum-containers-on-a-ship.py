class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        a=n**2
        t=maxWeight//w
        if t<=a:
            return(t)
        else:
            return a
