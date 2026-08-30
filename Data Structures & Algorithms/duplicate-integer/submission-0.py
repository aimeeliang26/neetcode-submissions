class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        

        # you can have a hashtable to store 
        # binary search tree 
        # time O(n) means within the bounds of the number of total elements
        # Space O(n) within the bounds of # of total elements

        # hashtable because the most we iterate is n. max space is the amount of n 


