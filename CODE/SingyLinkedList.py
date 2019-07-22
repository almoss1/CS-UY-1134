class Node:
def __init__(self,data,next = None):
    self.data = data
    self.next = next


head = Node()
head.data = 1
head.next = Node()
head.mext.data =2
new_node = Node()
head.next.next = new_node
new_node.data = 3
curr_node = head
while(curr_node is not None):
    print(curr_node.data, end = " ")
    curr_node = curr_node.next