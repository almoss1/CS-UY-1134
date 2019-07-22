#1 Double Ended Queue
import Stacks

class ArrayDeque:
    initial_capacity = 8
    def __init__(self):
        self.data = [None] * ArrayDeque.initial_capacity
        self.number_of_elems = 0
        self.front_ind = 0
        
    def data1(self):
        return self.data

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        back_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        return self.data[back_ind]

    def enque_first(self,elem):
        if self.is_empty():
            self.data[0] = elem
            self.number_of_elems += 1
            self.front_ind = 0
        else:
            self.data[self.front_ind + 1] = self.data[self.front_ind] 
            self.data[self.front_ind] = elem
            self.number_of_elems += 1
            self.front_ind = 0

    def enque_last(self,elem):
        if self.is_empty():
            self.data[0] = elem
            self.number_of_elems += 1
            self.front_ind = 0
        else:
            back_ind = (self.front_ind + self.number_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.number_of_elems += 1
            
    def deque_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        return elem


    def deque_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.data[back_ind] = None
        back_ind = self.data[back_ind -1] % len(self.data)
        self.number_of_elems -= 1


#2 Balanced Parenthesis
def balanced_expressions(string_input):
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for token in string_input:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty():
                return False
            from_S =  S.top()
            if righty.index(token) == lefty.index(from_S):
                S.pop()
            else:
                return False
        else:
            raise ValueError
    return S.is_empty()


#Balancing HTML tags

def get_tag(text):
    i = 0
    n = len(text)

    while i < n:
        while i < n and text[i] != "<":
            i += 1
        i+=1
        start = i
        while i < n and text[i] != ">":
            i =+ 1
        end = i
        if start < end:
            yield text[start:end]

def is_matched_html(expr):
    stack = ArrayStack()
    for tag in get_tag(expr):
        if tag[0] == "/":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != tag[1:]:
                return False
        else:
            stack.push(tag)
    return stack.is_empty()