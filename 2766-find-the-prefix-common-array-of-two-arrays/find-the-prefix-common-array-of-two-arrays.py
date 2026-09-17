class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        for i in range(len(A)):
            l=A[:i+1]
            r=B[:i+1]
            t=0
            for j in range(len(r)):
                if l[j] in r:
                    t+=1
            c.append(t)
        return c