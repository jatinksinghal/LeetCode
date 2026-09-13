class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 96
        a=(ord(coordinate1[0])-96+int(coordinate1[1]))
        b=(ord(coordinate2[0])-96+int(coordinate2[1]))
        if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
            return True
        else:
            return False