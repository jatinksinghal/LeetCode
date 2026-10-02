class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=s[::-1] 
        w=""
        for i in range(len(s)):
            w+=s[i]
            if i!=len(s)-1:
                w+=" "
        return w