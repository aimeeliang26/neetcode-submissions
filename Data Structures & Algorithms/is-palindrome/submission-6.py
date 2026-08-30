class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "tab a cat"
        l, r = 0, len(s) -1
        while l < r:
            while l < r and not self.checkIfAlpha(s[l]):
                l += 1
                continue
            while l < r and not self.checkIfAlpha(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def checkIfAlpha(self, s):
        
        return (ord('a') <= ord(s) <= ord('z') or
                ord("A") <= ord(s) <= ord("Z") or
                ord('0') <= ord(s) <= ord('9'))