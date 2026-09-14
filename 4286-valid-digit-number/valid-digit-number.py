class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        a=list(str(n))
        if (str(x) in a) and (a[0]!=str(x)):
            return True
        else:
            return False