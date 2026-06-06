class MinStack:

    def __init__(self):
        self.curr_min = None
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.curr_min:
            self.curr_min = val
        self.stack.append((val, self.curr_min))  
    def pop(self) -> None:
        output = None
        if self.stack:
            output = self.stack.pop()[0]
            if self.stack:
                self.curr_min = self.stack[-1][1]
            else:
                self.curr_min = None
        return output

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        print(self.stack[-1][1])
        return self.stack[-1][1]
