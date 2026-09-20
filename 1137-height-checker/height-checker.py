class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        a=sorted(heights)
        t=0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                t+=1
        return t