class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        a=[]
        for i in range(len(names)):
            c=heights.index(max(heights))
            a.append(names[c])
            heights[c]=0
        return a