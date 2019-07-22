class BinarySearchTreeMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item, left = None, right = None):
            self.item = item
            self.parent = None
            self.left = left
            self.right= right

            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent =self

        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if sel.right is not None:
                count += 1

        def disconnect(Self):
            self.parent = None
            self.right = None
            self.left = None
        

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return len(self) == 0

    #overloading bracket operator to allow for syntax: m[key] 
    def __getitem__(self,key):
        node =self.find(key)
        if node is None:
            raise KeyError(str(key) + "is not found")
        else:
            return node.item.value
    
    #return the node whose item has key 'key' or (None)
    def find(self,key):
        pass
    
    def __setitem__(self,key,value):
        node = self.find(key)
        if node is not None:
            node.item.value = value
        else:
            self.insert(key,value)






    def sum_nodes(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if self.subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)
        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self. subtree_height(self.root)

    def subtree_height(Self, subtree_root):
        if self.subtree_root.left is None and self.subtree_root.righ is None:
            return 0
        elif subtree_root.left is None:
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right
            return 1 + max(left_height, right_height)
        
        
    def preorder(self):
        yield from self.subtree_preorder(self,subtree_root)
    
    #yields all values in the nodes of the subtree rooted at "subtree_root"
    def subtree_preorder(self,subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)
    
    

    def inorder(self):
        yield from self.subtree_inorder(self.subtree_root)

    def subtree_inorder(self,subtree_root):
        if subtree_root is None:
            return

        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)



    def postorder(self):
        yield from self.subtree_postorder(self.subtree_root)

    def subtree_postorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root

    

#"Level Order Traversal"
    def breadth_first(self):
        if self.is_empty():
            return
        nodes_q =  ArrayQueue.ArrayQueue()
        nodes_q.enqueue(self.root)
        while (nodes_q.is_empty() == False):
            curr_node = nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if (curr_node.right is not None):
                nodes_q.enqueue(curr_node.right)


root_node - LinkedBinaryTree.Node(1)
my_tree = LinkedBinaryTree.Node(root_node)


    