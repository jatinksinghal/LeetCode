class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return i
                break