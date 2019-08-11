#Question 3


#Question 4
 def is_sum_balanced(bin_tree):
    total, value = is_subtree_sum_balanced(bin_tree.root)
     return total, value
      def is_subtree_sum_balanced(subtree_root):
            if subtree_root is None:
                return (0,True)
            else:
                left_sum, left_bool = is_subtree_sum_balanced(subtree_root.left)
                right_sum, right_bool = is_subtree_sum_balanced(subtree_root.right)
                total = left_sum + right_sum + subtree_root.data
                if left_bool == False or right_bool == False:
                    return (total, False)
                elif (-1 <= left_sum - right_sum) <=1:
                    return (total, True)
                else:
                    return (total,False)


