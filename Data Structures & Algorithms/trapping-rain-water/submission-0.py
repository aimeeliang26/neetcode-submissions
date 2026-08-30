class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointers 
        if not height: return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[len(height)-1]
        res = 0

        # while two pointers dont overlap, l < r
        # what is the curr input, 
        # if currinput > maxL 
        # maxL = curr input
        # if input < maxL, res = maxL-input + res

        while l < r:
            if maxL < maxR:
                if maxL > height[l]:
                    res += maxL - height[l]
                #move maxL pointer
                l += 1
                maxL = max(maxL, height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res


        # input 0 1 0 2 1 0 1 3 2 1 2 1
        # maxL  0 0 1 1 2 2 2 2 3 
        # maxR  1 1  
        # res   0 0 1 0 1 2 1 0   
        # res = maxL - input , input < maxL
        # shifting the pointer that has min height 