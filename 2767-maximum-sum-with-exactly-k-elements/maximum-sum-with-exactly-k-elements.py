class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        t=0
        for i in range(k):
            t+=max(nums)+i
        return t