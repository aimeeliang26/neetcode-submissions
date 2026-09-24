class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openBracket, closeBracket):

            if openBracket == closeBracket == n:
                res.append("".join(stack))
                return
            
            if openBracket < n:
                stack.append("(")
                backtrack(openBracket + 1, closeBracket)
                stack.pop()
            if closeBracket < openBracket:
                stack.append(")")
                backtrack(openBracket, closeBracket + 1)
                stack.pop()
            
        backtrack(0,0)
        return res 
    #TC: O(2^2n)
    #SC: O(2n) ---> O(n)