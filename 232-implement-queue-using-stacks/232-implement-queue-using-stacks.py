class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp_stack = self.stack[:]
        
        if not temp_stack:
            return None
        
        while len(temp_stack) != 1:
            temp_stack.pop()
            
        self.stack = self.stack[1:]
        
        return temp_stack[0]

    def peek(self) -> int:
        temp_stack = self.stack[:]
        
        if not temp_stack:
            return None
        
        while len(temp_stack) != 1:
            temp_stack.pop()
        
        return temp_stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()