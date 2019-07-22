import Stacks
class MaxStack:
    def __init__(self):
        self.data = Stacks.ArrayStack()
        self.max_val = None
        self.num_of_elem = 0
    
    def __len__(self):
        return self.num_of_elem
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self,elem):
        if self.max_val == None:
            self.max_val = elem
        if elem <= self.max_val:
            self.data.push((elem, self.max_val))
        else:
            self.max_val = elem
            self.data.push((elem, self.max_val))
        self.num_of_elem +=1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data[-1]


    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            num = self.data.pop()
            if not self.data.is_empty():
                num2 = self.data.top()
                if num[0] == self.max_val:
                    self.max_val = num2[1]
        self.num_of_elem -= 1
        return num[0]

    def max(self):
        if self.is_empty():
            raise Exception("It is empty")
        return self.max_val
    

# max_s = MaxStack() 
# max_s.push(3)
# max_s.push(1)
# max_s.push(6)
# max_s.push(4) 
# print(max_s.max())
# print(max_s.pop())
# print(max_s.pop())
# print(max_s.max())



