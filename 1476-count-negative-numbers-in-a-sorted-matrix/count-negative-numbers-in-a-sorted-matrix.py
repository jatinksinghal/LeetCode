class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        t=0
        for i in grid:
            for j in i:
                if j<0:
                    t+=1
        return t