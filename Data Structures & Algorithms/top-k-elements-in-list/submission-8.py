class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a dict to store the counts 
        # [1 1 1 2  3]
        count = {}
        freq = [[ ] for i in range(len(nums) + 1 )]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0) 
        
        for num, cnt in count.items():
            freq[cnt].append(num) # freq[3 freq] has a lisit of [apple, banana etc]
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            # res[i] = res.append[num] # res[0] = res.append[]
            #interate to the top k elements, -1 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        