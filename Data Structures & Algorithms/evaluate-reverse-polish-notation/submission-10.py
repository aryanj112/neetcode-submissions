class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            stack.append(t)
            if stack[-1] == '+':
                stack.pop()
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l + r)
            if stack[-1] == '-':
                stack.pop()
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l - r)
            if stack[-1] == '*':
                stack.pop()
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l * r)
            if stack[-1] == '/':
                stack.pop()
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(int(l / r))
        return int(stack[-1])

