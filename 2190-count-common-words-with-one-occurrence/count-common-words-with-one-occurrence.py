class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        a=[]
        for i in words2:
            if i in words1 and i not in a and words1.count(i)==1 and words2.count(i)==1:
                a.append(i)
        return len(a)