class Solution:
    def countSeniors(self, details: List[str]) -> int:
        t=0
        for i in details:
            a=i[11:13]
            c=int("".join(a))
            # for i in a:
            #     c=c*10+(int(i))
            if c>60:
                t+=1
        return t
                