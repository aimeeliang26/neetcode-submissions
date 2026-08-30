class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # "pwwkew"
        # pointer 
        q = 0
        maxLen = 0

        for p in range(len(s)): # 2
            while s[p] in seen: # w in seen?
                seen.remove(s[q]) #
                q += 1 # q = 1
            seen.add(s[p]) # seen = pw
            maxLen = max(maxLen, p - q + 1) # maxLen= 2
        return maxLen