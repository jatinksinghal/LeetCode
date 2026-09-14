class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        a=list(str(n))
        b=sorted(list(set(a)))
        d=[]
        m=len(a)
        f=b[0]
        for i in range(len(b)):
            c=str(n).count(b[i])
            d.append(c)
            if c<m:
                m=c
                f=b[i]
        # if str(d).count(str(m))>1:
        #     return
        return int(f)