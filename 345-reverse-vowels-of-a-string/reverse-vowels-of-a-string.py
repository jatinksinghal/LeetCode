class Solution:
    def reverseVowels(self, s: str) -> str:
        a=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                a.append(i)
        for i in range(len(a)//2):
            temp=s[a[i]]
            s[a[i]]=s[a[len(a)-1-i]]
            s[a[len(a)-1-i]]=temp

        return "".join(s)
