class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None
    
    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            print("Queue is full")
    
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

test_queue = Queue(3)
print("Is the queue empty?", test_queue.is_empty())
test_queue.enqueue(10)
test_queue.enqueue(20)
print("Front element:", test_queue.front())
test_queue.enqueue(30)
print("Is the queue full?", test_queue.is_full())
test_queue.enqueue(40) # Full
print("Element dequeued:", test_queue.dequeue())
print("Element dequeued:", test_queue.dequeue())
print("Element dequeued:", test_queue.dequeue())
print("Element dequeued:", test_queue.dequeue())  # Empty
print("Is the queue empty?", test_queue.is_empty())
