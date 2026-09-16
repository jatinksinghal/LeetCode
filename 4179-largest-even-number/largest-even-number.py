class Solution:
    def largestEven(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] in "24680":
                return "".join(s)
                break
            else:
                s.pop(i)
        else:
            return ""  