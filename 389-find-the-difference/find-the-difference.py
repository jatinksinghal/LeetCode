class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=list(s)
        b=""
        for i in t:
            if i in a:
                a.pop(a.index(i))
            else:
                a.append(i)
        return "".join(a)