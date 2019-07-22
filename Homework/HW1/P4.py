import ctypes

def make_array(n):
    return (n * ctypes.py_object)()
    #creating an array that can store n python objects
    #space in memory that can store items
    #can storemultiple objects of the same size

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


### NEW CODE
    def __repr__(self):
        return str(self.data[:self.n])


    def __add__(self,other):
        combined = MyList()
        combined.extend(self)
        combined.extend(other)
        return combined
            

    def __mul__(self,n):
        new_lst = MyList()
        for i in range(n):
            new_lst.extend(self)
        return new_lst

    def __rmul__(self, n):
        return self * n





#class implementation

def __repr__(self):
    result_str = "["

    for elem in self:
        result_str+= str(elem) + ","
    if len(self) > 0:
        result_str = result_str[:-2]
    result_str+= "]"
    return result_str

my_list1 = MyList()
my_list1.append(1)
my_list1.append(2)
print(my_list1)

def __add__(self,other):
    #If self has length n1 and other has length n2. should run in O(n1+ n2)
    n1= len(self)
    n2 = len(other)
    result = MyList()
    result.resize(n1+n2)
    for i in range(n1):
        result[i] =self[i]
    for i in range(n2):
        result[n1+i] = other[i]
    return result 

# or you could do it the easier way and do it this way
    result.extend(self) #O(n1)
    result.extend(other) #O(n2)
    return result



def __mul__(self,n):
    #If self has len(m) should run in time O(n*m)
    result = MyList()
    for i in range(n):
        result.extend(self)
    return result 

def __rmul__(self,n):
    return self * n

def __iadd__(self, other):
    self.extend(other)

my_list2 = MyList()
my_list2.append(3)
my_list2.append(4)
my_list2.append(5)
my_list2.append(6)
print(my_list2)
my_list3 = my_list1 + my_list2
print(my_list3)

my_list4 = my_list1 * 4
print(my_list4)


my_list4 = 4 * my_list1
print(my_list4)

my_list5 = MyList()
my_list5.append(8)
my_list1 += my_list5  #running time: O(len(my_lst5))
print(my_list1)