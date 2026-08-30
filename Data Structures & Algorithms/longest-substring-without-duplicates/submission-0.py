class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the longest without duplicate 
        # have a hashset to store the letters 

        # zxyzyxa 
        #     q
        #   p
        # count = 0, q = 0
        # hashset = zy
        seen = set()
        p = 0
        maxLen = 0
        for q in range(len(s)):           
            while s[q] in seen:
                seen.remove(s[p])
                p +=1
            
            seen.add(s[q])
            maxLen = max(maxLen, q - p + 1)
        # maxLen = 3
        # count = 2
        return maxLen
