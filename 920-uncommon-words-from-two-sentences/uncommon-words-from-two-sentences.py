class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        a=[]
        s1=s1.split()
        s2=s2.split()
        for i in s1:
            if i not in s2 and s1.count(i)==1:
                a.append(i)
        for i in s2:
            if i not in s1 and s2.count(i)==1:
                a.append(i)
        return a