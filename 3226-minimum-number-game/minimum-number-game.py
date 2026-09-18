class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        a=nums[::2]
        b=nums[1::2]
        for i in range(len(a)):
            b.insert(2*i + 1,a[i])
        return b
            

