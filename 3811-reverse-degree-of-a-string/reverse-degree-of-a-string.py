class Solution:
    def reverseDegree(self, s: str) -> int:
        t=0
        for i in range(len(s)):
            a=ord('z')-ord(s[i])+1
            t+= (i+1)*a
        return t