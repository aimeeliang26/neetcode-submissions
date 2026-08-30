class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,5] h = 2
        # if n < len(piles), return False 

        # 10 bananas, try with 5 -- if that meets the hours, try 3
        # (binary search approach)

        l, r = 1, max(piles) #search space of eatSpeed, not index; 1, 5; this is the tighest l, r 
        eatSpeed = h #anything that is pretty high in eating speed 
        while l <= r:
            totalTime = 0
            k = l + (r-l) // 2
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                eatSpeed = k
                #search in the left space
                r = k - 1
            else:
                l = k + 1
        return eatSpeed
            

