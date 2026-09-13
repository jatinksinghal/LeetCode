class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1,s2=[],[]
        for i in nums:
            if i>9:
                s2.append(i)
            else:
                s1.append(i)
        if sum(s1)>sum(s2) or sum(s2)>sum(s1):
            return True
        else:
            return False