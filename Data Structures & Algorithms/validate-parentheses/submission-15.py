class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                print("top", top, "char", c)
                if not((top == '(' and c == ')') or 
                (top == '[' and c == ']') or 
                (top == '{' and c == '}')):
                    return False
            print(stack)

        return False if stack else True
