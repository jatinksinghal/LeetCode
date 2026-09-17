class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        t=0
        for i in patterns:
            if i in word:
                t+=1
        return t