class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        b=[]
        for i in range(len(words)):
            w=[]
            for j in range(len(words[i])):
                k=ord(words[i][j])
                print(k-96)
                w.append(a[k-1-96])
            w="".join(w)
            print(w)
            b.append(w)
        return len(set(b))