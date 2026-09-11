class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a,b,c=nums[0],float("-inf"),float("-inf")
        nums=list(set(nums))
        if len(nums)>2:
            for i in nums:
                if i>a:
                    c=b
                    b=a
                    a=i
                elif i<a and i>b:
                    c=b
                    b=i
                elif i<a and i<b and i>c:
                    c=i
        else:
            c=max(nums)
        return c
        # a=[]
        # b=[]
        # for i in nums:
        #     if i in a:
        #         b.append(i)
        #     else:
        #         a.append(i)
        # return(a[len(a)-1])