class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a=[]
        for i in word:
            if (i.lower() in word )and (i.upper() in word) and (i not in a):
                a.append(i)
        return len(a)//2