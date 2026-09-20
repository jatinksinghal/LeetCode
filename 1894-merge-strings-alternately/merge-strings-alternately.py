class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        for i in range(len(word2)):
            word1.insert(2*i+1,word2[i])
        return "".join(word1)