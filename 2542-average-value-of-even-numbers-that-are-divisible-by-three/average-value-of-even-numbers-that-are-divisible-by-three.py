class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i%2==0 and i%3==0:
                a.append(i)
        if len(a)==0:
            return 0
        else:

            return sum(a)//len(a)