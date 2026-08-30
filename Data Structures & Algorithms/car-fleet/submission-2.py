class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p, s in pair: 
            stack.append((target-p)/s) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
          #closest to target first
        return len(stack)

        # sort in decreasing order by pos # position: 4, 3, 2; speed: 1, 4, 7

        # push onto stack to store position, speed 
        # time = position/speed #if time for further from target cars takes <= to the closer car, they merge in one fleet
        # if time <= 
        # calculate the time it takes, with the closest to target first 
