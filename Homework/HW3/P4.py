def min_max(bin_tree):
    def subtree_min_max(subtree_root):
        if bin_tree is None:
            raise Exception("This tree is empty")
        else:
            left_min, left_max = min_max(subtree_root.left)
            right_min, right_max = min_max(subtree_root.right)
            minimum = None
            maximum = None
            if left_min < minimum:
                minimum = left_min
            if right_min < minimum:
                 minimum = right_min
            if left_max > maximum:
                maximum = left_max
            if right_max > maximum:
                maximum = right_max
        return (maximum, minimum)
    return subtree_min_max(subtree_root.root):