class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(" ","")
        a=[]
        for i in key:
            if i not in a:
                a.append(i)
        w=""
        for i in message:
            if i!=" ":
                c=a.index(i)
                w+=(chr(97+c))
            else:
                w+=" "
        return w