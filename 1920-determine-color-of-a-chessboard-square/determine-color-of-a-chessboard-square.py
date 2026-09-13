class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a=list(coordinates)
        a1=ord(a[0])
        if ((a1-96)+int(a[1]))%2==0:
            return False
        else:
            return True