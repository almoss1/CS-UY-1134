import DoublyLinkedList

lnk_lst = DoublyLinkedList.DoublyLinkedList()
lnk_lst.add_last(2)
lnk_lst.add_last(4)
lnk_lst.add_last(6)
lnk_lst.add_last(3)
lnk_lst.add_last(17)
lnk_lst.add_last(42)
lnk_lst.add_last(-6)
lnk_lst.add_last(3)


def remove_all(lnk_lst,val):
    if lnk_lst.is_empty():
        return
    curr_node = lnk_lst.first_node()
    while curr_node is not lnk_lst.trailer:
        if curr_node.data == val:
            next_node = curr_node.next
            lnk_lst.delete_node(curr_node)
            curr_node = next_node
        else:
            curr_node = curr_node.next

print(lnk_lst)
remove_all(lnk_lst,3)
print(lnk_lst)


def max_in_array_list1(lst):
    if len(lst) == 1:
        return lst[0]
    res_max = max_in_arry_list1(lst[1:])
    return max(lst[0], res_max)
    #quadraic run time

def max_in_array_list2(lst):
    def max_in_array_list2_helper(lst,low,high):
        if low == high:
           return lst[low]
        else:
          rest_max = max_in_arry_list2(lst, low+1, high)
          return max(lst[low], rest_max)
    #linear run time
    return max_in_array_list2_helper(lst, 0, len(lst)-1)



def max_in_linked_list(lnk_lst):
    def max_in_linked_list_helper(lnk_lst,sublist_head):
        if sublist_head is lnk_lst.trailer:
            return sublist_head.data
        else:
            rest_max = max_in_linked_list_helper(lnk_lst,sublist_head.next)
            return max(sublist_head.data, rest_max)
    if lnk_lst.is_empty():
        raise Exception("List is empty")
    else:
        return max_in_linked_list_helper(lnk_lst, lnk_lst.first_node())


print(max_in_linked_list(lnk_lst))

