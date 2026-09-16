class Solution:
    def maxDistinct(self, s: str) -> int:
        a=[]
        for i in s:
            if i not in a:
                a.append(i)
        return len(a)
    #    a=len(list(set(s)))
    #    return(a) 