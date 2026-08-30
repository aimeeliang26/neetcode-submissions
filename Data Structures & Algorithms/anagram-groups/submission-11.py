class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        res = defaultdict(list)

        if len(strs) < 2:
            return [strs]
        
        # naive solution: go through each ele in strs, 
        for s in strs:
            count = [0] * 26 # count = [0],[0], [0]
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        return list(res.values())

