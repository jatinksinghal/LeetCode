class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        h={}
        for i in arr:
            h[i]=h.get(i,0)+1
        val=list(h.values())
        print(val)
        for i in val:
            if val.count(i)>1:
                return False
        return True