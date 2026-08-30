class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height = [1,7,2,5,4,7,3,6]

        # loop through the list
        l,r = 0, len(heights) -1 # l = 1, r = 5
        maxVal = 0
        while l < r:
            h = min(heights[l], heights[r]) # h = 7
            w = r - l # w = 5 - 1 = 4
            output = h * w # output = 28
            if output > maxVal:
                maxVal = output # maxVal = 36
                # if heights[l] < heights[r]: # 
                #     l += 1 # l = 1
            elif heights[l] < heights[r]: # 
                l += 1 # l = 1
            else:
                r -= 1
        return maxVal

        
        