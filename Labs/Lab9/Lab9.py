def are_bst_keys_same(bst1, bst2):
    if bst1.data is None or bst2.data is None:
        return False
    if bst1.data is None and bst2.data is None:
        return True
    if bst1.data is not None and bst2.data is not None:
        if bst1.data == bst2.data:
            return True
        else:
            right = are_bst_keys_same(bst1.right, bst2.right)
            left = are_bst_keys_same(bst1.left, bst2.left)


    
def is_bst(binary_tree):
    return is_bst_helper(binary_tree.root)[0]
def is_bst_helper(subtree_root):
     if subtree_root is None: 
        return True
    else:
        left_bool, (left_min, left_max) = is_bst_helper(subtree_root.left)
        if subtree_root.data < left_min or subtree_root.data > left_max:
            return False
        right_bool, (right_min, right_max) = is_bst_helper(subtree_root.right)
        if subtree_root.data < right_min or subtree_root.data > right_max:
            return False
        bool_tot = left_bool + right_bool
        return bool_tot




def lca_bst(bst, node1, node2):
    while bst is not None: 
        if bst.data > node1 and bst.data > node2: 
            bst = bst.left 
        elif bst.data < node1 and bst.data < node2: 
            bst = bst.right 
  
        else: 
            break
  
    return bst 
  