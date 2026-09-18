class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m=10**10
        for i in tasks:
            if sum(i)<m:
                m=sum(i)
        return m