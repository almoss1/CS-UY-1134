import Stacks
from DoublyLinkedList import *
from ArrayQueue import *

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.num_elements = 0

    def __len__(self):
        return self.num_elements
    
    def is_empty(self):
        return len(self.data) == 0

    def push(self, elem):
        self.data.add_after(elem)
        self.num_elements += 1

    def pop(self):
        if self.data.is_empty():
            raise Exception("LinkedStack is empty")
        else:
            self.data.delete_last()
            self.num_elements -= 1
            
    def top(self):
        if self.data.is_empty():
            raise Exception("LinkedStack is empty")
        else:
            self.data.last_node()



# 2 LeakyStack


class LeakyStack:
    def __init__(self, max_num_of_elems):
        self.DLL = DoublyLinkedList()
        self.max_num_of_elems = max_num_of_elems

    def __len__(self):
        return len(self.DLL)

    def is_empty(self):
        return len(self.DLL) == 0

    def push(self, elem):
        if len(self.DLL) == self.max_num_of_elems:
            self.DLL.delete_first()
            self.DLL.add_last(elem)
            self.max_num_of_elems+=1
        else:
            self.DLL.add_last(elem)
            self.max_num_of_elems += 1

    def pop(self):
        if self.is_empty():
            raise Empty('LeakyStack is empty')
        else:
            return self.DLL.delete_last()
            self.max_num_of_elems -= 1

    def top(self):
        if self.is_empty():
            raise Empty('LeakyStack is empty')
        else:
            return self.DLL.last_node()


# 3 QStack

class QStack:
    def __init__(self, max_num_of_elems):
        '''Initialize an empty leaky stack'''
        self.data_queue = ArrayQueue()
        self.max_num_of_elems = max_num_of_elems

    def __len__(self):
        return len(self.data_queue)

    def is_empty(self):
        return len(self.data_queue) == 0

#O(n) runtime
    def push(self, elem):
        self.data_queue.enqueue(elem)
        for i in range(self.max_num_of_elems):
            self.enqueue(self.data_queue.first())
            self.data_queue.dequeue()
        self.max_num_of_elems +=1

    # O(1) runtime
    def pop(self):
        if self.data_queue.is_empty():
          raise Exception("QStack is empty")
        else:
            return self.data_queue.dequeue()
            self.max_num_of_elems -= 1

    def top(self):
        if self.data_queue.is_empty():
           return self.data_queue[-1]
        else:
            self.data_queue.first()


