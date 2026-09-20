class Solution:
    def stringSequence(self, target: str) -> List[str]:
        f=[]
        for i in range(len(target)):
            for j in range(97,ord(target[i])+1):
                w1=list(target[:i])
                w1.append(chr(j))
                w1="".join(w1)
                f.append(w1)
        return f