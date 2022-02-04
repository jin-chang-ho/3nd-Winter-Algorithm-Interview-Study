class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
        return None

    def pop(self) -> int:
        temp_queue = self.queue[:]
        
        if not temp_queue:
            return None
        
        while len(temp_queue) != 1:
            temp_queue.pop(0)
            
        self.queue = self.queue[:-1]
        
        return temp_queue[0]

    def top(self) -> int:
        temp_queue = self.queue[:]
        
        if not temp_queue:
            return None
        
        while len(temp_queue) != 1:
            temp_queue.pop(0)
        
        return temp_queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()