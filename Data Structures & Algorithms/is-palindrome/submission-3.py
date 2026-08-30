class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "tab a cat"

        l, r = 0, len(s) -1

        while l < r:
            while l < r and not self.checkAlphaNum(s[l]): # 0 < 8
                l += 1
            while l < r and not self.checkAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 

    def checkAlphaNum (self, c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or 
                ord('0') <= ord(c) <= ord('9') )
    