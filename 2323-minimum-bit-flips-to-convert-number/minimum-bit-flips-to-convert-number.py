class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=len(format(start,'b'))
        b=len(format(goal,'b'))
        c=max(a,b)
        a=format(start,f"0{c}b")
        b=format(goal,f"0{c}b")
        t=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                t+=1
        
        return t