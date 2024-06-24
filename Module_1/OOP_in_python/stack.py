class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None


test_stack = Stack(3)
print("Is the stack empty?", test_stack.is_empty())
test_stack.push(10)
test_stack.push(20)
print("Top element:", test_stack.top())
test_stack.push(30)
print("Is the stack full?", test_stack.is_full())
test_stack.push(40)  # Full
print("Element popped:", test_stack.pop())
print("Element popped:", test_stack.pop())
print("Element popped:", test_stack.pop())
print("Element popped:", test_stack.pop())  # Empty
print("Is the stack empty?", test_stack.is_empty())
