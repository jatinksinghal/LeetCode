class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1,s2=0,0
        for i in nums:
            if i>9:
                s2+=i
            else:
                s1+=i
        if s1>s2 or s2>s1:
            return True
        else:
            return False