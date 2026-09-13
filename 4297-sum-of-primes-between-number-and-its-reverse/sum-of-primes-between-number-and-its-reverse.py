class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        newn,t,rev=n,[],0
        rev=0

        while newn>0:
            a=newn%10
            newn=newn//10
            rev=rev*10 + a
        for i in range(min(rev,n),max(rev,n)+1):
            for j in range(2,i//2 +1):
                if i%j==0:
                    break
            else:
                t.append(i)
        if 1 in t:
            t.pop(t.index(1))
        return sum(t)