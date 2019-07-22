class ArrayQueue:
    initial_capacity = 8
    def __init__(self):
        self.data = [None] * ArrayQueue.initial_capacity
        self.number_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return len(self) == 0

    def enqueue(self,item):
        if (self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.data[0] = item
            self.front_ind = 0
            self.number_of_elems = 1
        else:
            back_ind = (self.front_ind + self.number_of_elems) % len(self.data)
            self.data[back_ind] =item
            self.number_of_elems += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None 
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize((len(self.data) // 2))
        return val


    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    

    def resize(self,new_cap):
        old_data = self.data
        self.data =[None] * new_cap
        old_ind =  self.front_ind
        for new_ind in range(self.number_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
    