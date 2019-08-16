import ArrayQueue
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.parent = None
            self.left = left
            self.right= right

            if self.left is not None:
                self.left.parent = self
            if sel.right is not None:
                self.right.parent =self

    def __init__(self, root = None):
        self.root = root
        self.size = self.subtree_count(self.root)

    # return the number of nodes rooted by the node root
    def subtree_count(self,subtree_root):
        if subtree_root is None:
            return 0
        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)
        return left_count + right_count + 1

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return len(self) == 0

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

    def subtree_height(self, subtree_root):
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
        yield from self.subtree_preorder(self.subtree_root)
    
    #yields all values in the nodes of the subtree rooted at "subtree_root"
    def subtree_preorder(self.subtree_root):
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
