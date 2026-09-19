class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=[]
        t=0
        n=len(grid)**2
        for i in grid:
            for j in i:
                if j not in a:
                    a.append(j)
                else:
                    t=j
        b=n*(n+1)//2 - sum(a)
        return[t,b]