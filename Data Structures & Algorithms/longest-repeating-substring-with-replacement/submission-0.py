class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace up to k characters to make the longest substring that are 
        # all the same 

        # know the most freq char,
        # sliding window, condition of slide, 

        # aaababb
        #    p
        #      q
        # k -= 1
        res = 0
        charSet = set(s)
        # max(maxLen, q - p + 1)
        # i also dont get it 

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                # continue moving q pointer
                    count += 1
                while (r-l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1 #pointer 
                res = max(res, r - l + 1)
        return res
            
