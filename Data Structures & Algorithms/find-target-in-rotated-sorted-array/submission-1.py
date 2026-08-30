class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2] target = 1
        # l, r = 0, len(nums) - 1
        # finding the min (pivot) is important to performn Binary search on the two sorted array 

        # for i in nums: # 3, 4, 5,6,1,2
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            # not in ascending order, look for pivot       
            if nums[m] > nums[r]:
                #min is in right space
                l = m + 1
            else: 
                r = m 
        pivot = l

        def binarySearch(left:int, right:int)-> int:
            while left <= right:
                mid = left + (right - left) //2
                if nums[mid] < target:
                    #search in right 
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    return mid
            return -1

        result = binarySearch(0, pivot - 1) 
        if result != -1:
            return  result
        
        return binarySearch(pivot, len(nums)-1)
    
    # TC: O(logn), n is the number of elements in nums
    # SC: result, O(1)


