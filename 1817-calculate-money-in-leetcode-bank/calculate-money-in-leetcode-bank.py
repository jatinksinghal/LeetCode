class Solution:
    def totalMoney(self, n: int) -> int:
        a=n//7
        b=n%7
        c=0
        for i in range(a):
            for j in range(i+1,i+8):
                c+=j
        for i in range(a+1,a+1+b):
            c+=i
        return c