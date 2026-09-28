class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        h={}
        for i in edges:
            for j in i:
                h[j]=h.get(j,0)+1
        a=max(h.values())
        print(h,a)
        for i in h:
            if h[i]==a:
                return i