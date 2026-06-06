class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.cap = 0
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if self.cap == self.size:
            self.total -= self.queue.popleft()
            self.cap -= 1
        self.cap += 1
        self.total += val
        self.queue.append(val)
        return self.total/self.cap


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
