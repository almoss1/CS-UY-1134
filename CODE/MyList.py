import ctypes

def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        # Initialize an empty array
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        # append: O(1) amortized 
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_capacity):
        # resize: O(n), where n is number of elements in list
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, ind):
        # Runinng time O(1)
        if not (0 <= ind <= self.n-1):
            raise IndexError(str(ind) + " is out of range")
        return self.data[ind]

    def __setitem__(self, ind, value):
        # Running time O(1)
        if not (0 <= ind <= self.n-1):
            raise IndexError(str(ind) + " is out of range")
        self.data[ind] = value

    def extend(self, other):
        # extend: O(k) amortized, where k is number of elements in other
        for elem in other:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

            
    def pop(self):
        # O(1) amortized
        if self.n == 0:
            raise IndexError("Can't pop () from an empty list")
        if self.n == self.capacity // 4:
            self.resize(self.capacity//2)

        val = self.data[self.n -1]
        self.n -= 1
        return val
