class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0] #store min, starting off with nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                #sorted
                res = min(res, nums[l])
                break
            m = l+(r-l)//2
            res = min(res, nums[m])
            if nums[m]>=nums[l]:
                l = m + 1
            else:
                r= m - 1

        return res 

    # serveral understanding cleared: second half is always < first half bc of how rotation works 
    # intial nums[l] <nums[r] only happens if itself is a full ascending, no rotation happens