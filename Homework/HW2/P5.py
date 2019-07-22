import Stacks
class Queue:

    def __init__(self):
        self.stack1 = Stacks.ArrayStack()
        self.stack2 = Stacks.ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.is_empty()

    def enqueue(self, val):
        while len(self.stack1) != 0:  
            self.stack2.push(self.stack1[-1])  
            self.stack1.pop() 
        self.stack1.push(val)  
        while len(self.stack2) != 0:  
            self.stack1.push(self.stack2[-1])  
            self.stack2.pop() 
        self.n += 1

    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                raise Exception("Stack is empty")
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        self.n -= 1
        return self.stack2.pop()

    def first(self):
        return self.stack2.top()



# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.first()