class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                a.append(0)
            else:
                a.append(1)
            
        return sorted(a)