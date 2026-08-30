class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [nums[i], nums[j], nums[k]]
        # nums[i] + nums[j] + nums[k] == 0
        # use a while loop as the third pointer
        # [-4,-1,-1,0,1,2]
        # a = -4 
        #     l
        # if l == i, l ++ 
        # -4 -1 2 
        # -4 0 2 
        # -4 1 2
        # a = -1 ,i == 1
        # -4 -1 2
        # 0 -1 2
        # 0 -1 1 --> res

        # a = -1

        # a = 0, i == 3
        # -4 0 2
        # -1 0 2
        # -1 0 1 --> res

        # a = 1, i==4


        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i-1] == a: #dedup a
                continue 
            l, r = i+1, len(nums) - 1
            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -=1 
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else: #== 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
            
        
# TC: O(n^2) with n is the # of elements in nums 
# SC: O(m) - m is the number of unique triplets if output space is included. else it is O(1) plus the sorting algorithm used space 
