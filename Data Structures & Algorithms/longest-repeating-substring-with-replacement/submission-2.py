class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # you can perform K replacement, to get the longest string with one type of letter 
        # left, right 
        # move right pointer one by one, if r is diff to l pointer, 
        # life = 0, life ++ 
        # As long as life < = k
        # else 
        #     move left pointer one by one, 

        #     AAABABB k = 1
        #        l
        #           r
        #     len 4
        #     maxLen 5
        #     life 1
        # replacement needed = window length - count of most common char
        l = 0 
        maxLen = 0
        maxFreq = 0
        count = defaultdict(str)
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count.get(s[r]))

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -=  1
                l += 1

            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
        # TC: O(n), n is the num of elements in s 
        # SC: O(m), m is the largest window      
 