class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        for i in arr:
            if i not in target or target.count(i)!=arr.count(i):
                return False
        return True