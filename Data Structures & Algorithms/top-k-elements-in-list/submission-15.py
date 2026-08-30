class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
    #  count each number 
        for ele in nums:
            count[ele] = 1 + count.get(ele, 0)
        #  count[element, frequency]

        #  count [1:1, 2:2, 3:3]

        #  store this in a minheap, because heappq is a min heap 
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        #  heap[frequency, element]
        #  heap[count[element], element]

        #  remove all the elements that is smaller than k
        if len(heap)> k:
            heapq.heappop(heap)

        #    return the 2 most frequent ones:
        
        res = []
        j = 0
        while j < k:
            res.append(heapq.heappop(heap)[1])
            j+=1
            
        return res