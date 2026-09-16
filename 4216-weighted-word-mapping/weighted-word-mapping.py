class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        w=[]
        for i in words:
            t=0
            for j in i:
                a=ord(j)-97
                t+=weights[a]
            print(t)
            b=t%26
            w.append(chr(96+26-b))
        return "".join(w)