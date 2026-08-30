class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #position
        #speed

        #if A's (target - position) / speed == B's xxxx -- they are the same car fleet 

        #otherwise, they are not

        # target = 10 , position = [4,1,0,7], speed=[2,2,1,1]
        # assuming set can only store non-repetitive items, i will add all nums in and just get the length of the array 

        totalCarFleet = 0 
        timeSet = set()
        maxTime = 0
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        for p, s in pair: #go through each car, calculate the time, store in an array
            # maxTime
            # totalCarFleet
            timeTaken = (target - p)/ s #12-3 / 3 = 3
            if maxTime < timeTaken:
                totalCarFleet += 1 #totalCarFleet = 2
                maxTime = timeTaken  #maxTime = 12
            else: #maxTime > timeTaken -- will become 1 fleet
                continue 
            # if timeTaken in timeSet:
            #     continue
            
            # timeSet.add(timeTaken) #timeSet = 1,1,12,7,3
        
        return totalCarFleet            

