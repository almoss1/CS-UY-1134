class DoublyLinkedList:
    class Node:
        def __init__(self,data,prev=None, next = None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.header = DoublyLinkedList.Node(None)
        self.trailer = DoublyLinkedList.Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0 


    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is Empty")
        return self.header.next

    def last_node(self):
        return self.trailer.prev

    def add_after(self, node,data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data,prev, succ)
        # new_node.prev = prev
        # new_node.next = successor
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        
    def add_first(self,data):
        self.add_after(self.header,data)
    
    def add_last(self,data):
        self.add_after(self.trailer.prev, data)

    def add_before(self, node,data):
        self.add_after(self.node.prev,data)
    

    #link_lst.delete_nodes(some_node)==> delete_node(lnk_lst,some_node)
    def delete_node(self,node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev =prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())
    
    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.header
        while(curr_node is not self.trailer):
            yield curr_node.data
            curr_node = curr_node.next


    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) +']'


"""
lnk_list = DoublyLinkedList()
lnk_list.add_last(1)
lnk_list.add_last(2)
lnk_list.add_last(3)
lnk_list.add_last(4)
lnk_list.add_last(5)
lnk_list.add_first(0)
for elem in lnk_list:
    print(elem, end = "")
"""


        
        




    