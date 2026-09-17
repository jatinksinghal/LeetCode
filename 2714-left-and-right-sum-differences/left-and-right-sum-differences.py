class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        t=[]
        for i in range(len(nums)):
            a=sum(nums[i+1:])
            b=sum(nums[:i])
            t.append(abs(a-b))
        return t