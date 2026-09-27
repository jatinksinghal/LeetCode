class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]==1:
                return s.index(i)
        return -1