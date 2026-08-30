class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # reflection:
        # 1. think clearly of data structure, specifically what is maxheap, and why we use a heap?
        #     - maxheap, the highest on the top, you push ele off
        #     - minheap, the smallest on the top, you push ele off
        #         - whatever ele left in the minheap are the ele meets the criteria k > 3, if the smallest ele in the minheap alr meets this
        #         the rest of your minheap will meet this criteria 
            
        # nums = [1,2,2,3,3,3], k = 2

        # count = [[1,1], [2,2], [3,3]]
        # count [ key(ele), value(freq)]
        count = {} #dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # iterate the count put each pairs value to res and do it from the oppositive order
        heap = []
        res = []
        for num in count.keys():
            heapq.heappush(heap,(count[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        
        # maxheap[freq, key], --- the freq is bounded by the size of the input array 

        # give output
        #     -> iterate maxheap in reverse order, since we want top k 
        j = 0
        while j < k:
            res.append(heapq.heappop(heap)[1])
            j += 1

        return res
