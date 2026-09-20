class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        a=sorted(nums)
        for i in range(len(nums)//2):
            p=a[2*i:2*i+2]
            if p[0]!=p[1]:
                return False
        return True