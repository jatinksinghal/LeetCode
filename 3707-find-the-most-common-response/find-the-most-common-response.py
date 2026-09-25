class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        a,h=[],{}
        for i in responses:
            a.extend(list(set(i)))
        for i in a:
            h[i]=h.get(i,0)+1
        m=max(h.values())
        f=[]
        for i in h:
            if h[i]==m:
                f.append(i)
        f=sorted(f)
        t=[]
        for i in f:
            b=ord(i[0])%95
            t.append(b)
        c=t.index(min(t))
        return(f[c])
