class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=0
        for i in range(len(word)):
            if word[i]==ch:
                a=i
                break
        # print(a)
        return(word[a::-1]+word[a+1:])