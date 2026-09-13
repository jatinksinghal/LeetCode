class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            b=0
            c=nums[i]
            while c>0:
                a=c%10
                c=c//10
                b=b*10 + a
            nums.append(b)
        return len(set(nums))