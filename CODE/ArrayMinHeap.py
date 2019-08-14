class ArrayMinHeap:
    class Item :
        def __init__(self,priority, value = None):
            self.priority = priority
            self.value = value
        
            #allows for the syntax item1 <item2
        def __lt__(self,other):
            return self.priority < other.priority
    

    #end of Item class

    def __init__(self):
        self.data = []
        
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def left_idx(self,i):
        return 2*i +1

    def right_idx(Self,i):
        return 2*i +2

    def parent_idx(self,i):
        return (i-1) // 2

    def has_left(self, i):
        return self.left_idx(i) < len(self.data)

    def has_right(self,i):
        return self.right_idx(i) < len(self.data)

    def min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return self.data[0]

    def insert(self, priority, value = None):
        self.data.append(ArrayMinHeap.Item(priority,value))
        self.buble_up(len(self.data-1))

    def buble_up(self,i):
        if i ==0:
            return
        else:
            parent = self.parent_idx(i)
            if self.data[i] <self.data[parent]:
                self.swap(i, parent)
                self.buble_up(parent)

        """
        #iterative way
        while i > 0:
            parent = self.parent_idx(i)
            if self.data[i] <self.data[parent]:
                self.swap(i, parent)
                i = parent
            else:
                return
        """
            
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
