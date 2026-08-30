class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given an integer array nums, return an array output where 
        # output[i] is the product of all the ele of nums spart from nums[i]itself

        # nums = [1,2,4,6]
        # iterate every element in nums 

        # [2*4*6, 1*4*6, 1*2*4]

        # calculate the product of all non zeros
        n = len(nums)
        zeroCount = 0
        totalProduct = 1
        for element in nums:
            if element != 0:
                totalProduct = element * totalProduct
            if element == 0:
                zeroCount += 1  

        # calculate the number of zeros 

        # if number of zero is none 
        if zeroCount == 0:
        # iterate through nums, each nums[i] = totalproduct // nums[i]
            for i in range(n):
                nums[i] = totalProduct//nums[i]

        # if number of zero is 1:
        if zeroCount == 1:
            # iterate through nums, each nums[i] = 0
            for i in range(n):
                if nums[i] == 0:
                    nums[i] = totalProduct
                else:
                    nums[i] = 0

        if zeroCount > 1:
            for i in range(n):
                nums[i] = 0
        
        return nums

# learnings: if else statement make sure your logic is within bounds 

#       time complexity: O(n) where n is the number of elements in the array 
#       space complexity: n is the number of elements in the array, O(n) , and a fixed handful of variables such as count, O(1) total space complexity is O(n+1) = O(n)
        