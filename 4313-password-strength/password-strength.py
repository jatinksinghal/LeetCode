class Solution:
    def passwordStrength(self, password: str) -> int:
        h,t=set(password),0

        for i in h:
            if i in "abcdefghijklmnopqrstuvwxyz":
                t+=1
            elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                t+=2
            elif i in "1234567890":
                t+=3
            else:
                t+=5
        return t