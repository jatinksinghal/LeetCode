class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=s+s
        if goal in a and len(s)==len(goal):
            return True
        else:
            return False