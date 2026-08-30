class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find 3 ele in an array 
        # i,j,k cannot be the same, they are index, but return the ele, in any order, 
        # should not be duplicated (same 3 ele not allowed)
        # in no particular order, i am going to iterate it through all 
        # [-1,0,2,1] [-1,0,1,2,-1,-4]
        # [-1,0,1]    [-4,-1,-1,0,1,2]
        # [-1,0,1,2]
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i+ 1, len(nums) - 1
            while l < r:
                sums = a + nums[l] + nums[r]
                if sums > 0:
                    r -=1
                elif sums < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
        
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

        # i,j,k = 0, len(nums)-1, j = i + 1
        # sort 
        # if nums[i] + nums[j] +nums[k]
        # if nums[i] + nums[j] +nums[k]  == 0, 
        #      if res.contains([nums[i], nums[j], nums[k]])
        #         skip adding
        #     else 
        #         res.append([nums[i], nums[j], nums[k]])
    