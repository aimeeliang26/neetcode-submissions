class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pairs: temp, index

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]: #t > stack[-1][0] bc t is always one step ahead than stack 
                temp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex #i - stackIndex bc the future temp FROM CURRENT temp
            stack.append((t,i))
        return res
        # TC: O(n), n is the length of temperatures, while loop is always <= for so O(n)
        # SC: O(n)