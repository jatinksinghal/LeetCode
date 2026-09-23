class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(" ","")
        a=[]
        unenc=[]
        for i in key:
            if i not in a:
                a.append(i)
        # message=message.split()
        w=[]
        for i in message:
            if i!=" ":
                c=a.index(i)
                w.append(chr(97+c))
            # unenc.append("".join(w))
            else:
                w.append(" ")
        return "".join(w)