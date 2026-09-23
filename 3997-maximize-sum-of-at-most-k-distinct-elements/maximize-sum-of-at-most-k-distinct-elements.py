class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        a=sorted(list(set(nums)))
        a=a[::-1]
        return(a[:k])