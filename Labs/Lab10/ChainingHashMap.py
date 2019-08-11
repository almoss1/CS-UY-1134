from DoublyLinkedList import DoublyLinkedList
import random
class ChainingHashMap:
    def __init__(self, N=64, p=40206835204840513073):
        self.table_size = N
        self.number_of_items = 0
        self.table =[DoublyLinkedList() for i in range(self.N)]
        self.p = p
        self.a = random.randrange(1, self.p -1)
        self.b = random.randrange(0, self.p -1)

    def hash_function(self, key):
        return ((self.a * hash(key) +self.b) % self.p) % self.table_size
        
    def __len__(self):
        return self.number_of_items

    def is_empty(self):
        return (len(self) == 0)
    
    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.number_of_items += 1
        if self.number_of_items > self.table_size:
            self.rehash(2 * self.table_size)

    def __delitem__(self,key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.number_of_items -= 1
        if self.number_of_items < self.table_size // 4:
            self.rehash(self.table_size // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key
    
    def rehash(self, new_size):
        old = [(key,self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val
            

myMap= ChainingHashMap(128)





ht =ChainingHashTableMap()
for i in range(100):
    ht[i * i] = i

for i in range(ht.N):
   # print(i , ":" ,sep=" ", end=" ")
    curr_bucket =ht.table[i]
    for key in curr_bucket:
        print("(",key, "," , curr_bucket[key], ")", sep="", end="" )

for i in range(80):
    del ht[i * i]


for i in range(ht.N):
    print(i , ":" ,sep=" ", end=" ")
    curr_bucket =ht.table[i]
    for key in curr_bucket:
        print("(", key, "," , curr_bucket[key], ")", sep="", end="" )