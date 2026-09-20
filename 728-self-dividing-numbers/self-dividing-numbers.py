class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        t=[]
        for i in range(left,right+1):
            a=[]
            f=[]
            n=i
            while n>0:
                b=n%10
                n=n//10
                a.append(b)
            for j in a:
                if j!=0 and i%j==0 :
                    f.append(j)
                else:
                    break
            if a==f:
                t.append(i)
        return t
        #     t=[]
        #     a,b=[],[]
        #     n1=i
        #     while i>9:
        #         r=i%10
        #         a.append(r)
        #         i=i//10
        #     for j in a:
        #         if n1%j==0:
        #             b.append(j)
        #         else:
        #             break
        #     if len(a)==len(b):
        #         t.append(i)
        # return t