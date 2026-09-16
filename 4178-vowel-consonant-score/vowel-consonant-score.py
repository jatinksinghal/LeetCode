class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v,c=0,0
        for i in s:
            if i in "aeiou":
                v+=1
            elif i in "bcdfghjklmnpqrstvwxyz":
                c+=1
        if c>0:
            return v//c
        return 0