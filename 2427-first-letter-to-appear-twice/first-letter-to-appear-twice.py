class Solution:
    def repeatedCharacter(self, s: str) -> str:
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
            if h[i]>1:
                return i