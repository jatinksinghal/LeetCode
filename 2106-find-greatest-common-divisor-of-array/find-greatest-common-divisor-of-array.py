class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        for i in range(b,1,-1):
            if a%i==0 and b%i==0:
                return i
                break
        else:
            return 1