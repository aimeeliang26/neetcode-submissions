class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = [] 

        # open (, close ); close should never be greater than open
            # 
        # if open is greater than close, its alright. as longas it's < n 
        # 
        def backtrack(openBrac, closedBrac):
            if closedBrac == openBrac == n:
                res.append("".join(stack))
                return 
            if openBrac < n:
                stack.append("(")
                backtrack(openBrac + 1, closedBrac)
                stack.pop()
            if closedBrac < openBrac:
                stack.append(")")
                backtrack(openBrac, closedBrac + 1)
                stack.pop()
        backtrack(0,0)
        return res