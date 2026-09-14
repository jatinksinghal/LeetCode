class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        a=[]
        b=[]
        for i in range(1,n):
            for j in range (i+1,n+1):
                f=i/j
                if (f not in b) and f<=1:
                    b.append(f)
                    ch=[str(i),"/",str(j)]
                    r="".join(ch)
                    a.append(r)
        return a
                
                