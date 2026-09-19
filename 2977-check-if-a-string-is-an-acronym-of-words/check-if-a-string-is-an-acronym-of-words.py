class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        a=[]
        for i in words:
            a.append(i[0])
        if "".join(a)==s:
            return True
        else:
            return False