class Solution:
    def isValid(self, s: str) -> bool:
        # open bracket first
        #stack 

        # if "(" "{" "["
        # if first open, we can always have open, or a corresponding closed 
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for element in s:
            if element in closeToOpen:
                if stack and stack[-1] == closeToOpen[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        return True if not stack else False

        
