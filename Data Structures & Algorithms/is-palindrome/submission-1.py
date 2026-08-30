class Solution:
    def isPalindrome(self, s: str) -> bool:
        # aca, ac,a
        # start with l, r pointer, l = 0,  r = len(s)-1
        l, r = 0, len(s) - 1 # r = 8
        # start loop -- while l < r:
        while l < r: # 
            while l < r and not self.checkAlphaNume(s[l]): # 
                l += 1
            while r > l and not self.checkAlphaNume(s[r]):
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
            
                   
            
        # in the case where s[l] and s[r] are alphanumeric
        #     check that by having a function to check whether s[l] and s[r] fall 
        #     under the range of 'a' to 'z', 'A' to 'Z', '0' to '9'
        
        #     compare s[l] and s[r]
        #     if s[l] == s[r]
        #         continue 
        #     else
        #         return false 
        # else 
        #     return False
    
    def checkAlphaNume(self, c) -> bool:

        # return True if it falls under that range, else return False
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')
   
