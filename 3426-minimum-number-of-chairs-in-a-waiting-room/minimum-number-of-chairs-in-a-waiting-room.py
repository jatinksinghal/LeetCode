class Solution:
    def minimumChairs(self, s: str) -> int:
        m=0
        a=0
        for i in s:
            if i=="E":
                a+=1
                if m<a:
                    m=a
            else:
                a-=1
        return m