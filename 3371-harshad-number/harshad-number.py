class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=x
        c=0
        while a>0:
            r=a%10
            a=a//10
            c+=r
        if x%c==0:
            return c
        else:
            return -1