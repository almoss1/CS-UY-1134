from ArrayQueue import *

class LinkedQueue:
    def __init__(self):
        self.data = ArrayQueue.ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, elem):
        self.data.enqueue(elem)

    def dequeue(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        return self.data.dequeue()
    def first(self):
        if self.is_empty():
            raise Exception("LinkedQueue is empty")
        return self.data.first()