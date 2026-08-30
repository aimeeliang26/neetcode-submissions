class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1-9, a-z, A-Z
        l,r = 0, len(s) -1
        #while loop the string, have a l pointer on the left, right pointer on the right end

        #start comparing, 
        while l < r:
        # if left is a none 1-9,a-z,A-Z element, left + 1, until it is a ele, so while 
        # if right is a none..., right -1, ...
            while l < r and not self.checkAlphaNu(s[l]):
        # if left ele == right ele, left + 1, right + 1; continue with the str as long as l < r 
                l += 1
            while l < r and not self.checkAlphaNu(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 
        # odd case 
        # even case will be the same since it's checking palindrome, aca is a palin, acca is also palin 
        #uppercase and lowercase 
    def checkAlphaNu(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))