class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j,maxval = 0,len(heights) - 1, 0
        while i < j:
            curval = (j-i) * min(heights[i], heights[j])
            if curval > maxval:
                maxval = curval
            if heights[i] < heights[j]:
                i +=1
            else:
                j-=1
        return maxval
