class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<10:
                    nums[i]=nums[i+1]+nums[i]
                else:
                    nums[i]=(nums[i+1]+nums[i])%10
                if i+1==len(nums)-1:
                    nums.pop(len(nums)-1)
        return sum(nums)