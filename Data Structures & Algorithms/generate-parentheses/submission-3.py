class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paren if the open < n
        # only add closing if close < open
        # valid if open == close == n
        res = []
        stack = []

        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backTrack(openN , closeN + 1)
                stack.pop()
        
        backTrack(0,0)
        return res

