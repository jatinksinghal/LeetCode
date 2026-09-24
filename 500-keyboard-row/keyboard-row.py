class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        f=[]
        for i in words:
            a=set(i)
            if a <= set("QWERTYUIOPqwertyuiop"):
                f.append(i)
            elif a <= set("ASDFGHJKLasdfghjkl"):
                f.append(i)
            elif a <= set("zxcvbnmZXCVBNM"):
                f.append(i)
        return f