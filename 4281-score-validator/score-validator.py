class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        t,w=0,0
        for i in events:
            if i in "1234567890":
                t+=int(i)
            elif i=="WD" or i=="NB":
                t+=1
            elif i=="W":
                w+=1
            if w==10:
                return [t,w]
                break
        return [t,w]