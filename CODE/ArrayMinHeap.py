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
        return 2*i + 1

    def right_idx(Self,i):
        return 2*i + 2

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


    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        if not self.is_empty():
            self.sift_down(0)
        return item

       
    def sift_down(self,i):
        if not self.has_left(i):
            return
        left_idx = self.left_ind(i)
        min_child_idx = left_idx
        if self.has_right(i):
            right_idx = self.right_idx(i)
            if self.data[right_idx] < self.data[min_child_idx]:
                min_child_idx = right_idx
        
        if self.data[min_child_idx] > self.data[i]:
            self.swap(min_child_idx, i)
            self.sift_down(min_child_idx)


# merge sort runtime is theta(nlog(n))
#runtime is theta(nlog(n))
def heap_sort(lst):
    heap = ArrayMinHeap()
    for elem in lst:
        heap.insert(elem)
    srt_lst = []
    while not heap.is_empty():
        item = heap.delete_min()
        srt_lst.append(item.priority)
    return srt_lst

srt_lst = heap_sort([5])
print(srt_lst)