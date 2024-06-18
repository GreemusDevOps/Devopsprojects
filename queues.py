class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Current queue:", queue.queue)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Current queue after dequeue:", queue.queue)