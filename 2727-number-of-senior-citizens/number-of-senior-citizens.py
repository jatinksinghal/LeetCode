class Solution:
    def countSeniors(self, details: List[str]) -> int:
        t=0
        for i in details:
            a=i[11:13]
            c=int("".join(a))
            if c>60:
                t+=1
        return t
                