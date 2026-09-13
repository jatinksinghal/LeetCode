class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            a=nums[i]
            l=0
            t=0
            n=0
            while a>0:
                b=a%10
                a=a//10
                t+=1
                if b>l:
                    l=b
            for i in range(t):
                n=n*10+l
            count+=n
        return count
