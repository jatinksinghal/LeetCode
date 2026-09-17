class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,r,p=[],[],[]
        for i in nums:
            if i <pivot:
                l.append(i)
            elif i==pivot:
                p.append(i)
            else:
                r.append(i)
        return(l+p+r)