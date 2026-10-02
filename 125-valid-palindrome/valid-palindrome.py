class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=""
        for i in range (len(s)):
            if s[i].lower()  in "abcdefghijklmnopqrstuvwxyz0123456789":
                f+=s[i].lower()
        return f==f[::-1]
        
