class Solution:
    def smallestNumber(self, n: int) -> int:
        a=len(format(n,'b'))
        b="1"*a
        return int(b,2)