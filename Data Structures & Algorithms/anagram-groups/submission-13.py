class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ["act", "pots", "cat"]

        # if length of the strs is less than 2
        #     return [strs]
        if len(strs) < 2:
            return [strs]
        
        # count = 26 * [0] initialize a list with 0s 
        res = defaultdict(list)
        # iterate through each s in strs 
        for s in strs: #act 
            count = 26 * [0]
        # put the diff = ord(c) - ord('a') in the count
        #     count[diff] + 1
            for c in s: #a
                count[ord(c) - ord('a')] = count[ord(c) - ord('a')] + 1
        # hashmap count, value is append s (the string, not char)
            res[tuple(count)].append(s)
        # return hashmap.values
        return list(res.values())