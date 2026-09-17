class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        w=[]
        for i in range(len(s)):
            a=indices.index(i)
            w.append(s[a])
        return "".join(w)