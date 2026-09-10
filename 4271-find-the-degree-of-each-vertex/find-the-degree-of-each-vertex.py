class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a=[]
        for i in range(len(matrix)):
            t=0
            for j in range(len(matrix[i])):
                t+=matrix[i][j]
            a.append(t)
        return a