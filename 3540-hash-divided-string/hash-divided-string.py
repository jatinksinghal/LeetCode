class Solution:
    def stringHash(self, s: str, k: int) -> str:
        cj=[]
        for i in range(0,len(s),k):
            a=s[i:i+k]
            t=0
            for i in range(len(a)):
                w=ord(a[i])-97
                print(w)
                t+=w
            t=t%26
            cj.append(chr(97+t))
        cj="".join(cj)
        return cj