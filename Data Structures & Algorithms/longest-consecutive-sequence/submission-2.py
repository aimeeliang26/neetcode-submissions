class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
#         return the length of the longest consecutive sequence of elements that can be formed 

#         two pointers 
#         length variable 

#         1 2 3 4 

#         5 6 7 8
#         8-5 = 3 == j - i 

#         [2,5,6,7,8,0,1,2,3,5]
#         [2,3]
# i 
#   j
        if not nums:
            return 0
        nums = sorted(set(nums))

        length = 1
        i, j = 0,1
        while j < len(nums):
            if nums[j] - nums[i] == j-i:
                j += 1
                if j-i > length:
                    length = j-i
            else:
                i = j 
                j += 1

        return length 
   
