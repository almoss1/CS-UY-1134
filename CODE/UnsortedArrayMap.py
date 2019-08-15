class UnsortedArrayMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value
    
    def __init__(self):
        self.table = []

    
    def __len__(self):
        return len(self.table)
    
    def is_empty(self):
        return len(self) ==0

    #m[key] ==> m.__getitem__(key) ==> __getitem__(m,key)
    def __getitem__(self,key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError(str(key) + "is not in the map")

    #m[key] = value ==> m.__setitem__(key,value)
    def __setitem__(self,key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        #if we get here, the key is not in the map
        self.table.append(UnsortedArrayMap.Item(key,value))

    #del m[key] ==> m.__Delitem__(self,key)
    def __delitem__(self,key):
        for idx in range(len(self.table)):
            if key == self.table[idx].key:
                #could do one or the other, a little better runtime
                self.table.pop(idx)
                # self.table[idx], self.table[-1] = self.table[-1], self.table[idx]
                # self.table.pop()
                return
        #if we get here, then key is not in the map
        raise KeyError(str(key) + "is not in the map")

    def __iter__(self):
        for item in self.table:
            yield item.key


m = UnsortedArrayMap()
m["one"] = 1
m["two"] = 2
m["three"] = 3
m["four"] = 4
m["five"] = 5
val1 = "one"
val2 = "three"

#want t compute "one" + "three" ==> 4

result = m[val1] +m[val2]
print(result)
m["five"] = "0b101"
print(m["five"])
for key in m:
    print(key, m[key])


