class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        h={}
        f=[]
        for i in sorted(arr1):
            h[i]=h.get(i,0)+1
        for i in arr2:
            for j in range(h[i]):
                f.append(i)
                h[i]-=1
        for i in h:
            if h[i]>0:
                for j in range(h[i]):
                    f.append(i)
        
        return(f)