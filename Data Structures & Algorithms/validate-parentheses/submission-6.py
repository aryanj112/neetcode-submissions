class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if not stack:
                    return False
                check = stack.pop()
                if ( (c == ')' and check != '(') or (c == '}' and check != '{') or (c == ']' and check != '[') ):
                    return False
            else:
                return False     
        return True if not stack else False