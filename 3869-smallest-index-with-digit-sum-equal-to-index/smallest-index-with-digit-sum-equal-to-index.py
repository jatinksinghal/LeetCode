class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=0
            while nums[i]>0:
                b=nums[i]%10
                nums[i]=nums[i]//10
                a+=b
            if a==i:
                return i
                break
        else:
            return -1
