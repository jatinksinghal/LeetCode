class Solution:
    def greatestLetter(self, s: str) -> str:
        a=sorted(set(s.lower()))
        f=""
        for i in a:
            if i in s and i.upper() in s:
                f=i.upper()
        return f
