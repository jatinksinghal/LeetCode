class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            a=num%10
            num=num//10 + a
        return num