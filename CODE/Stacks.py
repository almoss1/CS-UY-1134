class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self,item):
        self.data.append(item)
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]

s= ArrayStack()
s.push(12)
s.push(23)
s.data()