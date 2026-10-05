class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f=[]
        for i in matrix:
            f.append(i)
        for j in range(len(f)):
            a=[]
            for i in range(len(f)-1,-1,-1):
                a.append(f[i][j])
            matrix[j]=a
        


        