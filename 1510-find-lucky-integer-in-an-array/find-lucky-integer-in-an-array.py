class Solution:
    def findLucky(self, arr: list[int]) -> int:
        h={}
        f=[]
        for i in arr:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]==i:
                f.append(i)
        if len(f)!=0:
            return max(f)
        return -1