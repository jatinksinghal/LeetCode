class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        b=sorted(list(set(list(str(n)))))
        # d=[]
        m=len(str(n))
        f=b[0]
        for i in range(len(b)):
            c=str(n).count(b[i])
            # d.append(c)
            if c<m:
                m=c
                f=b[i]
        return int(f)