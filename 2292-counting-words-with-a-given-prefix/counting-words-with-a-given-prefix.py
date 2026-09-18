class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        c=0
        for i in words:
            if pref==i[:len(pref)]:
                c+=1
        return c