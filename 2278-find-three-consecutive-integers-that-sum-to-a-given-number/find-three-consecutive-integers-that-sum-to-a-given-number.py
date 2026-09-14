class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a=(num-3)
        if a%3==0:
            return [a//3,a//3 +1, a//3 +2]
        else:
            return[]