#Written 
"""
1)
Preorder
ABDGCEFH
Inorder
BGDAECHF
Postorder
GDBEHFCA
2)3 
3)2

"""
import DoublyLinkedList

def right_circular_shift(lnk_lst):
    temp = trailer.prev
    temp2 = header.next
    header.next = temp
    trailer.prev = temp.prev
    temp2.prev = temp
    temp.prev = header
    trailer.prev.next = trailer
    temp.next = temp2


#3 count vals

def count_val(root, value):
    count = 0
    if root == None:
        return
    else:
        count_left = count_val(root.left,value)
        count_right = count_val(root.righ, value)
        count = count_left + count_right
        if root.data == value:
            count += 1
        return count
    


#Inverted Binary Tree
def invert_binary_tree(bin_tree):
    return LinkedBinaryTree(invert_subtree(bin_tree.root))

def invert_subtree(subtree_root):
    subtree_root = subtree_root
     if bin_tree is None:
        raise Expception('Tree is empty')
    else:
        if subtree_root.right is None and subtree_root.left is None:
            return subtree_root
        elif subtree_root.left is None and subtree_root.right is not None:
            right = invert_subtree(subtree_root.right)
            return LinkedBinaryTree.Node(subtree_root.data,right,None)
        elif subtree_root.left is not None and subtree_root.right is None:
            left = invert_subtree(subtree_root.left)
            return LinkedBinaryTree.Node(subtree_root.data,None,left)
        else:
            left =  invert_subtree(subtree_root.left)
            right = invert_subtree(subtree_root.right)
            return LinkedBinaryTree.Node(subtree_root.data,right,left)

#5  Count Number of leaves, 1-child, and 2-child nodes
 def subtree_children_dist(self, subtree_root):
     lst = [0,0,0]
     if subtree_root is None:
         return
    elif subtree_root.right is None and subtree_root.left is None:
        lst[0] =+ 1
    elif subtree_root.right is None and subtree_root.left is not None:
        lst[1] += 1
        subtree_children_dist(subtree_root.left)
    elif subtree_root.right is  not None and subtree_root.left is None:
        lst[1] += 1
         subtree_children_dist(subtree_root.right)
    else: #subtree_root.left and subtree_root.right is not none
        lst[2] += 1
        left = subtree_children_dist(subtree_root.left)
        right = subtree_children_dist(subtree_root.righ)
    return lst


