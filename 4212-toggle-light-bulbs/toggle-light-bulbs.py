class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        h,f={},[]
        for i in bulbs:
            h[i]=h.get(i,0)+1
        for i in h:
            if h[i]%2!=0:
                f.append(i)
        return sorted(f)