class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=set(candyType)
        # for i in candyType:
        #     if i not in a:
        #         a.append(i)
        if len(a)>(len(candyType)//2):
            return len(candyType)//2
        else:
            return len(a)