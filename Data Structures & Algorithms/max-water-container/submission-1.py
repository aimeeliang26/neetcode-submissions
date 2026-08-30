class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # iterate through every ele, compare 
        # [1,7,2,5,4,7,3,6]
        # l               r
        l, r = 0, len(heights) - 1
        maxRes = 0
        while l < r:
            h = min(heights[l], heights[r])
            w =  r - l
            output = h*w 
        
            if maxRes < output:
                maxRes = output
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxRes

        
