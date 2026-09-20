class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        t=0
        a=list(set(nums))
        for i in a:
            if nums.count(i)==1:
                t+=i
        return t