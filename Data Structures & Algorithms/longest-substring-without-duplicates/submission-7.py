class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        res = set()
        # l, keep track of starting pointer
        # r, explore pointer
        # ""
        l = 0
        length = 0
        for r in range(len(s)):

            while s[r] in res:
                res.remove(s[l])
                l += 1            
            res.add(s[r])
            length = max(length, r - l + 1)       
        return length

        # TC:O ( n), n is the number of elements in s, removal is <= n. 
        # SC: O(m), where m is the unique number of consecutive elements