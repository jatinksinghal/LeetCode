class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        f,h=[],[]
        for i in range( len(s)):
            if s[i]=="#" and len(f)!=0:
                f.pop()
            elif s[i]=="#":
                continue
            else:
                f.append(s[i])
        for i in range(len(t)):
            if t[i]=="#"and len(h)!=0:
                h.pop()
            elif t[i]=="#":
                continue
            else:
                h.append(t[i])
        print(f,h)
        f="".join(f)
        h="".join(h)
        if f==h:
            return True
        else:
            return False
      
        