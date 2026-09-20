class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=list(set(s))
        print(a)
        c=s.count(a[0])
        for i in a:
            if s.count(i)!=c:
                return False
                break
        return True