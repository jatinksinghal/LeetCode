class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        a=len(nums[0])
        for i in range(0,2**a):
            b=format(i,f"0{a}b")
            if b not in nums:
                return b
                break
        return ""