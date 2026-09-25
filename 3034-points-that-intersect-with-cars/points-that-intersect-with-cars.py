class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        a=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                a.append(j)
        return len(set(a))