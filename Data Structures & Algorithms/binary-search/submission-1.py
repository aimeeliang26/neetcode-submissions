class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # iterative method 
        
        # define l, r
        l, r = 0, len(nums) - 1

        # iterate nums [1,2,3] target = 2
        #             [1, 2] target = 2
        #             [1] target = 1
        while l <= r:
            # define middle 
            m = (l + (r-l)//2)
            if nums[m] < target:
                # go to left half 
                l = m + 1
            elif nums[m] > target:
                # go to right half 
                r = m - 1
            else:
                return m
         # did not find it 
        return -1 

